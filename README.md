# job_portal
A Django based web app where user can post jobs, apply for jobs, keep track of their applied job and job status all with proper authentication.

Job Portal Web App using Django (Python Web Framework)

Functionalities of the project:
1. User Authentication.
2. Job Listing based on Categories and Location.
3. The user can create a job opening and apply for jobs.
4. Apply job form also takes the resume of the user so that the recruiter can have a look at the resume of applicant.
5. Job details page.
6. User Profile page where user can see their applied jobs and status. (application status can be controlled from the admin panel http://127.0.0.1:8000/admin)

Steps to run the project:
1. Go to the project folder and open cmd (/job_portal/)
2. Various files can be seen in the job_portal folder one of the most important is manage.py which is used with almost all commands to interact with the project.
3. Once you open cmd run "pip install Django" and "pip install Pillow"
4. Run "python manage.py" to run the project on a local server which is http://127.0.0.1:8000/
5. Django by default uses port 8000 to run the project.
6. Go to http://127.0.0.1:8000/ you can see the project running.
7. As the project is set in the development server debug is set to true to enable good debugging when an error occurs.
8. The Admin panel can be found at http://127.0.0.1:8000/admin/

Other important points:
1. The username and password for admin are:
    username: admin 
    password: 1234
2. To create a superuser that is another admin:
    python manage.py createsuperuser

3. If the files are changes which change the info in the database file we need to run:
    python manage.py migrate
    python manage.py makemigrations
    python manage.py migrate.
