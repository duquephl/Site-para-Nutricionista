from django.db import models

# Create your models here.

from User.models import User

Choices_horario = (
    ('08:00', '08:00'),
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
)

Choices_status = (
    ('A', 'Agendado'),
    ('C', 'Cancelado'),
    ('F', 'Finalizado'),
    ('Livre', 'Livre'),
)

class Agendamento(models.Model):
    nome = models.ForeignKey('User.User', on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.CharField(max_length=5, choices=Choices_horario)
    status = models.CharField(max_length=5, choices=Choices_status, default='Livre')
    Data_Hora = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nome.nome + ' - ' + str(self.data) + ' - ' + self.horario

    def __display__(self):
        return User.objects.filter(id=self.nome_id).first().nome