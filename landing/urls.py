from django.urls import path
from . import views  #상대경로를 활용한 import 가능

app_name = 'landing'
urlpatterns = [
    path('', views.index, name='index'),
    path('inputtext',views.inputtext, name="inputtext"),
    path('<str:textarea>', views.landing, name="landing")
    # path('<int:post_id>/', views.detail, name='detail'),
    # path('new', views.new, name='new'),
    # path('create/', views.create, name='create'),
    # path('<int:post_id>/edit/', views.edit, name='edit'),
    # path('<int:post_id>/update/', views.update, name='update'),
    # path('<int:post_id>/delete/', views.delete, name='delete'),
    # path('<int:post_id>/like/', views.like, name='like'),
    # path('<int:post_id>/comments', views.comments),
]