from rest_framework import generics

from mainapp.serializers import MakaleSerializer, UzmanlikSerializer, ContactSerializer
from mainapp.models import Makaleler, Uzmanliklar, ContactModel
from mainapp.paginations import YayinlarPagePagination, YayinlarPageOthersPagination

class getSingleMakale(generics.RetrieveAPIView):
    queryset= Makaleler.objects.all()
    serializer_class= MakaleSerializer

class getSingleUzmanlik(generics.RetrieveAPIView):
    queryset= Uzmanliklar.objects.all()
    serializer_class = UzmanlikSerializer

class UzmanlikList(generics.ListAPIView):
    queryset= Uzmanliklar.objects.all()
    serializer_class= UzmanlikSerializer

class YayinlarMainMakaleList(generics.ListAPIView):
    serializer_class= MakaleSerializer
    pagination_class= YayinlarPagePagination

    def get_queryset(self):
        queryset = Makaleler.objects.all()
        kategori = self.request.query_params.get('kategori', None)
        if kategori is not None:
            queryset = queryset.filter(makale_kategori=kategori)
        return queryset

class YayinlarOthersMakaleList(generics.ListAPIView):
    queryset= Makaleler.objects.all()
    serializer_class= MakaleSerializer
    pagination_class= YayinlarPageOthersPagination

class addContact(generics.CreateAPIView):
    serializer_class= ContactSerializer
