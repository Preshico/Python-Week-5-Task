from tkinter import CASCADE
from django.db import models
from django.forms import DateField, IntegerField


class Airtiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(_(""))


class Song(models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

 class Lyric(models.Model):
     content = models.TextField()
     song_id = models.ForeignKey(song,on_delete=models.CASCADE)
 