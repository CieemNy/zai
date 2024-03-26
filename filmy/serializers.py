from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    filmy = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())
    einfo = serializers.PrimaryKeyRelatedField(queryset=ExtraInfo.objects.all())
    oceny = serializers.PrimaryKeyRelatedField(many=True, queryset=Ocena.objects.all())
    aktorzy = serializers.PrimaryKeyRelatedField(many=True, queryset=Aktor.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'filmy']


class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "is_superuser", "email", "is_staff", "is_active"]
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        password = validated_data.get('password', None)
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwania', 'gatunek', 'filmy']


class OcenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocena
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
        # fields = [
        #     'id',
        #     'tytul',
        #     'opis',
        #     'producent',
        #     'rezyser',
        #     'rok',
        #     'extrainfo',
        #     'ocena_set',
        #     'aktor_set',
        # ]
        fields = '__all__'

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