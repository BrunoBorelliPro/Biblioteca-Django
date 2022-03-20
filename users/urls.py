from django.urls import path

from users.views import UserCreateView, UsersListView, UserUpdateView, UserDeleteView, UserDetailView


app_name = 'users'

urlpatterns = [
    path('create_users/', UserCreateView.as_view(), name='cadastro_users'),
    path('list_users/', UsersListView.as_view(), name='list_users'),
    path('<pk>/user_detail/', UserDetailView.as_view(), name='user_detail'),
    path('<pk>/update_users/', UserUpdateView.as_view(), name='update_users'),
    path('<pk>/delete_users/', UserDeleteView.as_view(), name='delete_users'),
]
