# Generated by Django 4.0.4 on 2022-05-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(max_length=5)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]
