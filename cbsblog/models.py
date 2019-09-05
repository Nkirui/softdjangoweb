from django.db import models
# from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField (max_length=200)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def created_on_pretty(self):
            return self.created_on.strftime('%b %e, %Y')

#it will return you the date in this format – Sep 26, 2018, which looks more user friendly
