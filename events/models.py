from django.db import models


STATUS = ((0, 'Draft'), (1, 'Published'))
DIFFICULTY = ((0, "Super easy"), (1, "Easy"), (2, "Moderate"), (
    3, "Challenging"), (4, "Very challenge"), (5, "Extremely challenging"))


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


class Event(models.Model):
    """Event Model"""
    activity = models.ForeignKey('Activity', null=True, blank=True, on_delete=models.SET_NULL)
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
    published_status = models.IntegerField(choices=STATUS, default=0)
    featured_image = models.ImageField(null=True, blank=True)

    class Meta:
        """Order events by date"""
        ordering = ['date']

    def __str__(self):
        """Return Event Name as the Event object"""
        return str(self.name)
