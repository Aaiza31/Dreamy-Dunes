from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.TextField()
    image=models.ImageField(upload_to='blogs_images/')
    category = models.TextField(blank=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) #time added automatically on blogs
    
    def __str__(self):
        return self.title