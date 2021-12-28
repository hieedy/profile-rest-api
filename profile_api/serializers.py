from rest_framework import serializers

from profile_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length = 10)

# serializer here we are used is ModelSerializer
# it's similar to normal serializer but provide
# some more predefined functions that makes our task easier
# to work with existing djnago database model.

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model  = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
        'password' : {
            'write_only' : True,
            'style':{ 'input_type':'password'}
            }
        }


    #overriding the default create method which invoked by serializers
    # after valdating the data throught the information provided in META class
    # becaouse other wise default create method will store the password in the plain text format
    def create(self, validated_data):
        """Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user
        
