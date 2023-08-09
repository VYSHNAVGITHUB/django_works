from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework import authentication,permissions
from rest_framework.decorators import action


from django.contrib.auth.models import User
from movieapi.serializers  import UserSerializer,MovieSerializer,ReviewSerializer
from myapp.models import Movies,Reviews

from rest_framework_simplejwt.authentication import JWTAuthentication


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user==obj.user

class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    model=User
    http_method_names=["post"]



class MoviesView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    serializer_class=MovieSerializer
    queryset=Movies.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        movie_obj=Movies,object.get(id=kwargs.get("pk"))
        user=request.user

        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie_obj,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


class ReviewsView(GenericViewSet,DestroyModelMixin,UpdateModelMixin):
    serializer_class=ReviewSerializer
    queryset=Reviews.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]


