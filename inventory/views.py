
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement, OrderItem
from .forms import IngredientForm, MenuItemForm, RecipeForm, OrderItemForm


# Create your views here.
class HomeView(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context
    
    

class MenuView(ListView):
    template_name = "inventory/menu_list.html"
    model = MenuItem 
    
    
class AddMenuItemView(CreateView):
    template_name = "inventory/add_menu_item.html"
    model = MenuItem
    form_class = MenuItemForm
    success_url = reverse_lazy ('inventory:menu')
    
    
class IngredientsView(ListView):
    template_name = "inventory/ingredients_list.html"
    model = Ingredient


class AddIngredientView(CreateView):
    template_name = "inventory/add_ingredient.html"
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy ('inventory:ingredients')


class UpdateIngredientView(UpdateView):
    template_name = "inventory/update_ingredient.html"
    model = Ingredient
    form_class = IngredientForm  
    success_url = reverse_lazy ('inventory:ingredients')     
    
    
# class AddRecipeRequirementView(CreateView):
#     template_name = "inventory/add_recipe_requirements.html"
#     model = RecipeRequirement
#     form_class = RecipeRequirementForm  
#     success_url = reverse_lazy ('inventory:menu')   
    


class OrderList(ListView):
    model = OrderItem
    context_object_name = 'order'
    template_name='inventory/order_list.html'
    
    
    
class RecipeList(ListView):
    model = RecipeRequirement
    context_object_name = 'recipe'
    template_name='inventory/recipe_list.html' 
 
 
class AddRecipe(CreateView):
    model = RecipeRequirement
    form_class=RecipeForm
    template_name = "resturant/add_recipe.html"
    success_url = reverse_lazy('inventory:recipe')
    def form_valid(self, form):
        menu_item_id = self.kwargs['menu_item_id']
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        form.instance.menu_item = menu_item
        return super().form_valid(form) 
 
 
    
class AddOrder(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "inventory/add_order.html"
    success_url = reverse_lazy('inventory:order')

    def form_valid(self, form):
      
        response = super().form_valid(form)

     
        order_id = self.object.pk
        
        try:

            order_item = OrderItem.objects.get(pk=order_id)

            menu_item = order_item.food_item

            recipe_requirements = RecipeRequirement.objects.filter(menu_item=menu_item)

        
            for requirement in recipe_requirements:
                ingredient = requirement.ingredient
                quantity_used = requirement.quantity * order_item.quantity
                ingredient.available_qty -= quantity_used
                ingredient.save()
            total_price = order_item.quantity * order_item.food_item.price
            context = {
                'total_price': total_price,
            }
                

        except OrderItem.DoesNotExist:
         
            return HttpResponseRedirect('/error/')
        
      
        return render(self.request, 'resturant/calculation_ingredient.html',context) 
    
        
    