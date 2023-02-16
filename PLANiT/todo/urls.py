from django.urls import path

from todo.views import *


app_name = "todo"

urlpatterns = [
    path("", task_list, name="task_list"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("create_task/", create_task, name="create_task"),
    path("delete_tasks/", delete_tasks, name="delete_tasks"),
    path("delete_selected_tasks/", delete_selected_tasks, name="delete_selected_tasks"),
    path("group_list/", group_list, name="group_list"),
    path("create_group/", create_group, name="create_group"),
    path("edit_task/<int:task_id>/", edit_task, name="edit_task"),
    path("complete_task/<int:task_id>/", complete_task, name="complete_task"),
    path("group_tasks/<int:group_id>/", group_tasks, name="group_tasks"),
    path("manage_group/<int:group_id>/", manage_group, name="manage_group"),\
    path("group/<int:group_id>/generate_token/", generate_token, name="generate_token"),
    path('join_group/<uuid:join_link>/', join_group, name='join_group'),
    path("remove_user_from_group/<int:group_id>/<int:member_id>/", remove_user_from_group, name="remove_user_from_group"),
]