from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer

from login.models import User
class PostSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
			'username',
			'usertype',
			'userAvatarUrl',
			'createdDate'
		]


class UserSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = [
			'username',
			'usertype',
			'userAvatarUrl',
			'createdDate'
		]
