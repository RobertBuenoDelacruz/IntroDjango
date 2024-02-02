# posts/models.py

from django.db import models

# to store the tectual content of a message in a post 

class Post(models.Model):
    text = models.TextField() # this will be our column

    def __str__(self):
        return self.text[:50]
    # this will display 50 character of text field in the 
    # admin UI, you can store more characters in the database 
    # but in the Admin UI only the first 50 will show up.