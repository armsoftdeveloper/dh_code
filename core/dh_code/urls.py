from django.urls import path
from .views import *

urlpatterns = [
    # RU URLS
    path('api/dhcode/basic/ru/' , BasicAPIViewRU.as_view()),
    path('api/dhcode/etaps/ru/' , EtapsAPIViewRU.as_view()),
    path('api/dhcode/services/ru/' , ServicesAPIViewRU.as_view()),
    path('api/dhcode/advantages/ru/' , AdvantagesAPIViewRU.as_view()),
    path('api/dhcode/reviews/ru/' , ReviewsAPIViewRU.as_view()),
    # EN URLS
    path('api/dhcode/basic/en/' , BasicAPIViewEN.as_view()),
    path('api/dhcode/etaps/en/' , EtapsAPIViewEN.as_view()),
    path('api/dhcode/services/en/' , ServicesAPIViewEN.as_view()),
    path('api/dhcode/advantages/en/' , AdvantagesAPIViewEN.as_view()),
    path('api/dhcode/reviews/en/' , ReviewsAPIViewEN.as_view()),
    #DEFAULT PATHS FOR ALL LANGUAGES 
    path('api/dhcode/contact/' , ContactAPIView.as_view()),
    path('api/dhcode/portfolio/' , PortfolioAPIView.as_view()),
    path('api/dhcode/messages/' , MessagesAPIView.as_view()),
]
