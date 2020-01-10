from django.urls import path
from .views import *
urlpatterns = [
    path('',products_index),
    path('add/',add_form),
    path('update/<int:id>',update_form),
    path('save/',post_add_product),
    path('save/<int:id>',post_update_product),
    path('delete/<int:id>',delete)
]