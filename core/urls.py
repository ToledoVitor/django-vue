from django.urls import path
from . import views

urlpatterns = [
    path('api/dapau', views.dapau),
    path('api/whoami', views.whoami),
    path('api/settings', views.settings),

    path('api/list_jogos', views.list_jogos),
    path('api/creategame', views.create_jogo),

    path('api/register', views.registerPage, name="register"),
    path('api/login', views.loginPage, name="login")
]
