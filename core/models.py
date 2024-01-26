from django.db import models
from django.utils import timezone

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(AbstractModel, self).save(*args, **kwargs)

class Store(AbstractModel):
    title = models.CharField('Title',max_length=150, null=True, blank=True)
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    phone = models.CharField('Phone Number',max_length=150, null=True, blank=True)
    makes = models.CharField('Makes',max_length=150, null=True, blank=True)
    address = models.CharField('Address',max_length=150, null=True, blank=True)
    sm_url = models.CharField('Sosial Media URL',max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return f"{self.title}" 

class Order(AbstractModel):
    title = models.CharField('Title',max_length=150, null=True, blank=True)
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    phone = models.CharField('Phone Number',max_length=150, null=True, blank=True)
    car = models.CharField('Car',max_length=150, null=True, blank=True)
    vin = models.CharField('Vin',max_length=150, null=True, blank=True)
    engine = models.CharField('Engine',max_length=150, null=True, blank=True)
    year = models.CharField('Year',max_length=150, null=True, blank=True)
    body = models.CharField('Body',max_length=150, null=True, blank=True)
    country = models.CharField('Country',max_length=150, null=True, blank=True)
    transmission = models.CharField('Transmission',max_length=150, null=True, blank=True)
    fuel = models.CharField('Fuel',max_length=150, null=True, blank=True)
    turbo = models.BooleanField(default=False)
    airbags = models.CharField('Airbags',max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.title} for {self.car}" 
    
class Contact(AbstractModel):
    name = models.CharField('Name',max_length=150, null=True, blank=True)
    email = models.CharField('Email',max_length=150, null=True, blank=True)
    phone = models.CharField('Phone',max_length=150, null=True, blank=True)
    message = models.CharField('Message',max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.name}"