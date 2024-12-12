from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import FeedUserSerializer

class ReviewSerializer(ModelSerializer):
    user = FeedUserSerializer() # 추가

    class Meta:
        model = Review
        fields = "__all__"
        # fields = ("id", "content", "likes_num")