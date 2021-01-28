from core.models import Jogo

def list_jogos():
    lista = Jogo.objects.all()
    return lista
    