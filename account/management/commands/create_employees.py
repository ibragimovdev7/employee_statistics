from account.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        p = ['998768853','88767543','998907766','33234656','998444599']
        f_n = ['Abdulla', 'Bobur', 'Burxon', 'Nuriddin', 'Salohiddin']
        l_n = ['Imomov', 'Xofizov', 'Bilolov', 'Choriyev', 'Abdugafforov']
        for i in range(5):
            User.objects.create(
                phone=p[i],
                password='Qazxsw21`',
                username=f_n[i],
                first_name=f_n[i],
                last_name=l_n[i],
                is_active=True,
                is_staff=True
            )

        print('Employees have created Successfully...!')