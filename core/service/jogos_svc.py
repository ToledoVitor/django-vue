from core.models import Jogo

def list_jogos():
    lista = Jogo.objects.all()
    return lista

def create_jogo(criador, esporte, data, horas, descricao, imagem):
    jogo = Jogo.objects.create(criador=criador, esporte=esporte, data=data, horas=horas, descricao=descricao, imagem=imagem)
    return jogo.to_dict_json()
