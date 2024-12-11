from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FeedSerializer
from rest_framework.exceptions import NotFound
from .models import Feed


class Feeds(APIView):
	def get(self, request):
		feeds = Feed.objects.all()
		# many=True, feeds 객체가 단일 객체이면 many=False(기본값)
		# Feed 모델은 다른 객체도 참조하고 있기 때문에 many=True로 변경 필요. (여러 객체 직렬화)
		# 객체 -> JSON (시리얼라이즈)
		serializer = FeedSerializer(feeds, many=True)
		return Response(serializer.data)
	
	def post(self, request):
		serializer = FeedSerializer(data=request.data)
		# JSON => Serialize한 데이터를 Feed Model을 기반으로 data validation
		if serializer.is_valid():
			# save()함수가 정상실행되면 => serializer의 create() 함수 실행됨
			# request를 날린 유저의 데이터를 Feed에 저장
			feed = serializer.save(user=request.user)
			serializer = FeedSerializer(feed)
			return Response(serializer.data)

		else:
			return Response(serializer.errors)

		


class FeedDetail(APIView):
	def get_object(self, feed_id):
		try:
			return Feed.objects.get(id=feed_id)
		except Feed.DoesNotExist:
			raise NotFound
	
	def get(self, request, feed_id):
		feed = self.get_object(feed_id)
		serializer = FeedSerializer(feed)
		return Response(serializer.data)