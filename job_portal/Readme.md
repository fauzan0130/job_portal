Job Portal Web App using Django (Python Web Framework)

Functionalities of the project:
1. User Authentication.
2. Job Listing based on Categories, Location.
3. User can create a job opening as well as apply for jobs.
4. Apply job form also takes resume of the user so that the recruiter can have a look on the resume of the applicant.
5. Job details page.
6. User Profile page where user can see their applied jobs and status.(application status can be controller from admin panel http://127.0.0.1:8000/admin)

Steps to run the project:
1. Go to project folder and open cmd (/job_portal/)
2. Various files and be seen in job_portal folder one of the most important is manage.py which is used with almost all commands to interact with the project.
3. Once you open cmd run "pip install Django" and "pip install Pillow"
4. Run "python manage.py" to run the project on local server that is http://127.0.0.1:8000/
5. Django by default uses port 8000 to run the project.
6. Go to http://127.0.0.1:8000/ you can see the project running.
7. As the project is set in development server debug is set to true to enable good debugging when an error occurs.
8. Admin panel can be found at http://127.0.0.1:8000/admin/

Other important points:
1. Username and password for admin is:
    username: admin 
    password: 1234
2. To create a superuser that is another admin:
    python manage.py createsuperuser

3. If the files are changes which changes the info in database file we need to run:
    python manage.py migrate
    python manage.py makemigrations
    python manage.py migrate.