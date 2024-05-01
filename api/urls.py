from django.urls import path
from api.views.category import CategoryCreateView, CategoryListView, CategoryDetailView, CategoryDeleteView
from api.views.item import ItemCreateView, ItemListView, ItemDetailView, ItemDeleteView, ItemStockUpdateView
from api.views.tag import TagCreateView, TagListView, TagDetailView, TagDeleteView


urlpatterns = [

    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('tag/create/', TagCreateView.as_view(), name='tag_create'),
    path('item/create/', ItemCreateView.as_view(), name='item_create'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('tag/', TagListView.as_view(), name='tag_list'),
    path('item/', ItemListView.as_view(), name='item_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('tag/delete/<int:pk>/', TagDeleteView.as_view(), name='tag_delete'),
    path('item/delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
    path('item/update/<int:pk>/', ItemStockUpdateView.as_view(), name='item_stock_update'),

]
