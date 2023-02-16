from django.forms import ModelForm, DateInput, DateField
from datetime import date
from todo.models import Task
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Add bootstrap to built-in django forms
class BootstrapAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class BootstrapUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class TaskForm(ModelForm):

    # Limit datefield to not include past dates
    deadline = DateField(widget=DateInput(attrs={'type': 'date','min': date.today()}))
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'category', 'priority', 'group']

    # Add bootstrap class to form fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
