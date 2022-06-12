from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name=''),
    path('user/', views.userPage, name="user-page"),
    path('customer_complaints/<str:types>', views.cust_complaints, name = 'customer_complaints'),
    path('section_complaints/<str:types>', views.sect_complaints, name = 'section_complaints'),
    path('customer_transformer_complaints/', views.trans_cust_complaints, name = 'trans_customer_complaints'),
    path('section_transformer_complaints/', views.trans_sect_complaints, name = 'trans_section_complaints'),
    path('assign_jobs/', views.assign_jobs, name = 'assign_jobs'),
    path('rectify_jobs/', views.rectify_jobs, name = 'rectify_jobs'),
    path('cancel_jobs/', views.cancel_jobs, name = 'cancel_jobs'),
    path('transformer_maintenance/<str:types>', views.transformer_maintenance, name = 'trans_maintenance'),
    path('reports/', views.reports, name = 'reports'),
    path('create_customer_complaint/<str:types>', views.create_cust_cmp, name = 'create_cust_complaint'),
    path('assign_complaint/<str:pk>/<str:trans>', views.assign_complaint, name="assign_complaint"),
    path('delete_complaint/<str:pk>/<str:trans>', views.delete_complaint, name="delete_complaint"),
]   