from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import index, generate_sentences, judge_entailment

router = DefaultRouter()

urlpatterns = [
    path('', index, name='index'),
    path('generate_sentences/', generate_sentences, name='generate_sentences'),
    path('judge/', judge_entailment, name='judge_entailment'),
]
