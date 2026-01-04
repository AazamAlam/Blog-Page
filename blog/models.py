from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#other arguments possible such as auto_now or auto_now_add but with caveats (can't change/auto update)
#timzone.now() is a function, but we do not want to execute it right away
#one to many relationship set up with ForeignKey, first arg is the table it is related
# Second argument tells what happens when author deleted, cascade: delete posts when author is deleted

#Migrations -> makemigrations, migrate commands, sqlmigrate blog 0001 shows the sql code about to run (english like)
# blog 0001 comes from the migrations folder, indicated during makemigrations
# very easy to make changes through migrations of the databasesd