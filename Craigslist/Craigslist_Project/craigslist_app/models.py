from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    # In admin site, when a search is created, it will show the string that was searched
    def __str__(self):
        return '{}'.format(self.search)

    # In admin site, the database column is named Searchs by Django but the correct spelling is Searches
    # class Meta makes the spelling correction
    class Meta:
        verbose_name_plural = 'Searches'
