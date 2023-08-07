from django.urls import path
from . import views
from main.views import index, contacts, product, great_prod

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('product/<int:product_id>/', views.product, name='product'),
    path('great_prod/', great_prod)
]




