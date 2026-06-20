from django.shortcuts import render , redirect
from django.core.mail import send_mail
from .models import Projects , Tools
import requests
from portfolio_core.settings import TOKEN
# Create your views here.

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


def home(request):
    r = requests.get("https://api.github.com/user", headers=headers)
    repo_count = r.json()['public_repos']

    projects = Projects.objects.all()
    tools = Tools.objects.all()

    context = {
        'repo_count' : repo_count,
        'projects' : projects,
        'tools' : tools
    }

    return render(request , "home.html" , context)

def compose_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = f"Message from \n\n Name : {name} \n\n Email : ({email}):\n\n Phone : {phone} \n\n Message : {message}"

        send_mail(subject , full_message , email, ['dangerm249@gmail.com'],fail_silently=False,)
        return redirect('home')