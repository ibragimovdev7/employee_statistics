from django.db import connection
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response

from .models import Order, OrderDetails
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from helpers import pagination
from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework.views import APIView


class OrderViewSet(ModelViewSet):
    pagination_class = pagination.CustomPagination
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()


class OrderDetailViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = OrderDetailSerializer
    pagination_class = pagination.CustomPagination
    queryset = OrderDetails.objects.all()


class StatisticEmlpoyeeWithIdView(APIView):

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id", False)
        year = request.query_params.get("year", False)
        month = request.query_params.get("month", False)
        with connection.cursor() as cursor:
            try:
                if id and year and month:
                    next_month = int(month) + 1 if int(month) < 12 else 1
                    sql1 = f'''
                        SELECT account_user.id AS id_employee,account_user.first_name, account_user.last_name, 
                        COUNT(account_user.id) AS clients_count,
                        SUM(orders_orderdetails.quantity) AS  quantity,
                        SUM(orders_orderdetails.price * orders_orderdetails.quantity) AS total_price
                        FROM orders_order
                        JOIN orders_orderdetails ON orders_order.id = orders_orderdetails.order_id
                        JOIN account_user ON orders_order.employee_id_id=account_user.id 
                        JOIN products_product ON orders_orderdetails.product_id=products_product.id
                        WHERE orders_order.date >=  date '{year}-{month}-01' AND orders_order.date < date '{year}-{next_month}-01' 
                        AND account_user.id='{id}' AND account_user.is_staff='true' AND account_user.is_active='true' AND account_user.is_superuser='false'
                        GROUP BY account_user.id
        
                    '''
                    cursor.execute(sql1)
                    columns = [col[0] for col in cursor.description]
                    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                if id and not year and not month:
                    sql2 = f'''
                                        SELECT account_user.id AS id_employee,account_user.first_name, account_user.last_name, 
                                        COUNT(account_user.id) AS clients_count,
                                        SUM(orders_orderdetails.quantity) AS  quantity,
                                        SUM(orders_orderdetails.price * orders_orderdetails.quantity) AS total_price
                                        FROM orders_order
                                        JOIN orders_orderdetails ON orders_order.id = orders_orderdetails.order_id
                                        JOIN account_user ON orders_order.employee_id_id=account_user.id 
                                        JOIN products_product ON orders_orderdetails.product_id=products_product.id
                                        WHERE  account_user.id='{id}' AND account_user.is_staff='true'AND account_user.is_superuser='false'
                                        GROUP BY account_user.id
                                    '''
                    cursor.execute(sql2)
                    columns = [col[0] for col in cursor.description]
                    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            except Exception as e:
                return Response({'error': str(e)})

        return JsonResponse(data, safe=False)


class StatisticEmployeeListView(APIView):
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", False)
        month = request.query_params.get("month", False)
        with connection.cursor() as cursor:
            try:
                if month and year:
                    next_month = int(month) + 1 if int(month) < 12 else 1
                    sql1 = f'''
                            SELECT account_user.id AS id_employee,account_user.first_name, account_user.last_name, 
                            COUNT(account_user.id) AS clients_count,
                            SUM(orders_orderdetails.quantity) AS  quantity,
                            SUM(orders_orderdetails.price * orders_orderdetails.quantity) AS total_price
                            FROM orders_order
                            JOIN orders_orderdetails ON orders_order.id = orders_orderdetails.order_id
                            JOIN account_user ON orders_order.employee_id_id=account_user.id 
                            JOIN products_product ON orders_orderdetails.product_id=products_product.id
                            WHERE orders_order.date >=  date '{year}-{month}-01' AND orders_order.date < date '{year}-{next_month}-01' AND
                            account_user.is_staff='true' AND account_user.is_active='true' AND account_user.is_superuser='false'
                            GROUP BY account_user.id

                    '''
                    cursor.execute(sql1)
                    columns = [col[0] for col in cursor.description]
                    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                else:
                    sql2 = f'''
                                        SELECT account_user.id AS id_employee,account_user.first_name, account_user.last_name, 
                                        COUNT(account_user.id) AS clients_count,
                                        SUM(orders_orderdetails.quantity) AS  quantity,
                                        SUM(orders_orderdetails.price * orders_orderdetails.quantity) AS total_price
                                        FROM orders_order
                                        JOIN orders_orderdetails ON orders_order.id = orders_orderdetails.order_id
                                        JOIN account_user ON orders_order.employee_id_id=account_user.id 
                                        JOIN products_product ON orders_orderdetails.product_id=products_product.id
                                        WHERE account_user.is_staff='true' AND account_user.is_active='true' AND account_user.is_superuser='false'
                                        GROUP BY account_user.id
                                    '''
                    cursor.execute(sql2)
                    columns = [col[0] for col in cursor.description]
                    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            except Exception as e:
                return Response({'error': str(e)})

        return JsonResponse(data, safe=False)


class StatisticaCLientsView(APIView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id", False)
        year = request.query_params.get("year", False)
        month = request.query_params.get("month", False)
        with connection.cursor() as cursor:
            try:
                if id and month and year:
                    next_month = int(month) + 1 if int(month) < 12 else 1
                    sql1 = f'''
                                SELECT
                                    account_user.id AS id_client,
                                    account_user.first_name,
                                    account_user.last_name,
	                                SUM(orders_orderdetails.quantity) AS quantity,
                                    SUM(orders_orderdetails.quantity * orders_orderdetails.price) AS total_price
                                FROM
                                    orders_order
                                JOIN
                                    orders_orderdetails ON orders_order.id = orders_orderdetails.order_id
                                JOIN
                                    account_user ON orders_order.client_id_id = account_user.id 
                                JOIN
                                    products_product ON orders_orderdetails.product_id = products_product.id
                                WHERE
                                    account_user.is_client = 'true'
                                    AND account_user.is_active = 'true'
                                    AND account_user.is_superuser = 'false'
                                    AND account_user.id = '6'
                                    AND orders_order.date >=  date '{year}-{month}-01' AND orders_order.date < date '{year}-{next_month}-01'
                                Group By account_user.id


                            '''
                    cursor.execute(sql1)
                    columns = [col[0] for col in cursor.description]
                    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                if id and not month and not year:
                    sql2 = f'''
                                SELECT
                                    account_user.id AS id_client,
                                    account_user.first_name,
                                    account_user.last_name,
	                                SUM(orders_orderdetails.quantity) AS quantity,
                                    SUM(orders_orderdetails.quantity * orders_orderdetails.price) AS total_price
                                FROM
                                    orders_order
                                JOIN
                                    orders_orderdetails ON orders_order.id = orders_orderdetails.order_id
                                JOIN
                                    account_user ON orders_order.client_id_id = account_user.id 
                                JOIN
                                    products_product ON orders_orderdetails.product_id = products_product.id
                                WHERE
                                    account_user.is_client = 'true'
                                    AND account_user.is_active = 'true'
                                    AND account_user.is_superuser = 'false'
                                    AND account_user.id = '{id}'
                                GROUP BY account_user.id
                                            '''
                    cursor.execute(sql2)
                    columns = [col[0] for col in cursor.description]
                    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            except Exception as e:
                return Response({'error': str(e)})

        return JsonResponse(data, safe=False)
