from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import CustomUserCreationForm, ProfileUpdateForm
from .serializer import ProfileSerializer
from .models import Profile
from rest_framework import status

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            # Create a Profile for the user
            Profile.objects.create(
                user=user,
                name=request.data.get('name'),  # Retrieve name from the request
                email=request.data.get('email'),  # Retrieve email from the request
            )
            return Response({'message': 'User and Profile created successfully'}, status=201)
    return Response({'error': 'Invalid data'}, status=400)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=200)
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
    return Response({'error': 'Invalid request method'}, status=400)

#okok

@api_view(['POST'])
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({'message': 'Logout successful'}, status=200)
    return Response({'error': 'User not authenticated'}, status=401)


# @api_view(['GET', 'PUT'])
# @login_required
# def profile_update(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     profile = user.profile

#     if request.method == 'PUT':
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'GET':
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data, status=200)

#     return Response({'error': 'Invalid request method'}, status=400)


# @api_view(['GET'])
# def profile_detail(request, user_id):
#     try:
#         user = User.objects.get(pk=user_id)
#         profile = Profile.objects.get(user=user)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except User.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Profile.DoesNotExist:
#         return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
