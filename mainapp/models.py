from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver

from unidecode import unidecode

# Create your models here.
class MakaleTags(models.Model):
    makale_tag_isim = models.CharField(('Makale Tag'), max_length=100)

    def __str__(self):
        return self.makale_tag_isim

    class Meta:
        verbose_name = "Makale Etiketi"
        verbose_name_plural = "Makale Etiketleri"


class Makaleler(models.Model):
    makale_baslik = models.CharField(('Makale Başlığı'), max_length=150)
    makale_yayintarihi = models.DateField(('Makale Yayın Tarihi'))
    makale_mesaj = RichTextField()
    makale_slug = models.SlugField(unique=True)

    KATEGORILER = (
        ('ticarethukuku', 'Ticaret Hukuku'),
        ('tazminathukuku', 'Tazminat Hukuku'),
        ('sozlesmelerhukuku', 'Sözleşmeler Hukuku'),
        ('mirashukuku', 'Miras Hukuku'),
        ('ishukuku', 'İş Hukuku'),
        ('icraiflashukuku', 'İcra-İflas Hukuku'),
        ('gayrimenkulhukuku', 'Gayrimenkul Hukuku'),
        ('cezahukuku', 'Ceza Hukuku'),
        ('ailehukuku', 'Aile Hukuku'),
    )

    makale_kategori = models.CharField(('Makale Kategorisi'), max_length=50, choices=KATEGORILER)


    makale_meta_description = models.CharField(('Makale Meta Açıklaması(SEO İÇİN)'), max_length=350)

    tag = models.ManyToManyField(MakaleTags)

    def __str__(self):
        return self.makale_baslik

    def save(self, *args, **kwargs):

        self.makale_slug = slugify(unidecode(self.makale_baslik))
        super(Makaleler, self).save(*args, **kwargs)

    class Meta:
        ordering= ('-makale_yayintarihi',)
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"

    class Uzmanliklar(models.Model):
        uzmanlik_baslik = models.CharField(('Uzmanlık Alanı Başlığı'), max_length=100)
        uzmanlik_mesaj = RichTextField()
        uzmanlik_slug = models.SlugField(unique=True)

        uzmanlik_unique_name = models.CharField(('Uzmanlık Tekil Adı'))

        def save(self, *args, **kwargs):
            self.makale_slug = slugify(unidecode(self.uzmanlik_baslik))
            super(Uzmanliklar, self).save(*args, **kwargs)
