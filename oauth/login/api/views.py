from rest_framework.generics import ListAPIView,viewsets

from login.models import User
from .serializers import PostSerializer
class PostListAPIView(ListAPIView):

	queryset=User.objects.all()
	serializer_class=PostSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer