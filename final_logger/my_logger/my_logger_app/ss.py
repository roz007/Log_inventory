from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Event , EventRegistration

class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField( required = True, validators=[UniqueValidator(queryset=User.objects.all())])
    username=serializers.CharField( validators = [UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')



class EventSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    class Meta:
        model=Event
        fields=('id','Event_name','content','created_by','start_time','end_time','is_public','total_people','max_people')

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventRegistration
        field=('id','user','event')

