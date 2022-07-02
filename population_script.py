import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','leveltwo.settings')
import django
django.setup()
from protwo.models import User
from faker import Faker
fakegen = Faker()
def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        f_name = fake_name[0]
        l_name = fake_name[1]
        email = fakegen.email()

        user = User.objects.get_or_create(first_name=f_name, last_name=l_name, email=email)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populate complete')