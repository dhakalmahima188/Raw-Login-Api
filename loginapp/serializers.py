from rest_framework import serializers

        
class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField(required=False)
    username=serializers.CharField(max_length=100,required=False)
    email=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100,required=False)
    
    def create(self, validated_data):
        return validated_data
    
  