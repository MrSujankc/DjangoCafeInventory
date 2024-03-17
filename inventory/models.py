from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=25)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipe_requirements')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_requirements')
    quantity = models.IntegerField(default=0)
    
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='purchases')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Purchased Date')
 
    