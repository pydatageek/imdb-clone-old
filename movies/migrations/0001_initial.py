# Generated by Django 2.2.5 on 2019-09-30 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('celebs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=55, unique=True)),
                ('content', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('title', models.CharField(max_length=75)),
                ('release_year', models.CharField(max_length=4)),
                ('slug', models.SlugField(max_length=85)),
                ('duration', models.SmallIntegerField(blank=True, default=0, help_text='in minutes', null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('trailer', models.URLField(blank=True, default='', help_text='trailer url (for now, ONLY youtube videos)', null=True)),
                ('source_content', models.URLField(blank=True, default='', null=True)),
                ('source_image', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='name in movie')),
                ('cast', models.ForeignKey(limit_choices_to=models.Q(duties__name__icontains='Cast'), on_delete=django.db.models.deletion.CASCADE, related_name='moviecast', to='celebs.Celebrity')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviecast', to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='casts',
            field=models.ManyToManyField(through='movies.MovieCast', to='celebs.Celebrity'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(limit_choices_to=models.Q(duties__name__icontains='Director'), related_name='directors', to='celebs.Celebrity'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='writers',
            field=models.ManyToManyField(limit_choices_to=models.Q(duties__name__icontains='Writer'), related_name='writers', to='celebs.Celebrity'),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('title', 'release_year')},
        ),
    ]
