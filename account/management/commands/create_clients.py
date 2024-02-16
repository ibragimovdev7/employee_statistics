from account.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        p = ['99876885','887675433','998907765','33234655','998444595']
        f_n = ['Ismoil', 'Ishoq', 'Nizomiddin', 'Alimardon', 'Zuhriddin']
        l_n = ['Inomov', 'Ochilov', 'Baxromov', 'Nuriddinov', 'Abduganiyev']
        for i in range(5):
            User.objects.create(
                phone=p[i],
                password='Qazxsw21`',
                username=f_n[i],
                first_name=f_n[i],
                last_name=l_n[i],
                is_active=True,
                is_client=True
            )

        print('Clients have created Successfully...!')