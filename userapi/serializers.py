from rest_framework import serializers

from .models import User,ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	activity_periods = ActivityPeriodSerializer(many=True)
	class Meta:
		model = User
		fields = ('id','real_name', 'tz','activity_periods')
	def create(self, validated_data):
		user_validated_data = validated_data.pop('activity_periods')
		user = User.objects.create(**validated_data)
		activity_period_set_serializer = self.fields['activity_periods']
		for each in user_validated_data:
			each['user'] = user
		choices = activity_period_set_serializer.create(user_validated_data)
		return user
