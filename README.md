# PLANiT


### Description:
This is my CS50 final project!

PLANiT is a simple todo list webapp, using the Django framework and python language.
The app supports user registration, once registered and logged in a user can create a todo list. Users can add tasks to their todo list as well as edit tasks and mark them as completed. Additionally users can delete unwanted tasks.
PLANiT allows users to set a priority, deadline, and category for tasks. Users can also sort their todo list by deadline and category or both. PLANiT also supports group functionality, users can create groups. Users join groups via the groups url and a unique token. The group admin can control group specific functionallitty  

### Installation and running project:
- clone repo
- download [Python](https://www.python.org/downloads/)
- create virtual environment
- use requirements.txt to intall all needed packages
- create .env file or change related variables 
- cd into project folder
- use python manage.py runserver to start the development server
### Video Demo:  <URL https://youtu.be/NlzJeEerF2s>


#### Project structure:
The project structure follows Django's default file structure, as such some of the files were automatically created by Django.

In the project folder, 'PLANiT', I had to edit settings.py and urls.py to setup the project as instructed in django documentation.
In the app folder, 'todo', you have the rest of the project files. I decided for simplicity to have only one app with all the contents.
- views.py - contains the backend functions for the webapp. I decided to use function based views mostly because I was more comfortable with them at the beginning and didn't want to rewrite parts of the code. 
    - Registering users, login, logout.
    - CRUD functionality for the todo list.
    - Sorting functionality, allows user to sort by deadline, task category or both.
- urls.py - contains the url routes for all the views.
- models.py - contains the task model. I chose to use Django's built-in user model.
    - The task model has fields to store information for the task, I chose to keep it simple only creating fields I though were relevant.
- forms.py - contains the forms created for the project used to create the tasks, as well as inherited forms for user creation and authentication in order to add bootstrap styling.
- static folder - contains a 'todo' subfolder, following Django convention.
    - styles.css - contains my added styling for the project.
- templates - contains a 'todo' subfolder, following Django convention, this folder has all the HTML templates used for the project. layout.html which is the base HTML template for the rest of the templates, all other templates are using the Django template language and regular HTML to create the frontend HTML the user will interface with.
- admin.py - contains the models imported to use in Django's admin panel. I created custom TaskAdmin class responsible for customizing the admin display for the Task model.

#### Future plans:
I have some additional feature ideas that may be implemented in a future date.
- Create friend list and make shareable tasks.
- Create task groups.
- Add some language processing python package to help users create a todo list for a goal in mind 

## Thank you for reading about my project :)
