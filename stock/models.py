from django.db import models

from registration.models import User

ORDER_STATUSES_CHOICES = (
    ('New', 'New'),
    ('Rejected', 'Rejected'),
    ('Approved', 'Approved'),
    ('Research', 'Research'),
    ('Archieved', 'Archieved'),
)

PROJECT_STATUSES_CHOICES = (
    ('Draft', 'Draft'),
    ('Approved', 'Approved'),
    ('Operative', 'Operative'),
    ('Inoperative', 'Inoperative'),
)


class Order(models.Model):
    title = models.CharField(
        max_length=40,
    )
    description = models.TextField()
    orderer = models.ForeignKey(User, related_name='orders')
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUSES_CHOICES,
        default='New',
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    order = models.OneToOneField(Order, related_name='project')
    status = models.CharField(
        max_length=15,
        choices=PROJECT_STATUSES_CHOICES,
        default='Draft',
    )
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title


class CrossProjectUser(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    role = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return '{0} : {1}'.format(self.user, self.project)
