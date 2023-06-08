from rest_framework import serializers

        
class EmployeeSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100,required=False)
    email=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100,required=False)
    
  