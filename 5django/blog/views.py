from django.views.generic import ListView
from .models import Post 

# Create your view here to populate data from database
# This is where the ORM of Django interacts with the database

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
