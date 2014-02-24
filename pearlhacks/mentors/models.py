from django.db import models

# Create your models here.
class Mentor(models.Model):
    nameFirst = models.CharField(max_length=20)
    nameLast = models.CharField(max_length=20)
    company = models.CharField(max_length=30)
    companyUrl = models.CharField(max_length=50)
    twitter = models.CharField(unique=True, max_length=50)
    linkedIn = models.CharField(unique=True, max_length=50)
    website = models.CharField(max_length=50)
    linkOther = models.CharField(max_length=50)
    # techExp = models.CharField(max_length=1000)
    language = models.CharField(max_length=20)
    languageUrl = models.CharField(max_length=50)
    almaMater = models.CharField(max_length=50)
    photoUrl = models.CharField(unique=True, max_length=50)
    color = models.CharField(max_length=20)
    hexCode = models.CharField(max_length=7)
    allWomen = models.CharField(unique=True, max_length=500)
    afraid = models.CharField(unique=True, max_length=500)
    proud = models.CharField(unique=True, max_length=500)
    about = models.CharField(unique=True, max_length=500)
    # hobbies = models.CharField(max_length=1000)

    # pub_date = models.DateTimeField('date published')

    class Meta(object):
		ordering = ('nameFirst', 'nameLast', 'company')