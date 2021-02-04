from core import views
from django.urls import path

urlpatterns = [
    path('api/dapau', views.dapau),
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/whoami', views.whoami),
    path('api/settings', views.settings),
    path('api/list_jogos', views.list_jogos),
    path('api/list_for_user', views.list_for_user),
    path('api/creategame', views.create_jogo),
    path('api/search_info/<str:info>', views.search_info),
    path('api/participate/username=<str:username>/jogo=<str:jogo>', views.participate),
    path('api/unparticipate/username=<str:username>/jogo=<str:jogo>', views.unparticipate)
]
