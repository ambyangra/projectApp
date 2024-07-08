from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser
from ..models import User
from ..serializers import UserSerializer

class UserDetailView(APIView):
    def get(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            return Response({
                'id': None,
                'username': '',
                'user_type': None,
                'is_coach': False,
                'is_player': False,
                'is_league_admin': False,
            })
        serializer = UserSerializer(user)
        return Response(serializer.data)