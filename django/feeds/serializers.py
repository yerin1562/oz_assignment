from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer

class FeedSerializer(ModelSerializer):

    user = FeedUserSerializer() # feed 의 user모델을 직렬화 하기 위해 필요한 코드

    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1
            # 현재의 모델과 연결된 모델들까지 serialize 시키겠다는 뜻        
            # Feed - User 모델 => 현재 코드는 Feed 모델 객체를 직렬화 하고 있지만,
            # depth = 1 이라는 코드를 통해 User 객체도 직렬화하겠다는 뜻.
            #depth = 1 # objects도 serialize화 시킴