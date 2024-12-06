import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
faker=Faker()
from random import *
def phonenumber():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        frollno=faker.random_int(min=1,max=9999)
        fname=faker.name()
        fdob=faker.date()
        fmarks=faker.random_int(min=1,max=100)
        fphonenumber=phonenumber()
        faddress=faker.address()
        femail = faker.email()
        Student.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,
                                      phonenumber=fphonenumber,address=faddress,email=femail)
n=int(input("Enter number of Records"))
populate(n)
print(f'{n} Records Inserted Successfully........!')