#from django.contrib.auth.models import User
from userapi.models import ActivityPeriod,User
from django.core.management.base import BaseCommand
import datetime
import random

class Command(BaseCommand):
	help = 'Create Users'

	def add_arguments(self, parser):
		parser.add_argument('real_name', type=str, help='name of the user to be created')
		parser.add_argument('count_ap',type=int,help='count of activity periods')
		parser.add_argument('timezone_ip',type=str,help='timezone whichneeds to be set')

	def handle(self, *args, **kwargs):
		username = kwargs['real_name']
		timezone_ip = kwargs['timezone_ip']
		max_count = kwargs['count_ap']
		user= User.objects.create(real_name=username,tz=timezone_ip)
		start_time = end_time = datetime.datetime.now()
		count = 0
		while (count < max_count) :
			start_time = end_time
			end_time = start_time + datetime.timedelta(seconds=random.randint(1,7000))
			ActivityPeriod.objects.create(start_time=start_time,end_time=end_time,user_id=user.id)
			count = count + 1