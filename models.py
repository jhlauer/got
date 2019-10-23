from django.db import models
from django.core.validators import MinLengthValidator

#example models 
class House(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Type must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Culture(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Type must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Type must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")])
    house = models.ForeignKey('House', on_delete=models.CASCADE, null=False)
    culture = models.ForeignKey('Culture', on_delete=models.CASCADE, null=True)
    title = models.ForeignKey('Title', on_delete=models.CASCADE, null=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.nickname

class Child(models.Model):
        pass

class Parent(models.Model):
        pass

class Sibling(models.Model):
        pass

class Spouse(models.Model):
        pass
