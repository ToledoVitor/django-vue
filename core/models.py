from django.db import models
from django.contrib.auth.models import User
# {% load static %}

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.SET_NULL)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )

class Jogo(models.Model):
    criador = models.CharField(max_length=512, null=True)
    esporte = models.CharField(max_length=512, null=True)
    data  = models.CharField(max_length=512, null=True)
    horas = models.CharField(max_length=512, null=True)
    descricao = models.CharField(max_length=512)
    imagem = models.ImageField(
        default='/media/images/basquete.jpg'
    )

    def to_dict_json(self):
        return {
            'criador': self.criador,
            'esporte': self.esporte,
            'data': self.data,
            'horas': self.horas,
            'descricao': self.descricao,
            'imagem': self.imagem
        }