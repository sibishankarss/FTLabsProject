from django.db import models

# Create your models here.
class User(models.Model):
	real_name = models.CharField(max_length=60)
	tz = models.CharField(max_length=60)
	def __str__(self):
		return self.real_name

class ActivityPeriod(models.Model):
	user = models.ForeignKey(User, related_name='activity_periods',on_delete=models.DO_NOTHING)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	class Meta:
		unique_together = ('user','start_time')
	def __unicode__(self):
		return self
