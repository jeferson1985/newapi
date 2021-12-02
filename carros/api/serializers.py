from rest_framework import serializers
from carros import models


class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carros
        fields = ['id_carrro', 'nome_carro', 'modelo_carro', 'ano_modelo', 'motor_carro', 'kilometragem', 'status_carro', 'valor_venda']

