from rest_framework import generics
from api.models.item import Item
from api.serializers import ItemSerializer, ItemListSerializer, ItemStockUpdateSerializer
from api.views.pagination import CustomPagination


class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    pagination_class = CustomPagination


class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'


class ItemStockUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemStockUpdateSerializer
    lookup_field = 'pk'
