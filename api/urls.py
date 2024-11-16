from django.urls import path

from . import views

urlpatterns = [
    path('category/',views.viewcategory),
    path('product/',views.viewproduct),
    path('createproduct/',views.createproduct),
    path('createcategory/',views.createcategory),
    path('delete_product/<int:id>',views.delete_product),
]