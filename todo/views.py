from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from uuid import uuid4, UUID

from todo.models import *
from todo.forms import *


def register_view(request):
    if request.method == "POST":
        form = BootstrapUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:login")
    else:
        form = BootstrapUserCreationForm()
    return render(request, "todo/register.html", {"form": form})

@login_required
def logout_view(request):
    # Logout on POST request for user confirmation
    if request.method == "POST":
        logout(request)
        return redirect("todo:login")

    return render(request, "todo/logout.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("todo:task_list")

    if request.method == "POST":
        form = BootstrapAuthForm(request, data=request.POST)

        if form.is_valid():
            # Retrieve the cleaned data from the form
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("todo:task_list")
    else:
        form = BootstrapAuthForm()
    return render(request, "todo/login.html", {"form": form})


@login_required
def task_list(request):
    # Query for current users tasks
    tasks = Task.objects.filter(creator=request.user)
    # Query for all category choices
    categories = Task.category.field.choices

    # Sorting the list
    sort = request.GET.get("sort")
    selected_category = request.GET.get("category")

    # Sort by category, deadline or both
    if selected_category:
        tasks = tasks.filter(category=selected_category)
    if sort == "deadline":
        tasks = tasks.order_by("deadline")
    if sort == "reset":
        return redirect("todo:task_list")

    context = {
        "tasks": tasks,
        "categories": categories,
        "selected_category": selected_category
    }
    return render(request, "todo/task_list.html", context)

@login_required
def create_task(request):
    if request.method == "POST":
        # Save new task
        form = TaskForm(request.POST)
        if form.is_valid():
            # Hold save in order to add current user as creator (from model)
            new_task= form.save(commit=False)
            new_task.creator = request.user
            new_task.save() 
            return redirect("todo:task_list")

    else:
        form = TaskForm()
    return render(request, "todo/create_task.html", {"form": form})

@login_required
def edit_task(request, task_id):
    # Get the task to be edited
    task = get_object_or_404(Task, pk=task_id)
    
    # Save edited task 
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:task_list')

    else:
        # Prefill form with current task object data
        form = TaskForm(instance=task)
        context= {
            "task": task, # To access ID
            "form": form
        }
    return render(request, "todo/edit_task.html", context)

@login_required
def complete_task(request, task_id):
    # Get the task to be deleted
    task = get_object_or_404(Task, pk=task_id)

    # Change the task's status to complete
    task.complete = True
    task.save()
    return redirect("todo:task_list")

@login_required
def delete_tasks(request):
    tasks = Task.objects.filter(creator=request.user)
    return render(request, "todo/delete_tasks.html", {"tasks": tasks})

@login_required
def delete_selected_tasks(request):
    if request.method == "POST":
        # Get the list of selected task IDs from the POST data
        task_ids = request.POST.getlist("task_id")
        
        # Get the tasks with the selected IDs or return a 404 error
        tasks = get_list_or_404(Task, id__in=task_ids)
        for task in tasks:
            task.delete()
            messages.success(request, f"Task '{task}' deleted successfully.")
        return redirect("todo:delete_tasks")
            
    else:
        tasks = Task.objects.filter(creator=request.user)
        return redirect("todo:delete_tasks")


@login_required
def group_list(request):
    # Query for current users tasks
    groups = Group.objects.filter(members=request.user)

    context = {
        "groups": groups,
    }
    return render(request, "todo/group_list.html", context)


@login_required
def create_group(request):
    if request.method == "POST":
        # Create new group
        group_name = request.POST["group_name"]
        join_link = uuid4()
        user = request.user
        new_group = Group.objects.create(name=group_name, join_link=join_link, creator=user)
        # Add user as member
        new_group.members.add(user)
        return redirect("todo:group_list")
    else:
        return render(request, "todo/create_group.html")


@login_required
def group_tasks(request, group_id):
    # Query current group to check if current user is groups creator
    group = get_object_or_404(Group, id=group_id)
    # Query groups tasks
    tasks = Task.objects.filter(group = group_id)
    # Query for all category choices
    categories = Task.category.field.choices

    # Sorting the list
    sort = request.GET.get("sort")
    selected_category = request.GET.get("category")

    # Sort by category, deadline or both
    if selected_category:
        tasks = tasks.filter(category=selected_category)
    if sort == "deadline":
        tasks = tasks.order_by("deadline")
    if sort == "reset":
        return redirect("todo:group_tasks", group_id=group_id)

    context = {
        "tasks": tasks,
        "categories": categories,
        "selected_category": selected_category,
        "group": group
    }
    return render(request, "todo/group_tasks.html", context)

@login_required
def manage_group(request, group_id):
    # Query for group
    group = get_object_or_404(Group, id=group_id)
    # Query for all group members
    members = group.members.all()

    context = {
        "group": group,
        "members": members
        }
    return render(request, "todo/manage_group.html", context)

@login_required
def remove_user_from_group(request, group_id, member_id):
    # Query for group
    group = get_object_or_404(Group, id=group_id)
    # Query for user to be removed
    member = get_object_or_404(User, id=member_id)

    if request.method == "POST":
        if member == group.creator:
            messages.error(request, f"Admin cannot be removed as user")
        else:
            # Remove user from group
            group.members.remove(member)
        
        return redirect("todo:manage_group", group_id=group_id)

    else:
        context = {
            "group": group,
            "member": member
            }
        return render(request, "todo/remove_user_confirm.html", context)

@login_required
def generate_token(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    # Generate a new token for the group
    token = uuid.uuid4()

    if request.method == "POST":
        # Create a new member with blank member 
        new_member = Membership.objects.create(group=group, join_token=token)
        context = {
            "group": group,
            "token": token
        }
        return render(request, "todo/generate_token.html", context)

    else:
        context = {
            "group": group,
            "token": token
        }
        return render(request, "todo/generate_token.html", context)


@login_required
def join_group(request, join_link):
    # Query for group
    group = get_object_or_404(Group, join_link=join_link)
    # Query for all group members
    members = group.members.all()
    if request.method == "POST":
        # Users token input
        token = request.POST.get("token")

        # Check if token is 
        try:
            UUID(token)
            # Query for membership with that token
            membership = get_object_or_404(Membership, join_token=token)
            # membership object exists with matching token
            if membership:
                # user is already member
                if request.user in members:
                    messages.error(request, f"User already in group.")
                # membership user field is empty
                elif not membership.user:
                    membership.user = request.user
                    membership.save()
                    messages.success(request, f"{request.user.username} added successfully")
                    return redirect("todo:group_tasks", group.id)
                else:
                    messages.error(request, f"Error joining group. Please contact group admin.")
        # Invalid token input
        except ValueError:
            messages.error(request, f"Error joining group. Please contact group admin.")
        
        context = {
            "group": group,
        }
        return render(request, "todo/join_group.html", context)

    return render(request, "todo/join_group.html", {"group": group})