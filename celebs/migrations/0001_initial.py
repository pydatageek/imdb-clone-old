# Generated by Django 2.2.6 on 2019-10-03 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100)),
                ('nick_name', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=100, null=True, verbose_name='Birth place')),
                ('bio', models.TextField(blank=True, null=True)),
                ('source_content', models.URLField(blank=True, default='', null=True)),
                ('source_image', models.CharField(blank=True, max_length=250, null=True)),
                ('trailer', models.URLField(blank=True, default='', help_text='trailer url (for now, ONLY youtube videos)', null=True)),
            ],
            options={
                'verbose_name_plural': 'Celebrities',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Duties',
            },
        ),
    ]
