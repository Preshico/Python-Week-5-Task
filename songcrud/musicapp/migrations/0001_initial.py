from dataclasses import field
from tabnanny import verbose
from tkinter import CASCADE
from unicodedata import name

import django


initial = True

dependencies = [
]

operations = [
    migrations.CreateModel(
        name="Artiste",
        field=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('first_name',models.CharhField(max_length=255)),
            ('age', models.InteerField()),
        ],
    ),
    migrations.CreateModel(
          name="Song",
        field=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('title',models.CharhField(max_length=255)),
            ('date_released', models.DateField()),
            ('likes', models.InteerField()),
            ('artiste_id', models.ForeignKey(on_delete-django.db.models.deletion.CASCADE, to-'musicapp.artiste')),
            
        ],
    ),
       migrations.CreateModel(
          name="Lyric",
        field=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('content', models.TextField()),
            ('song_id', models.ForeignKey(on_delete-django.db.models.deletion.CASCADE, to-'musicapp.artiste')),
            
        ],
    ),
]