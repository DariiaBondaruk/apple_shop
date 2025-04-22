from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>', views.single_product, name = 'single_product'),
    path('products', views.index, name = 'products'),
    path('category/<int:category_id>', views.single_category, name = 'single_category'),
    path('categories', views.categories, name='categories'),
]