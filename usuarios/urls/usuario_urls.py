from django.urls import path
from usuarios.views import usuario_view

urlpatterns = [
    # -------------------
    # SALUDO
    # -------------------
    path('', usuario_view.saludo),

    # -------------------
    # MEMORIA
    # -------------------
    path('usuarios/', usuario_view.usuarios_memoria),
    path('usuarios/add/', usuario_view.usuarios_memoria_add),

    # -------------------
    # CRUD DB
    # -------------------
    path('db/usuarios/', usuario_view.usuarios_list),
    path('db/usuarios/<int:id>/', usuario_view.usuarios_get),
    path('db/usuarios/create/', usuario_view.usuarios_create),
    path('db/usuarios/update/<int:id>/', usuario_view.usuarios_update),
    path('db/usuarios/delete/<int:id>/', usuario_view.usuarios_delete),
]