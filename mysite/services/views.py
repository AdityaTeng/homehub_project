from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import RegisterForm

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Request
from .serializers import RequestSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/mymodule/account')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


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
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
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