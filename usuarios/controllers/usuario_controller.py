from usuarios.serializers.usuario_serializer import UsuarioSerializer
from usuarios.services import usuario_service
from usuarios.utils.responses import success, error
from usuarios.exceptions.custom_exceptions import NotFoundError

# -------------------
# SALUDO
# -------------------
def saludo():
    return success(message="Servidor Django funcionando 🚀")


# -------------------
# MEMORIA
# -------------------
def listar_memoria():
    return success(usuario_service.listar_memoria())


def agregar_memoria(data):
    if not data:
        return error("Datos vacíos", 400)

    return success(usuario_service.agregar_memoria(data), "Agregado")


# -------------------
# CRUD DB
# -------------------
def listar():
    try:
        usuarios = usuario_service.listar()
        data = UsuarioSerializer(usuarios, many=True).data
        return success(data)

    except Exception as e:
        return error(str(e), 500)


def obtener(id):
    try:
        usuario = usuario_service.obtener(id)
        data = UsuarioSerializer(usuario).data
        return success(data)

    except NotFoundError as e:
        return error(str(e), 404)


def crear(data):
    try:
        serializer = UsuarioSerializer(data=data)

        if not serializer.is_valid():
            return error(serializer.errors, 400)

        usuario = usuario_service.crear(serializer.validated_data)
        return success(UsuarioSerializer(usuario).data, "Creado", 201)

    except Exception as e:
        return error(str(e), 500)


def actualizar(id, data):
    try:
        serializer = UsuarioSerializer(data=data)

        if not serializer.is_valid():
            return error(serializer.errors, 400)

        usuario = usuario_service.actualizar(id, serializer.validated_data)
        return success(UsuarioSerializer(usuario).data)

    except NotFoundError as e:
        return error(str(e), 404)

    except Exception as e:
        return error(str(e), 500)


def eliminar(id):
    try:
        usuario_service.eliminar(id)
        return success(message="Eliminado")

    except NotFoundError as e:
        return error(str(e), 404)

    except Exception as e:
        return error(str(e), 500)