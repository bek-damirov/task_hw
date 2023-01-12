from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .serializers import CategorySerializer, QuestionSerializer, QuestionAnswerSerializer
from .models import Category, QuestionAnswer


class QuestionPagination(PageNumberPagination):
    page_size = 2


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Api для добавления, редактирования, удаления категорий,
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionView(generics.ListCreateAPIView):
    """
       API для просмотра и добавления вопросов с ответами
       """

    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['importance', ]
    pagination_class = QuestionPagination



class QuestionAnswerView(generics.RetrieveUpdateDestroyAPIView):
    """
      API для детального просмотра, редактирования, удаления
      """

    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer











