from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#user models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} Profile" 


class Recipe(models.Model):
  recipe_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  description = models.TextField()
  photo = models.ImageField() 
  category = models.CharField(max_length=200)
  created_by = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recipes')

class PreparationSteps(models.Model):
  pstep_id = models.AutoField(primary_key=True)
  steps = models.TextField()
  created_by = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='psteps')
  user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='psteps')

class Ingredients(models.Model):
  ingredient_id = models.AutoField(primary_key=True) 
  steps = models.TextField()
  created_by = models.varchar(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='ingredients')
  user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ingredients')

class Comments(models.Model):
  comment_id = models.AutoField(primary_key=True)
  steps = models.TextField()
  commented_by = models.varchar(max_length=50)
  commented_at = models.DateTimeField(auto_now_add=True)
  user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')

class Ratings(models.Modeel):
  rating_id = models.AutoField(primary_key=True)
  steps = models.TextField()
  rated_by = models.varchar(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings') 
