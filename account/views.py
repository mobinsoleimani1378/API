from uuid import uuid4
from .permissions import IsUserOrReadOnly
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSer, OtpSer
from rest_framework.authentication import TokenAuthentication
from .models import User, Otp
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from random import randint


#
# class UserData(APIView):
#     # authentication_classes = [TokenAuthentication]
#
#     def get(self, request):
#         user = request.user
#         ser = UserSer(instance=user)
#         return Response(ser.data)


class UserAdd(APIView):
    def post(self, request):
        ser = UserSer(data=request.data)
        if ser.is_valid():
            ser.save()

            return Response(ser.data)
        else:
            return Response(ser.errors)


class UpdateUser(APIView):
    permission_classes = [IsUserOrReadOnly]

    def put(self, request, id):
        user = User.objects.get(id=id)
        self.check_object_permissions(request, user)
        ser = UserSer(data=request.data, instance=user, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'update': 'done'})


class signin(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        # fullname = request.data.get('fullname')

        user = None

        # if '@' in fullname:
        #     try:
        #         user = User.objects.get(email=fullname)
        #     except ObjectDoesNotExist:
        #         pass

        if not user:
            user = authenticate(username=phone, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'r': 'yes'})

        return Response({'error': 'invalid credential'})


class signout_user(APIView):
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OtpPhone(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        code = randint(1000, 9999)
        print(code)
        token = str(uuid4())
        instance = Otp.objects.create(phone=phone, code=code, token=token)
        ser = OtpSer(instance=instance)
        return Response({'token': ser.data})


class OtpCode(APIView):
    def post(self, request):
        code = request.data.get('code')
        token = request.data.get('token')
        if Otp.objects.filter(code=code, token=token).exists():
            otp = Otp.objects.get(token=token)
            user, is_created = User.objects.get_or_create(phone=otp.phone)
            token, _ = Token.objects.get_or_create(user=user)
            otp.delete()
            return Response({'user_id': user.id, 'token': token.key, 'login': 'yes'})
        else:
            return Response({'code': 'is not correct'})
