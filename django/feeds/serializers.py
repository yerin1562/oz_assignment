from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):

    user = FeedUserSerializer(read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
		# read_only => API 결과값에는 보이지만, put/post를 할 때는 파라미터를 넣어주지 않아도 된다.

    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1
            # 현재의 모델과 연결된 모델들까지 serialize 시키겠다는 뜻        
            # Feed - User 모델 => 현재 코드는 Feed 모델 객체를 직렬화 하고 있지만,
            # depth = 1 이라는 코드를 통해 User 객체도 직렬화하겠다는 뜻.
            #depth = 1 # objects도 serialize화 시킴