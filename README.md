# PLANiT


### Description:
This is my CS50 final project!

PLANiT is a todo list webapp, using the Django framework and python language.
The app supports user registration, once registered and logged in a user can create a todo list. Users can add tasks to their todo list as well as edit tasks and mark them as completed. Additionally users can delete unwanted tasks.
PLANiT allows users to set a priority, deadline, and category for tasks. Users can also sort their todo list by deadline and category or both. PLANiT also supports group functionality, users can create groups. Users join groups via the groups url and a unique token. The group admin can control group specific functionality  

## Installation

- Clone the repository to your local machin
```bash
git clone https://github.com/MatanVatkin/PLANiT.git
```

- Navigate to the project directory using
```bash
cd folder_name
```

- Create a new virtual environment for the project
```bash
python -m venv venv
```

- Activate the virtual environment
```bash
macOS or Linux - source venv/bin/activate
Windows - venv\Scripts\activate
```

- Install the required packages
```bash
pip install -r requirements.txt
```

- Setup the database:
```bash
python manage.py migrate
```

- Finally, start the development server using
```bash
python manage.py runserver
```
That's it! You should now be able to access the project in your web browser at 
```bash
http://127.0.0.1:8000/
```

#### Future plans:
I have some additional feature ideas that may be implemented in a future date.
- Create friend list and make shareable tasks.
- Create task groups.
- Add some language processing python package to help users create a todo list for a goal in mind 

## Thank you for reading about my project :)
