from django.db import models

from registration.models import User

ORDER_STATUSES_CHOICES = (
    ('New', 'New'),
    ('Rejected', 'Rejected'),
    ('Approved', 'Approved'),
    ('Research', 'Research'),
    ('Archieved', 'Archieved'),
)


class Order(models.Model):
    title = models.CharField(
        max_length=40,
    )
    description = models.TextField()
    orderer = models.ForeignKey(User)
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUSES_CHOICES,
        default='New',
    )

    def __str__(self):
        return self.title
