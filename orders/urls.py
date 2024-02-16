from django.urls import path
from .views import StatisticEmlpoyeeWithIdView, StatisticEmployeeListView, StatisticaCLientsView

urlpatterns = [
    path('statistics/employee/<int:id>', StatisticEmlpoyeeWithIdView.as_view()),
    path('employee/statistics/',StatisticEmployeeListView.as_view()),
    path('statistics/client/<int:id>',StatisticaCLientsView.as_view())
]
