from django.urls import path
from .views import BlogApi

urlpatterns = [
    path('blog-data/', BlogApi.as_view() , name='get-blog-data')
]
