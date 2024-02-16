# employee_statistics
## statistic
1. clone repo
2. create virtualenviroment
3. pip install -r  requirements.txt 
4. create database postgresql db_name='demo_db', db_user='demo_user', password='12345'
5. python manage.py migrate
6. python manage.py createsuperuser 
7. py manage.py create_employees (create default employees)
8. py manage.py create_clients (create default clients)
9. py manage.py create_products (create default products)
10. py manage.py add (create orders and order_setails)
11. python manage.py runserver
## apis
1. /statistics/employee/{id}/?month=1&year=2023
2. /employee/statistics/?month=1&year=2023
3. /statistics/client/{id}?month=1&year=2023
   #####
4. order/list (for all orders)
5. order/details (for all order details)


 
