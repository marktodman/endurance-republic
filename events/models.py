from django.db import models


STATUS = ((0, 'Draft'), (1, 'Published'))
DIFFICULTY = ((0, "Super easy"), (1, "Easy"), (2, "Moderate"), (
    3, "Challenging"), (4, "Very challenging"), (5, "Extremely challenging"))


# Customer model for creating Activities
class Activity(models.Model):
    """Acitivty Model"""

    class Meta:
        verbose_name_plural = 'Activities'

    type = models.CharField(
        'Activity type', max_length=200, null=False, blank=False, unique=True)
    published_status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        """Return Activity type as the Activity object"""
        return str(self.type)


# Customer model for creating Events associated with Activities
class Event(models.Model):
    """Event Model"""
    activity = models.ForeignKey(
        'Activity', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(
        'Event Name', max_length=200, blank=False, unique=False)
    description = models.TextField('Description', blank=False, unique=False)
    duration = models.IntegerField('Duration (days)', null=False, blank=False)
    distance = models.IntegerField(
        'Distance (km)', null=False, blank=False)
    location = models.CharField(
        'Location', max_length=200, blank=False, unique=False)
    date = models.DateField('Date')
    difficulty = models.IntegerField(choices=DIFFICULTY, default=3)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    published_status = models.IntegerField(choices=STATUS, default=0)
    featured_image = models.ImageField(null=True, blank=True)

    class Meta:
        """Order events by date"""
        ordering = ['date']

    def __str__(self):
        """Return Event Name as the Event object"""
        return str(self.name)
