from django.urls import path
from . import views
from main.views import contacts, great_prod, ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('great_prod/', great_prod)
]




