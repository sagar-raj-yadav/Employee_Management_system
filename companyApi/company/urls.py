from django.urls import path
from .views import home_page,create_company,get_company,update_company,delete_company

#home url
urlpatterns = [
    path('', home_page),
    path('addcompany/',create_company),
    path('getcompany/',get_company),
    path('updatecompany/',update_company),
    path('deletecompany/',delete_company),
]



