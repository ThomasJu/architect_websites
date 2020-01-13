# Generated by Django 3.0.2 on 2020-01-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of Employee', max_length=100)),
                ('title', models.CharField(help_text='Enter the title of Employee', max_length=100)),
                ('experience', models.TextField(help_text='Enter the working experience of Employee', max_length=1000)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
