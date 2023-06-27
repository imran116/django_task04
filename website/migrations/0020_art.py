# Generated by Django 4.2.1 on 2023-06-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_category_file_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='Arts_image/')),
                ('title', models.CharField(max_length=100)),
                ('timeStamp', models.TimeField(auto_now=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
