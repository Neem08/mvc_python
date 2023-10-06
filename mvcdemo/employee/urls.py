from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add/',views.addEmp,name='addEmp'),
    path('delete/<int:emp_id>',views.delEmp,name='delEmp'),
    path('update/<int:emp_id>',views.updateEmp,name='updateEmp'),
    path('filter/',views.filter,name="filter"),
]