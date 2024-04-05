from . import views
from django.urls import path
app_name = 'inventory'


urlpatterns = [
     path('', views.HomeView.as_view(), name='home'),
     path('menu/', views.MenuView.as_view(), name="menu"),
     path('menulist/', views.MenuView.as_view(), name="menu-list"),
     path('add/menu/', views.AddMenuItemView.as_view(), name="menu-add"),
     path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
     path('add/ingredients/', views.AddIngredientView.as_view(), name="add-ingredients"),
     path('ingredients/<slug:pk>/update', views.UpdateIngredientView.as_view(), name="update-ingredients"),
     path('Order/', views.OrderList.as_view(), name="order"),
     path('add/Order', views.AddOrder.as_view(), name="add-order"),
     path('recipe/', views.RecipeList.as_view(), name="recipe"),
     path('add-recipe-requirement/<int:menu_item_id>/', views.AddRecipe.as_view(), name='add-recipe'),
]
