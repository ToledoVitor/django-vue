from django.contrib import admin

from core.models import ActivityLog, Jogo


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class JogoAdmin(admin.ModelAdmin):
    list_display = ('criador', 'esporte', 'dia', 'horas', 'imagem', 'descricao', 'participantes')

admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Jogo, JogoAdmin)