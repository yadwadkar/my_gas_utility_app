from django.db import models

# Create your models here.
from accounts.models import Customer

# Service Request model to store customer service requests
class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('Installation', 'Installation'),
        ('Maintenance', 'Maintenance'),
        ('Repair', 'Repair'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    file = models.FileField(upload_to='service_files/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.user.username} - {self.service_type} - {self.status}"
