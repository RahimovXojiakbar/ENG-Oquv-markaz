# Generated by Django 5.1 on 2024-08-31 04:57

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(choices=[('STARTER', 'STARTER'), ('BEGINNER', 'BEGINNER'), ('INTERMEDIATE', 'INTERMEDIATE'), ('PREINTERMEDIATE', 'PREINTERMEDIATE'), ('UPPERINTERMEDIATE', 'UPPERINTERMEDIATE'), ('ADVANCED', 'ADVANCED'), ('IELTS', 'IELTS')], max_length=200)),
                ('status', models.CharField(choices=[('INPROGRESS', 'INPROGGRESS'), ('WAITING', 'WAITING'), ('CANCELED', 'CANCELED'), ('COMPLETED', 'COMPLATED')], max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-,*/', length=11, max_length=20, prefix='group_', primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('fullname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('birth_date', models.DateField()),
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-,*/', length=11, max_length=20, prefix='student_', primary_key=True, serialize=False)),
                ('group', models.ManyToManyField(related_name='students', to='main.group')),
            ],
            options={
                'ordering': ['fullname'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('fullname', models.CharField(max_length=180)),
                ('phone', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('IELTS 7', 'IELTS 7'), ('IELTS 7,5', 'IELTS 7,5'), ('IELTS 8', 'IELTS 8'), ('IELTS 8,5', 'IELTS 8,5'), ('IELTS 9', 'IELTS 9')], max_length=200)),
                ('birth_date', models.DateField()),
                ('hire_time', models.DateTimeField(auto_now_add=True)),
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-,*/', length=11, max_length=20, prefix='student_', primary_key=True, serialize=False)),
                ('group', models.ManyToManyField(related_name='teachers', to='main.group')),
            ],
            options={
                'ordering': ['birth_date'],
            },
        ),
    ]
