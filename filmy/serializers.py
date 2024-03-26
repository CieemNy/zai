from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "is_superuser", "email", "is_staff", "is_active"]


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwania', 'gatunek', 'rezyser', 'filmy']


class OcenaSerializer(serializers.ModelSerializer):
    class Meta: model = Ocena

    fields = ['recenzja', 'gwiazdki', 'film']


class AktorSerializer(serializers.ModelSerializer):
    filmy = serializers.SlugRelatedField(slug_field='tytul', queryset=Film.objects.all(), many=True)

    class Meta:
        model = Aktor

    fields = ['id', 'imie', 'nazwisko', 'filmy']


class FilmSerializer(serializers.ModelSerializer):
    extrainfo = serializers.StringRelatedField()
    ocena_set = OcenaSerializer(read_only=True, many=True)
    aktor_set = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Film
        fields = [
            'id',
            'tytul',
            'opis',
            'producent',
            'rezyser',
            'rok',
            'ocena'
        ]

    def create(self, validated_data):
        return Film.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tytul = validated_data.get('tytul', instance.tytul)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.producent = validated_data.get('producent', instance.producent)
        instance.rezyser = validated_data.get('rezyser', instance.rezyser)
        instance.rok = validated_data.get('rok', instance.rok)
        instance.ocena = validated_data.get('ocena', instance.ocena)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()