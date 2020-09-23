from django.db import models
import uuid
from django.conf import settings
import PIL
from fontawesome_5.fields import IconField
from django.shortcuts import reverse


# Create your models here.


class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_start_price = models.FloatField()
    time_needed = models.TimeField(default='00:30')
    slug = models.SlugField(default='tattoo-service')

    def __str__(self):
        return self.service_title

    def get_absolute_url(self):
        return reverse('tattoo:service-details', kwargs={'slug': self.slug})

    def add_to_cart_url(self):
        return reverse('tattoo:add-service-to-cart',
                       kwargs={'slug': self.slug})


class OrderedService(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.service.service_title}'

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    services = models.ManyToManyField(OrderedService)

    ordered_date = models.DateTimeField()

    def get_time_needed(self):
        return self.services.time_needed
    # order_created_time
    #


class PortfolioPhoto(models.Model):
    image = models.ImageField()


class Icon(models.Model):
    icon = IconField()
