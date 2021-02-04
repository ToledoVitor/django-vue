from core.models import Jogo
from datetime import date, datetime
from itertools import groupby
from collections import namedtuple
from django.contrib.auth.models import User
import ast
import json
import operator

def list_jogos():
    lista = Jogo.objects.order_by('esporte').all()
    return lista

def list_for_user():
    lista = Jogo.objects.order_by('esporte').all()
    return lista

def list_jogos_by_esporte():
    jogos = list_jogos()
    jogos_agrupados = []
    for esporte, grupo_jogos in groupby(jogos, operator.attrgetter("esporte")):
        jogos_agrupados.append({"esporte": esporte, "jogos": [jogo.to_dict_json() for jogo in grupo_jogos]})
    return jogos_agrupados

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
    jogo = json.loads(jogo)
    jogo_id = jogo['id']
    participantes = jogo['participantes']
    participantes += f", {username}" if participantes else username
    jogo_db = Jogo.objects.get(id=jogo_id)
    jogo_db.participantes = participantes
    jogo_db.save()
    return jogo

def unparticipate(username, jogo):
    jogo = json.loads(jogo)
    jogo_id = jogo['id']
    participantes = jogo['participantes']
    participantes = participantes.replace(f", {username}", '').replace(username, '')
    jogo_db = Jogo.objects.get(id=jogo_id)
    jogo_db.participantes = participantes
    jogo_db.save()
    return jogo