from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # re_path를 사용하여 정규표현식으로 구현해보기
    # re_path('^$', views.index, name='index'),
    # re_path('^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # re_path('^(?P<question_id>\d+)/result/$', views.results, name='results'),
    # re_path('^(?P<question_id>\d+)/vote/$', views.vote, name='vote')
]