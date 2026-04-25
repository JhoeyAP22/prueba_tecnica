from rest_framework import serializers
from usuarios.models.usuario_model import Usuario

class UsuarioSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(
        error_messages={
            "blank": "El nombre no puede estar vacío",
            "required": "El nombre es obligatorio"
        }
    )

    email = serializers.EmailField(
        error_messages={
            "blank": "El email no puede estar vacío",
            "required": "El email es obligatorio"
        }
    )

    class Meta:
        model = Usuario
        fields = '__all__'