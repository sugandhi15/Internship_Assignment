from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import UserSerializer
from .models import User
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
import jwt
from django.contrib.auth.hashers import check_password
import re
from .tasks import send_welcome_email



class hello_view(APIView):

    def get(self,request):
        try:
            return JsonResponse({"message": "Hello, there!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        



class registration(APIView):

    def post(self,request):
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            password = request.data.get('password')
            if not name or not email or not password:
                return JsonResponse({"error": "All fields are required"}, status=400)
            data = {
                "name": name,
                "email": email,
                "password": password
            }
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                payload = {
                    'name': serializer.validated_data["name"],
                    'email': serializer.validated_data["email"],
                    'password': serializer.validated_data["password"]
                }
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
                send_welcome_email.delay(
                    subject='Welcome!',
                    message='Thanks for registering.',
                    recipient_email=serializer.validated_data["email"]
                )
                return JsonResponse({"message": "User registered successfully" , "token": token}, status=201)
            return JsonResponse({"error": serializer.errors}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        

        

class login(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            if not email or not password:
                return JsonResponse({"error": "Email and password are required"}, status=400)
            try:
                user = User.objects.get(email=email)
                if not user:
                    return JsonResponse({"error" : "No user exist with this email"})
                if check_password(password,user.password):
                    token = jwt.encode({ 'name': user.name ,'email' : user.email ,'password' :user.password},settings.SECRET_KEY,algorithm=settings.JWT_SETTINGS['ALGORITHM'])
                    return JsonResponse({"message": "Login successful", "user": user.name ,"token": token}, status=200)
                return JsonResponse({"error": "Invalid email or password"}, status=401)
            except User.DoesNotExist:
                return JsonResponse({"error": "Invalid email or password"}, status=401)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)



class information(APIView):
    def get(self, request):
        try:
            token = request.headers.get('Authorization')
            if not token:
                return JsonResponse({"error": "Token is required"}, status=401)
            try:
                decode = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user = User.objects.get(email=decode['email'])
                return JsonResponse({"name": user.name, "email": user.email , "Information": "This is your information"}, status=200)
            except jwt.InvalidTokenError:
                return JsonResponse({"error": "Invalid token"}, status=401)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
