# EmployeeProject
This project Backend was generated with Django RestFramework.

Full documentation for the Django RestFramework is available at https://www.django-rest-framework.org/.

# Requirements
Python 3.7 <br />
Django 3.1 <br />
Django RestFramework 3.11.1

# Installation
After Installing Python you can install other requirements using pip...

pip install django   <br />
pip install djangorestframework

# Running Server
That's it, we're done!

Run project by navigating to the project directory and use **python manage.py runserver**

You can now open the API in your browser at http://127.0.0.1:8000/ which is by default hosted by Django.

# API 
1. GET ALL Employee: <br />
		API: http://127.0.0.1:8000/api/employee/  <br />
		Request: GET
		
2. GET Employee by ID:  <br />
		API: http://127.0.0.1:8000/api/employee/?id=1   <br />
		Request: GET
		
3. ADD Employee:  <br />
		API: http://127.0.0.1:8000/api/employee/   <br />
		Request: POST  <br />
		Payload: {"name": "Rahul", "address": "Pune"}
