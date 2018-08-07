from django.db import models

from tuites.managers import TuitesManager


# Create your models here.
class Tuite(models.Model):
    content = models.CharField('Tuite', max_length=280)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tuites')
    date_created = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField('users.User', blank=True) # queryset dos usuário que gostaram do tweet


    objects = TuitesManager()

    @property
    def likes_count(self):
        return self.liked_by.count() 

    def __str__(self):
        return f'{self.author.username}: {self.content}'

    class Meta:
        ordering = ('-date_created', )
# related_name: como eu posso acessar os Tuites a partir do model que é author
