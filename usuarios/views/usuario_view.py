from rest_framework.decorators import api_view
from usuarios.controllers import usuario_controller


# -------------------
# SALUDO
# -------------------
@api_view(['GET'])
def saludo(request):
    return usuario_controller.saludo()


# -------------------
# MEMORIA
# -------------------
@api_view(['GET'])
def usuarios_memoria(request):
    return usuario_controller.listar_memoria()


@api_view(['POST'])
def usuarios_memoria_add(request):
    return usuario_controller.agregar_memoria(request.data)


# -------------------
# CRUD DB
# -------------------
@api_view(['GET'])
def usuarios_list(request):
    return usuario_controller.listar()


@api_view(['GET'])
def usuarios_get(request, id):
    return usuario_controller.obtener(id)


@api_view(['POST'])
def usuarios_create(request):
    return usuario_controller.crear(request.data)


@api_view(['PUT'])
def usuarios_update(request, id):
    return usuario_controller.actualizar(id, request.data)


@api_view(['DELETE'])
def usuarios_delete(request, id):
    return usuario_controller.eliminar(id)