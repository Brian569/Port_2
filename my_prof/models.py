from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    image = CloudinaryField()
    email = models.EmailField()
    contact_me = CloudinaryField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class Pictures(models.Model):
    # phone_number = PhoneNumberField()
    project_1 = CloudinaryField()
    project_2 = CloudinaryField()
    project_3 = CloudinaryField()
  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"