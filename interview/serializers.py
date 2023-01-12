from rest_framework import serializers
from .models import Category, QuestionAnswer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'
        extra_kwargs = {
            'answer': {'write_only': True}
        }


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'
        read_only_fields = ['category']



