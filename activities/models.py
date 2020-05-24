from django.db import models
from users.models import User


class Activity(models.Model):
    class Meta:
        db_table = 'activities'

    CATGRY_CHOICES = [
        ('ST', 'Study'),
        ('SP', 'Sports'),
        ('VO', 'Volunteer'),
        ('PO', 'Project'),
        ('EN', 'Entertainment'),
        ('UN', 'Unknown')
    ]

    name = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATGRY_CHOICES,
        default='UN'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    address = models.TextField()
    male_wanted = models.IntegerField(default=0)
    female_wanted = models.IntegerField(default=0)
    male_joined = models.IntegerField(default=0)
    female_joined = models.IntegerField(default=0)
    publisher = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    joined_users = models.ManyToManyField(User, through='Join', related_name='joined_activity')
    liked_users = models.ManyToManyField(User, through='Like', related_name='liked_activity')
    favored_users = models.ManyToManyField(User, through='Favourite', related_name='favoured_activity')
    watched_times = models.BigIntegerField(default=0)


class Join(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date_time = models.DateTimeField()


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date_time = models.DateTimeField()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
