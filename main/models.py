from django.db import models
from string import ascii_letters , digits
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

group_level = {
    'STARTER': 'STARTER',
    'BEGINNER':'BEGINNER',
    'INTERMEDIATE':'INTERMEDIATE',
    'PREINTERMEDIATE':'PREINTERMEDIATE',
    'UPPERINTERMEDIATE':'UPPERINTERMEDIATE',
    'ADVANCED':'ADVANCED',  
    'IELTS':'IELTS'

}

group_status = {
    'INPROGRESS':'INPROGGRESS',
    'WAITING':'WAITING',
    'CANCELED':'CANCELED',
    'COMPLETED':'COMPLATED'
}

teacher_qualification = {
    'IELTS 7':'IELTS 7',
    'IELTS 7,5':'IELTS 7,5',
    'IELTS 8':'IELTS 8',
    'IELTS 8,5':'IELTS 8,5',
    'IELTS 9':'IELTS 9'
}

class Group(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    level = models.CharField(choices=group_level, max_length=200)
    status = models.CharField(max_length=200, choices=group_status)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    uuid = ShortUUIDField(
        length = 11,
        max_length= 20,
        prefix = 'group_',
        alphabet = ascii_letters + digits + '-,*/',
        primary_key=True
    )

    class Meta:
        ordering = ['title']


    def __str__(self) -> str:
        return f'{self.title}'
    

class Student(models.Model):
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=150)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField()
    group = models.ManyToManyField(Group, related_name='students')
    uuid = ShortUUIDField(
        length = 11,
        max_length= 20,
        prefix = 'student_',
        alphabet = ascii_letters + digits + '-,*/',
        primary_key=True
    )

    class Meta:
        ordering = ['fullname']

    def __str__(self) -> str:
        return f'{self.fullname} - {self.group}'
    

class Teacher(models.Model):
    fullname = models.CharField(max_length=180)
    phone = models.CharField(max_length=200)
    level = models.CharField(choices=teacher_qualification, max_length=200)
    birth_date = models.DateField()
    hire_time = models.DateTimeField(auto_now_add=True)
    group = models.ManyToManyField(Group, related_name='teachers')
    uuid = ShortUUIDField(
        length = 11,
        max_length= 20,
        prefix = 'student_',
        alphabet = ascii_letters + digits,
        primary_key=True
    )

    class Meta:
        ordering = ['birth_date']

    def __str__(self) -> str:
        return f'{self.fullname} - {self.group}'

