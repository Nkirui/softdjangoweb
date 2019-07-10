from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted_on = models.DateField(db_index=True, auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __unicode__(self):
        return '%s' % self.title

    #def get_absolute_url(self):
        #return ('view_blog_post', None, {'slug': self.slug})


    def posted_on_pretty(self):
            return self.posted_on.strftime('%b %e, %Y')  

    #it will return you the date in this format – Sep 26, 2018, which looks more user friendly 
    

class Comment(models.Model):
    comments = models.CharField(max_length=60, blank=True, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.comments

    class Meta:
        ordering = ['-comment_date']

    def save_comment(self):
        return self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment