from dataclasses import field, fields
from rest_framework import serializers
from django.forms import ModelForm
from .models import Receita

class PostForm(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'