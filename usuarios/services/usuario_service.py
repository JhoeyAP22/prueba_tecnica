from usuarios.models.usuario_model import Usuario
from usuarios.exceptions.custom_exceptions import NotFoundError

# -------------------
# MEMORIA
# -------------------
usuarios_memoria = []

def listar_memoria():
    return usuarios_memoria

def agregar_memoria(data):
    usuarios_memoria.append(data)
    return data


# -------------------
# BASE DE DATOS
# -------------------
def listar():
    return Usuario.objects.all()

def obtener(id):
    usuario = Usuario.objects.filter(id=id).first()
    if not usuario:
        raise NotFoundError("Usuario no encontrado")
    return usuario

def crear(data):
    return Usuario.objects.create(**data)

def actualizar(id, data):
    usuario = obtener(id)

    usuario.nombre = data.get("nombre")
    usuario.email = data.get("email")
    usuario.save()

    return usuario

def eliminar(id):
    usuario = obtener(id)
    usuario.delete()