from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country-detail', args=[str(self.pk)])


# City model
class City(BaseModel):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city-detail', args=[str(self.pk)])

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ad(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    images = models.ManyToManyField('Image')
    
    def __str__(self):
        return self.title

class Image(BaseModel):
    image = models.ImageField(upload_to='ad_images')

class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CustomField(BaseModel):
    TEXT = 'text'
    NUMBER = 'number'
    DATE = 'date'
    FIELD_TYPE_CHOICES = [
        (TEXT, 'Text'),
        (NUMBER, 'Number'),
        (DATE, 'Date'),
    ]

    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=10, choices=FIELD_TYPE_CHOICES)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
