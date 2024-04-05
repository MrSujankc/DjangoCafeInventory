
from django import forms
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement, OrderItem


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"
        
        
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"
        
        
class RecipeForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"
                
        