from core.models import Jogo
from datetime import date, datetime
from itertools import groupby
import ast
import operator

def list_jogos():
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
    jogo = ast.literal_eval(jogo)
    subst = jogo.get('participantes')
    subst = ast.literal_eval(subst)
    add = subst.append(username)
    jogo["participantes"] = str(subst)
    return str(jogo)

def unparticipate(username, jogo):
    jogo = ast.literal_eval(jogo)
    subst = jogo.get('participantes')
    subst = ast.literal_eval(subst)
    rmv = subst.remove(username)
    jogo["participantes"] = str(subst)
    return jogo