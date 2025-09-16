from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializer import BlogSerializer
# Create your views here.

class BlogApi(APIView):
    def get(self,request):
        blog_data=Blog.objects.all().order_by('-created_at')#latest pehly show hn blog to '-' ye sign means descending order
        category=request.query_params.get('category')
        id=request.query_params.get('id')
        if category:
            blog_data=blog_data.filter(category__icontains=category)
        if id :
            blog_data=blog_data.filter(id=id)
        serializer = BlogSerializer(blog_data , many=True , context={'request' : request})#context isliye lgaya he ta k image k path k saath URL b mile or image open b ho
        return Response(serializer.data)