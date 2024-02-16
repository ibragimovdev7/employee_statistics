from django.db import models


class Order(models.Model):
    employee_id = models.ForeignKey('account.User', related_name='orders', on_delete=models.CASCADE)
    client_id = models.ForeignKey('account.User', related_name='client_order', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.client_id.__str__()} - order:{self.id}'

    def item_count(self):
        return self.details.count()

    def total_price(self):
        return sum([i.total_price() for i in self.details.all()])


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'order:{self.order.id} - {self.product}, quantity:{self.quantity}'

