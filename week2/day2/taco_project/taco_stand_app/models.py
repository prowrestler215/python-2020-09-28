from django.db import models


# Create your models here.
class Taco(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # who updated it
    # objects


# from taco_stand_app.models import Taco
# Taco.objects.all()
# Taco.objects.create(
#     name='Carne Asada Taco',
#     description='Beef',
#     price='1.20',
#     image_url='http://sweetcarolinescooking.files.wordpress.com/2013/06/img_37371.jpg'
# )

# Taco.objects.create(
#     name='Al pastor',
#     description='Pork',
#     price='2.50',
#     image_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.DVRT37scVrJf0p_CoGulRQHaDa%26pid%3DApi&f=1'
# )
