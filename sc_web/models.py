from django.db import models

# Create your models here.
class Brand_Product(models.Model):
    name = models.CharField(max_length=100)

class Model_Product(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    brand_id = models.ForeignKey(Brand_Product, on_delete=models.CASCADE)
    model_id = models.ForeignKey(Model_Product, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=200)

class Type_Operation(models.Model):
    name = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''