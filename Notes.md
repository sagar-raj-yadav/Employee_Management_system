# what we do (Employee management system)
i.add company name ,fetch company details
ii.particular company me multiple employess hoga (add employee,fetch employee details)
iii.Ralationship -> one to many(one company can have many employee)

# End points
#Company
i.   GET        /companies/                 get all companies 
ii.  GET        /companies/{id}/            get single company details
iii. PUT        /companies/{id}/            update campany
iv.  DELETE     /companies/{id}/            delete company-id
v.   POST       /companies/                 create new company
vi.  GET        /companies/{id}/employee/    get all employee of company-id

#Employee
i.   GET        /employees/                 get all employees 
ii.  GET        /employees/{id}/            get single employees details
iii. PUT        /employees/{id}/            update employees
iv.  DELETE     /employees/{id}/            delete employees
v.   POST       /employees/                 create new employees

# steps to make API
i.install python ,django , django rest framework (DRF)
ii.make Models
iii.make serializers 
serializers->Data ko objects se JSON format (ya kisi aur format) mein convert karna aur vice versa.
Serialization->object to JSON 
Deserialization->JSON to object
iv.views 
request and response handle karna .
views types:Function-Based Views  and Class-Based Views
v.urls (urls and views ka mapping hoga)

# start project
i.django-admin startproject companyApi
ii.cd companyApi
iii.pip install djangorestframework
iv.python manage.py runserver
v.django-admin startapp newAppCreated (newAppCreated ->yese hum new app bana sakte h)

vi.python manage.py makemigrations
vii.python manage.py migrate
