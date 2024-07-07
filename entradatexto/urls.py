from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('search/', views.searchView, name='search'),
    path('user_profile/<int:user>/', views.user_profile, name='user_profile'),
    path('home/', views.home, name='home'),
    path('crearcomentario/', views.crearcomentario, name='crearcomentario'),
    path('listacomentarios/', views.listacomentarios, name='listacomentarios'),
    path('commentupdate/<int:id>/', views.commentupdate, name='commentupdate'),
    path('deletecomment/<int:id>/', views.deletecomment, name='deletecomment'),
    path('configuraciones/', views.configuraciones, name='configuraciones'),
]













'''router = routers.DefaultRouter()
router.register('api/users', userViewSet)

urlpatterns = [
    path('', include(router.urls)),
]'''