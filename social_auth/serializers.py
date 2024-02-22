from rest_framework import serializers

from social_auth.register import register_social_user
from . import google
import os
from rest_framework.exceptions import AuthenticationFailed

class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()
    
    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError('The token is invalid or expired')
        
        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
            raise AuthenticationFailed('The token is invalid')
        
        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'
        
        # print(user_id, email, name, provider)
        
        return register_social_user(provider=provider, user_id=user_id, email=email, name=name)