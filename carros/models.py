from django.db import models
from uuid import uuid4


class Carros(models.Model):
    id_carrro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_carro = models.CharField(max_length=255)
    fabrica_carro = models.CharField(max_length=255)
    modelo_carro = models.CharField(max_length=255)
    ano_modelo = models.IntegerField()
    motor_carro = models.FloatField()
    kilometragem = models.FloatField()
    status_carro = models.CharField(max_length=40)
    valor_venda = models.FloatField()
    create = models.DateField(auto_now_add=True)



