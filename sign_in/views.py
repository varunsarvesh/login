from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from sign_in.functions import register, login , Username_already_exist_Error, Username_dosent_exist_Error, Username_password_missmatch_Error
from . import forms


def index(request):
    form = forms.signup()
    return render(request, 'login/index.html', {'form': form})


def verify(request):
    if request.method == 'POST':
        form = forms.signin(request.POST)
        username = form.data['username']
        password = form.data['password']
        print(form)
        try:
            if login(username, password):
                return render(request, 'login/signed.html')
            else:
                return  HttpResponse('duhx  ')
        except Username_dosent_exist_Error:
            return HttpResponse('username dosent exist')
        except Username_password_missmatch_Error:
            return HttpResponse('username & pass dosent match')


def sign_up(request):
    form = forms.signup()
    return render(request, "login/signup.html", {'form': form})


def test_post(request):
    import pdb;pdb.set_trace()


class signed_up(APIView):
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser, )

    @staticmethod
    def post(request):
        # if request.method == 'POST':
        form = forms.signup(request.POST)
        # username = form.data['username']
        # password = form.data['password']
        username = request.data['username']
        password = request.data['password']
        data = []
        data.append([{'username':username}, {'password':password}])
        return Response({"data": data})

        #     # email = form.data['email']
        #     try:
        #         register(username, password)
        #         return render(request, "login/index.html", {'form': form})
        #     except Username_already_exist_Error:
        #         return HttpResponse('Username already present')