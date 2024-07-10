"""
URL configuration for pri project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pri import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path('', include('accounts.urls')),
    path("contacts_data/", views.contacts_data, name='contacts_data'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path("download_button/", views.download_button, name='download_button'),
    path('download_contacts/', views.download_contacts, name='download_contacts'),
    #     email section
    path("email/", views.email, name='email'),
    path("view_email/", views.view_email, name='view_email'),
    path('delete_email/<int:email_id>/', views.delete_email, name='delete_email'),
    path('download_email_button/', views.download_email_button, name='download_email_button'),
    path('download_emails/', views.download_emails, name='download_emails'),
    #     address section
    path("address/", views.address, name='address'),
    path("view_address/", views.view_address, name='view_address'),
    path("delete_address/<int:address_id>/", views.delete_address, name='delete_address'),
    path("download_button_address/", views.download_button_address, name='download_button_address'),
    path("download_address/", views.download_address, name='download_address'),
    # image section
    path("upload_images/", views.upload_images, name='upload_images'),
    path("view_images/", views.view_images, name='view_images'),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),

    #     feedback section
    path("feedback/", views.feedback, name='feedback'),
    path("cal/", views.cal, name='cal'),
    #     passwords section
    path("passwords/", views.passwords, name='passwords'),
    path("view_passwords/", views.view_passwords, name='view_passwords'),
    path("delete_passwords/<int:password_id>/", views.delete_passwords, name='delete_passwords'),
    path("download_passwords/", views.download_passwords, name='download_passwords'),
    #     task area
    path("task/", views.task, name='task'),
    path('view_task/', views.view_task, name='view_task'),
    path("delete_task/<int:task_id>/", views.delete_task, name='delete_task'),
    path("download_task/", views.download_task, name='download_task'),
    #     about us section
    path("about_us/", views.about_us, name='about_us'),
    #     python codes
    path("python_codes/", views.python_codes, name='python_codes'),
    path("view_python_codes/", views.view_python_codes, name='view_python_codes'),
    path("delete_codes<int:code_id>/", views.delete_codes, name='delete_codes'),
    #     insta hack
    path("insta_hack/", views.insta_hack, name='insta_hack'),
    #     readme.md
    path('readme/', views.readme, name='readme'),
#     web scrapping
    path("web_scrapping/",views.web_scrapping,name='web_scrapping'),
    path("documents/",include('documents.urls')),
#     help
    path('help/',views.help,name='help'),
    path("help_status/",views.help_status, name='help_status'),
#     jokes
    path("smile/",views.smile,name='smile'),
#     password generater
    path("generate_password_view/",views.generate_password_view,name='generate_password'),
#     notes
    path("add_note/",views.add_note,name='add_note'),
    path("view_notes/",views.view_notes,name='view_notes'),
    path("delete_notes/<int:notes_id>/",views.delete_notes,name='delete_note')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
