from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.title} - ${self.price}"

class Purchase(models.Model):
    quantity=models.IntegerField()  
    menu_id=models.ForeignKey(MenuItem,on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('gram', 'Gram'),
        ('ltr', 'Liter'),
        ('piece', 'Per Piece'),
    ]
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} (Qty: {self.quantity} {self.unit}, Unit Price: {self.unit_price})"
    
    
    
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipe_requirements')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_requirements')
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.menu_item.title} requires {self.quantity} {self.ingredient.name}"
    
    
 
class OrderItem(models.Model):
    food_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    table_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.food_item} - {self.table_name}"    