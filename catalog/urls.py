from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ContactTemplateView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')

]
