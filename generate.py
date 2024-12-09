import os
import random
import django
from string import ascii_letters, digits
from random import choices


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from main.models import Group, Student, Teacher

fake = Faker()



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


Group.objects.all().delete()
Student.objects.all().delete()
Teacher.objects.all().delete()


# Group ma'lumotlarini yaratish
levels = list(group_level.keys())
statuses = list(group_status.keys())
teacher_level = list(teacher_qualification.keys())

for _ in range(40): 
    group = Group.objects.create(
        title=fake.word().capitalize()+ ' group',
        level=fake.random_element(levels),
        status=fake.random_element(statuses),
        description=fake.text(),
        price=round(random.uniform(100, 1000), 2),
        uuid = "group_"+ "".join(choices(ascii_letters+digits, k=12))
    )
    group.save()
groups = Group.objects.all()  # Yaratilgan guruhlarni olish

# Student ma'lumotlarini yaratish

for _ in range(500):  
    student = Student.objects.create(
        fullname=fake.name(),
        phone=fake.phone_number(),
        address=fake.address(),
        birth_date=fake.date_of_birth(minimum_age=18, maximum_age=25),
        uuid = "student_"+ "".join(choices(ascii_letters+digits, k=12))
    )
    student.save()
    student.group.set([fake.random_element(groups)])

# Teacher ma'lumotlarini yaratish
for _ in range(35): 
    teacher = Teacher.objects.create(
        fullname=fake.name(),
        phone=fake.phone_number(),
        birth_date=fake.date_of_birth(minimum_age=25, maximum_age=45),
        level = fake.random_element(teacher_level),
        uuid = "teacher_"+ "".join(choices(ascii_letters+digits, k=12))
    )
    teacher.save()
    teacher.group.set([fake.random_element(groups)])



