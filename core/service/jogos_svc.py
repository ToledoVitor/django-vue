from core.models import Jogo
from datetime import date, datetime

def list_jogos():
    lista = Jogo.objects.all()
    return lista

def create_jogo(criador, esporte, dia, horas, descricao, imagem, participantes):
    jogo = Jogo.objects.create(criador=criador, esporte=esporte, dia=date.fromisoformat(dia), horas=horas, descricao=descricao, imagem=imagem, participantes=participantes)
    return jogo.to_dict_json()

def search_info(info):
    jogos = Jogo.objects.filter(esporte=info)
    jogos = list(jogos)
    lista_jogos = []
    for jogo in jogos:
        lista_jogos.append(jogo.to_dict_json())    
    return lista_jogos

def participate(username, jogo):
    jogo["participantes"].append[username]
    return jogo

def unparticipate(username, jogo):
    jogo["participantes"].remove[username]
    return jogo