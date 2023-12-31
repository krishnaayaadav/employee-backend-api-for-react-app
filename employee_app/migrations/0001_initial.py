# Generated by Django 4.2.2 on 2023-07-07 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('job_role', models.CharField(max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('avtar', models.ImageField(upload_to='Employees/Images')),
                ('status', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
