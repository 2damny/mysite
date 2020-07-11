from django.urls import path
from . import views

#클라이언트가 형식별로 요청하면 형식에 맞는 view호출
#'<int:question_id>/' url 패턴

app_name = 'polls'
urlpatterns = [
    # ex; /polls/
    path('', views.index, name='index'),

    # ex; /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # ex; /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # ex; /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
