from django.contrib import admin
from .models import Ingredient
from .models import MenuItem
from .models import RecipeRequirement
from .models import Purchase
from .models import OrderItem

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)
admin.site.register(OrderItem)
