from django.contrib import admin
from django.urls import path, include
from projects import views
from accounts import views as ac_views
from inspections import views as ins_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('inspections/', ins_views.inspections, name='inspections'),
    path('login/', ac_views.login, name='login'),
    path('create/', views.create, name='create'),
    path('project_info/<int:id>/', views.get_project_info, name='get_project_info'),
    path('edit_project/<int:id>/', views.edit_project, name='edit_project'),

]
