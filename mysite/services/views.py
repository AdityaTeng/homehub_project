from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import RegisterForm

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Request
from .serializers import RequestSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view


# Create your views here.
def home(request):
    print("HOME")
    queryset = []
    context = {}
    if str(request.user) == 'AnonymousUser':
        return render(request, 'index.html')
        # return redirect("/login")
    elif request.method=="GET":
        queryset = Request.objects.all().filter(user=request.user)
        print(queryset)#User.id, User.username)
        if User.is_authenticated:
            context['Requests'] = queryset
            return render(request, 'index.html', context)
        else:
            return redirect("/login")

# Create your views here.
class ListRequestView(generics.ListAPIView):
    """Provides a get method handler."""
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


# class SongsViewSet(viewsets.ModelViewSet):
#     queryset = Songs.objects.all().order_by('title')
#     serializer_class = SongsSerializer

@api_view(['GET', 'POST'])
def get_request(request):
    """GET and POST Service Request"""
    if request.method == 'GET':
        print("GET")
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("POST1")
        print(request.data)
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            print('True')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    queryset = []
    context = {}
    queryset = Request.objects.all()
    # try:
    #     if request.user.is_superuser:
    #         queryset = Lead.objects.all()
    #     else:
    #         user = SalesPersonUser.objects.filter(email=request.user).first()
    #         queryset = Lead.objects.filter(assigned_to=user.id)
    # except:
    #     pass
    
    context['Requests'] = queryset
    return render(request, 'requests.html', context)

def new_request(request):
    return render(request, 'new_request.html')