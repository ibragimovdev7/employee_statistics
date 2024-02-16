import datetime
import random
from orders.models import Order, OrderDetails
from account.models import User
from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        clients = User.objects.filter(is_client=True)
        employees = User.objects.filter(is_staff=True)
        products = Product.objects.all()
        employee = employees
        client = clients
        day = [i for i in range(1,29)]
        month = [j for j in range(1,11)]
        year = [x for x in range(2001,2023)]

        for i in range(1000):

            order = Order.objects.create(
                employee_id=random.choice(employee),
                client_id=random.choice(client),
                date=datetime.date(random.choice(year),random.choice(month),random.choice(day))
            )

            prod = random.choice(products)
            OrderDetails.objects.create(
                order=order,
                product=prod,
                price=prod.price,
                quantity=random.choice([3,1,5,6,9,7,8,2])
            )


        print('Success....................!')