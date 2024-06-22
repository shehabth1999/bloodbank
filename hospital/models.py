from django.db import models
from authentication.models import BloodType, BaseUser

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    map_url = models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    number_of_bags = models.PositiveIntegerField(default=0)
    is_required = models.BooleanField(default=True)

    class Meta:
        unique_together = ('hospital', 'blood_type')

    def __str__(self):
        return f'{self.hospital.name} - {self.blood_type.type}: {self.number_of_bags} bags'
    

class DonationRequest(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
