from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MyInfoUserSerializer
from rest_framework.exceptions import NotFound, ParseError
from django.contrib.auth.password_validation import validate_password
from rest_framework.authentication import TokenAuthentication # 사용자 인증 (추가)
from rest_framework.permissions import IsAuthenticated # 권한 부여 (추가)
from django.contrib.auth import authenticate, login
from rest_framework import status

# api/v1/users/myinfo [POST]
class Users(APIView):
    # read
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)

    # post
    def post(self, request):
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)

        try:
            validate_password(password)
        except: 
            raise ParseError("Incalid password")

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return ParseError(serializer.errors)
        

# api/v1/users/myinfo [GET,PUT]
class MyInfo(APIView):
    authentication_classes = [TokenAuthentication] # 추가
    permission_classes = [IsAuthenticated] # 추가
    
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)

    # update
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


# api/v1/users/login
class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError()

				#위 아래 둘 중 하나 사용

        # if not (username and password):
            # raise ParseError()

        user = authenticate(request, username=username, password=password)
        print(user)

        if user:
            # 아래 코드 실행시 sessionid, csrftoken이 생성
            # sessionid는 사용자 세션과 관련된 상태 정보를 식별하기 위한 고유한 식별자입니다.
            # 이를 클라이언트(웹 브라우저)에 쿠키로 저장함으로써,
            # 브라우저가 서버에 요청할 때마다 해당 세션과 관련된 데이터를 식별하여 사용자 상태를 유지할 수 있습니다.
            # 단, localhost:3000에서는 실행 안됨.

            # csrftoken: csrf공격 방지를 위해 필요한 토큰
            # ex) 은행앱에 로그인된 상태에서 악의적인 사이트에서 어떤 행동들을 하면
            # 쿠키에 있는 값을 털어서 해당 사용자인척 은행 API로 송금 요청을 시도
            # 일반적으로 Django의 기본 설정에서 세션과 CSRF 토큰은 세션 쿠키와 관련된 도메인과 경로에 한정하여 사용됩니다.
            # 따라서 http://127.0.0.1:3000/에서 로그인한 후 다른 URL로 이동하면 해당 URL과 경로에 대한 세션과 CSRF 토큰은 적용되지 않습니다.
            login(request, user)
            return Response({"message":"success"}, status=status.HTTP_200_OK) # 이 부분을 수정
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        


# django의 session을 활용한 로그아웃
from django.contrib.auth import logout

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("request", request.headers)
        logout(request)
        return Response(status=status.HTTP_200_OK)
    

import jwt
from django.conf import settings

class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError

        user = authenticate(request, username=username, password=password)

        if user:
            payload = {"id": user.id, "username": user.username}
            
            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            
            return Response({"token": token})
        

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from config.authentication import JWTAuthentication

class UserDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username
        })