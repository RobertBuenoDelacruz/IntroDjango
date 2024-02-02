from django.views.generic import ListView, DetailView
from .models import Post 

# Create your view here to populate data from database
# This is where the ORM of Django interacts with the database

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post 
    template_name = 'post_detail.html'
