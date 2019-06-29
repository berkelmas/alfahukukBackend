from rest_framework import serializers
from .models import ContactModel

class MakaleSerializer(serializers.Serializer):
    id= serializers.CharField()
    makale_baslik = serializers.CharField(max_length=150)
    makale_yayintarihi = serializers.DateField()
    makale_mesaj = serializers.CharField()
    makale_kategori = serializers.CharField(source='get_makale_kategori_display')
    makale_kategori_nondisplay = serializers.CharField(source='makale_kategori')
    makale_slug = serializers.SlugField(allow_blank=False)

    makale_meta_description = serializers.CharField(max_length=350)
    tag = serializers.StringRelatedField(many=True)

class UzmanlikSerializer(serializers.Serializer):
    id= serializers.CharField()
    uzmanlik_baslik= serializers.CharField(source='get_uzmanlik_baslik_display')
    uzmanlik_baslik_nondisplay = serializers.CharField(source='uzmanlik_baslik')
    uzmanlik_mesaj= serializers.CharField()

class ContactSerializer(serializers.Serializer):
    contact_isim= serializers.CharField()
    contact_ulasim= serializers.CharField()
    contact_message= serializers.CharField()

    def create(self, validated_data):
        return ContactModel.objects.create(**validated_data)
