from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import logout_view
from users.views import logout_view, register_view
urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
path('register/', register_view, name='register'),
    path('', include('tasks.urls')),
    path('api/', include('api.urls')),
]