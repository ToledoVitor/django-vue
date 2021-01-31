# coding: utf-8
import json
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.shortcuts import render, redirect
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, globalsettings_svc, jogos_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')

def registerPage(request):
    context = {}
    return render(request, 'accounts/register', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context )

# @csrf_exempt
# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = auth.authenticate(username=username, password=password)
#     user_dict = None
#     if user is not None:
#         if user.is_active:
#             auth.login(request, user)
#             log_svc.log_login(request.user)
#             user_dict = _user2dict(user)
#     return JsonResponse(user_dict, safe=False)


# def logout(request):
#     if request.method.lower() != 'post':
#         raise Exception('Logout only via post')
#     if request.user.is_authenticated:
#         log_svc.log_logout(request.user)
#     auth.logout(request)
#     return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


def settings(request):
    le_settings = globalsettings_svc.list_settings()
    return JsonResponse(le_settings)

def list_jogos(request):
    lista = list(jogos_svc.list_jogos())
    jogos = []
    for i in lista:
        jogos.append(i.to_dict_json())
    return JsonResponse(jogos, safe=False)

def create_jogo(request):
    criador = request.POST['criador']
    esporte = request.POST['esporte']
    data = request.POST['data']
    horas = request.POST['horas']
    descricao = request.POST['descricao']
    imagem = request.POST['imagem']
    jogo = jogos_svc.create_jogo(
        criador=criador, esporte=esporte, data=data, horas=horas, descricao=descricao, imagem=imagem)
    return JsonResponse(jogo, safe=False)

def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d