# blog/models.py
from django.db import models

# to store the textual content of a message in a post

class Post(models.Model): # A blog has a title, author, and body
    
    # Title column -> CharField()
    title = models.CharField(max_length=200) 
    # this will be our column in the table 'Blog'

    # Author will be the user to log in and creates/ modifies the blog 
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
        # Whe the user is deleted in auth_user all the blogs in the post
        # table associated with the author will be deleted 
    )

    # Body Column -> TextField()
    body = models.TextField()

    def __str__(self):
        return self.title[:75]
    # this will display 50 character of the text field in the 
    # Admin UI, you can store more characters in the database 
    # but in the Admin UI only the first 50 will show up.