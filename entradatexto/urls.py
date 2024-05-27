from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='indice'),
     path('1',views.comentariosview,name='comentariosvista'),
    path('2',views.listacomentarios,name='listacomentarios'),

]











'''router = routers.DefaultRouter()
router.register('api/users', userViewSet)

urlpatterns = [
    path('', include(router.urls)),
]'''