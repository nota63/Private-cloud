from datetime import datetime

from django.shortcuts import render, redirect
from contacts.models import Contacts
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import csv
from django.http import HttpResponse
from plyer import notification
import time
from email_cloud.models import Email_Cloud
from address.models import Address
from images.models import Image
from django.contrib.auth.decorators import login_required
from feedback.models import Feedback
from credentials.models import Credentials
from tasks.models import Tasks
from developer.models import Developer
import requests
import time
import datetime
from requests.exceptions import ConnectionError
from bugs.models import Bugs
import pyjokes as jokes
import secrets
import string
from notes.models import Notes


# @login_required
def home(request):
    return render(request, 'home.html')


def contacts_data(request):
    data = Contacts.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        relation = request.POST.get('relation')
        contact_number = request.POST.get('contact_number')
        notification.notify(
            title="Private Cloud",
            message=f"successfully saved contact of {name} into Database!",
            timeout=5
        )
        ob = Contacts(name=name, relation=relation, contact_number=contact_number)
        ob.save()
        messages.success(request, "Contact saved")
    return render(request, 'contacts.html', {'data': data})


def view_contacts(request):
    data = Contacts.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search')
        if search != None:
            data = Contacts.objects.filter(name__icontains=search)
    return render(request, 'view_contacts.html', {'data': data})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contacts, id=contact_id)
    contact.delete()
    messages.success(request, 'Contact deleted successfully!')
    return redirect('view_contacts')


def download_button(request):
    return render(request, 'download_button.html')


def download_contacts(request):
    contacts = Contacts.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Relation', 'Contact Number'])

    for contact in contacts:
        writer.writerow([contact.name, contact.relation, contact.contact_number])

    return response


# email section

def email(request):
    email_data = Email_Cloud.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        messages.success(request, "Email saved successfully")
        oc = Email_Cloud(name=name, email=email)
        oc.save()
        notification.notify(
            title="Private Cloud",
            message=f"private email of {name} saved done",
            timeout=5
        )

    return render(request, 'email.html')


def view_email(request):
    email_data = Email_Cloud.objects.all()
    if request.method == 'GET':
        email_search = request.GET.get('email_search')
        if email_search != None:
            email_data = Email_Cloud.objects.filter(name__icontains=email_search)
    return render(request, 'view_email.html', {'email_data': email_data})


def delete_email(request, email_id):
    email_entry = get_object_or_404(Email_Cloud, id=email_id)
    email_entry.delete()
    messages.success(request, "Email deleted successfully")
    return redirect('view_email')


def download_email_button(request):
    return render(request, 'download_email_button.html')


def download_emails(request):
    emails = Email_Cloud.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email'])

    for em in emails:
        writer.writerow([em.name, em.email])

    return response


# ADDRESSES AREA STARTS

def address(request):
    private_ad = Address.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin_code')
        colony = request.POST.get('colony')
        house_number = request.POST.get('house_number')
        district = request.POST.get('district')
        state = request.POST.get('state')
        country = request.POST.get('country')
        db = Address(name=name, city=city, pin_code=pin_code, colony=colony, house_number=house_number,
                     district=district, state=state, country=country)
        db.save()
        messages.success(request, "Address saved successfully")
        notification.notify(
            title='Private Cloud',
            message=f'Address of {name} saved to database',
            timeout=5
        )
        return redirect('address')
    return render(request, 'address.html')


def view_address(request):
    private_ad = Address.objects.all()
    if request.method == 'GET':
        add_search = request.GET.get('add_search')
        if add_search != None:
            private_ad = Address.objects.filter(name__icontains=add_search)
    return render(request, 'view_address.html', {'data': private_ad})


def delete_address(request, address_id):
    address_entry = get_object_or_404(Address, id=address_id)
    address_entry.delete()
    messages.success(request, "Address deleted successfully")
    return redirect('view_address')


def download_button_address(request):
    return render(request, 'download_button_addres.html')


def download_address(request):
    address = Address.objects.all()
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="addresses.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'City', "Pin code", "colony", 'House Number', "District", 'State Country'])
    for em in address:
        writer.writerow([em.name, em.city, em.pin_code, em.colony, em.house_number, em.district, em.state, em.country])
    return response


# IMAGE AREA STARTS

def upload_images(request):
    if request.method == 'POST':
        title = request.POST['title']
        image_file = request.FILES['image']  # Get the uploaded image file
        new_image = Image(title=title, image=image_file)
        new_image.save()
        messages.success(request, "Image saved success")
        notification.notify(
            title="Private Cloud",
            message=f"Image  {title} saved to Database",
            timeout=5
        )
        return redirect('upload_images')  # Redirect to view images page after successful upload
    return render(request, 'upload_image.html')


def view_images(request):
    images = Image.objects.all()
    if request.method == 'GET':
        image_search = request.GET.get('image_search')
        if image_search != None:
            images = Image.objects.filter(title__icontains=image_search)
    return render(request, 'view_images.html', {'images': images})


def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('view_images')


# FEEDBACK SECTION
def feedback(request):
    data = Feedback.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        rating = request.POST.get('rating')
        recommend = request.POST.get('recommend')
        store = Feedback(name=name, email=email, comments=comments, rating=rating, recommend=recommend)
        store.save()
        messages.success(request, 'thanks for your feedback!')
        notification.notify(
            title="Private cloud",
            message=f' Thanks {name} for your feedback',
            timeout=5
        )
        return redirect('feedback')
    return render(request, 'feedback.html')


def cal(request):
    return render(request, 'calender.html')


# passwords area starts

def passwords(request):
    credential = Credentials.objects.all()
    if request.method == 'POST':
        platform = request.POST.get('platform')
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = Credentials(platform=platform, username=username, password=password)
        data.save()
        messages.success(request, "Password saved successfully")
        notification.notify(
            title='Private Cloud',
            message=f"your password of {platform} saved to database",
            timeout=5
        )
        return redirect('passwords')
    return render(request, 'passwords.html')


def view_passwords(request):
    data = Credentials.objects.all()
    if request.method == 'GET':
        password_search = request.GET.get('password_search')
        if password_search != None:
            data = Credentials.objects.filter(platform__icontains=password_search)
    return render(request, 'view_passwords.html', {'data': data})


def delete_passwords(request, password_id):
    data = get_object_or_404(Credentials, id=password_id)
    data.delete()
    messages.success(request, 'password deleted successfully')
    return redirect('view_passwords')


def download_passwords(request):
    data = Credentials.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="passwords.csv"'

    writer = csv.writer(response)
    writer.writerow(['Platform', 'Username/Email', 'Password'])

    for password in data:
        writer.writerow([password.platform, password.username, password.password])

    return response


# TASKS SECTION
def task(request):
    tasks = Tasks.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task')
        time = request.POST.get('time')
        date = request.POST.get('date')
        description = request.POST.get('description')
        select = request.POST.get('select')
        data = Tasks(task=task, time=time, date=date, description=description, select=select)
        data.save()
        messages.success(request, 'Task saved successfully')
        notification.notify(
            title="Private Cloud",
            message=f"Task saved! and we know your task is {select} for you😛!\n and be alert you have to accomplish "
                    f"your task on {date} At {time} 😅",
            timeout=11
        )
        return redirect('task')
    return render(request, 'task.html')


def view_task(request):
    data = Tasks.objects.all()
    if request.method == 'GET':
        task_search = request.GET.get('task_search')
        if task_search != None:
            data = Tasks.objects.filter(task__icontains=task_search)
    return render(request, 'view_task.html', {'data': data})


def delete_task(request, task_id):
    data = get_object_or_404(Tasks, id=task_id)
    data.delete()
    messages.success(request, "task deleted successfully")
    return redirect('view_task')


def download_task(request):
    data = Tasks.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks.csv"'

    writer = csv.writer(response)
    writer.writerow(['Task', 'Time', 'Date', 'Description', 'Importance Level'])

    for task in data:
        writer.writerow([task.task, task.time, task.date, task.description, task.select])

    return response


# about us
def about_us(request):
    return render(request, 'about_us.html')


# python code scripts section

def python_codes(request):
    dev = Developer.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        python_version = request.POST.get('python_version')
        required_libraries = request.POST.get('required_libraries')
        code = request.POST.get('code')
        data = Developer(title=title, description=description, python_version=python_version,
                         required_libraries=required_libraries, code=code)
        data.save()
        messages.success(request, "Script saved successfully!")
        return redirect('python_codes')
    return render(request, 'python_codes.html')


def view_python_codes(request):
    data = Developer.objects.all()
    if request.method == 'GET':
        code_search = request.GET.get('code_search')
        if code_search != None:
            data = Developer.objects.filter(title__icontains=code_search)
    return render(request, 'view_python_codes.html', {'data': data})


def delete_codes(request, code_id):
    data = get_object_or_404(Developer, id=code_id)
    data.delete()
    messages.success(request, "Code snippet deleted successfully")
    return redirect('view_python_codes')


# insta hack

def insta_hack(request):
    return render(request, 'insta_hack.html')


# README.md

def readme(request):
    return render(request, 'readme.html')


# web scrapping
def web_scrapping(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        response = requests.get(url)
        html_content = response.text
        if html_content:
            messages.success(request, "request accomplished successfully")
            notification.notify(
                title='Private Cloud',
                message=f' request successfull for {url}',
                timeout=5
            )
            return render(request, 'web_scrapping.html', {'html_content': html_content})
        else:
            messages.error(request, "request denied! please try again later")
    return render(request, 'web_scrapping.html')


# HELP
def help(request):
    bugs = Bugs.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        section = request.POST.get('section')
        issue = request.POST.get('issue')
        email = request.POST.get('email')
        date = request.POST.get('date')
        try:
            bugs = Bugs(name=name, username=username, section=section, issue=issue, email=email, date=date)
            bugs.save()
            messages.success(request, "bug report submitted successfully")
            notification.notify(
                title='Private Cloud',
                message=f"Hello {name} your bug report was submitted you can check your bug status on 'help_status'\n "
                        f"Thanks for your patience",
                timeout=9
            )
            return redirect('help_status')
        except ConnectionError:
            messages.error(request, "please connect to the internet!")
        except WindowsError:
            messages.error(request, 'some error occurred please try again later')
    return render(request, 'help.html')


def help_status(request):
    bugs = Bugs.objects.all()
    return render(request, 'help_status.html', {'bugs': bugs})


# JOKES
def smile(request):
    joke = jokes.get_joke(language='en', category='neutral')
    data = (joke)
    return render(request, 'smile.html', {'data': data})


# generate passwords
def generate_password_view(request):
    password = ''
    length = 12  # Default password length

    if request.method == 'POST':
        length = int(request.POST.get('length', 12))
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))

    return render(request, 'generate_password_view.html', {'password': password, 'length': length})


# NOTES

def add_note(request):
    note = Notes.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        topic = request.POST.get('topic')
        notes = request.POST.get('notes')
        data = Notes(date=date, topic=topic, notes=notes)
        data.save()
        messages.success(request, "Note saved to database")
        return redirect('add_note')
    return render(request, 'add_note.html')


def view_notes(request):
    data = Notes.objects.all()
    if request.method == 'GET':
        note_search=request.GET.get('note_search')
        if note_search != None:
            data = Notes.objects.filter(topic__icontains=note_search)
    return render(request, 'view_notes.html', {'data': data})


def delete_notes(request, notes_id):
    note = get_object_or_404(Notes, id=notes_id)
    note.delete()
    messages.success(request, "Note deleted successfully")
    return redirect('view_notes')
