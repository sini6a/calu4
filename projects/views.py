from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User

from .models import Project, Donation
from .forms import NewDonationForm

def index(request):
    proekti = []
    korisnici = []

    project_list = Project.objects.order_by('-project_Date')

    project_ids = Donation.objects.all().values_list('project_Id', flat=True)
    projects = Project.objects.all().values_list('project_Name', flat=True)
    user_ids = Donation.objects.all().values_list('user_Id', flat=True)
    users = User.objects.all().values_list('username', flat=True)
    
    last_project_id = Project.objects.latest('project_id').project_id
    
    final_donated = 0
    total_donated = Donation.objects.all().values_list('donated', flat=True)
    
    for value in total_donated:
        final_donated = final_donated + value
        
    for project in project_ids:
        tempvar = Project.objects.get(pk=project).project_Name
        proekti.append(tempvar)
        
    for user in user_ids:
        tempvar = User.objects.get(pk=user).username
        korisnici.append(tempvar)
    
    korisnici.reverse()
    proekti.reverse()
    
    template = loader.get_template('home.html')
    context = {
        'project_list': project_list,
        'users': korisnici,
        'projects':proekti,
        'last_project_id':last_project_id,
        'total_donated':final_donated,
    }
    return HttpResponse(template.render(context, request))
    
# def project(request, project_id):
    # project_list = Project.objects.get(pk=project_id)
    # template = loader.get_template('project_info.html')
    # context = {
        # 'project_list': project_list,
    # }
    # return HttpResponse(template.render(context, request))

def project(request, project_id):
    if request.method == 'POST':
        form = NewDonationForm(request.POST)
        if form.is_valid():
            donated = form.cleaned_data.get('amount_to_Donate')
            update_info = Project.objects.get(pk=project_id)
            update_info.project_Reach = update_info.project_Reach + donated
            update_info.save()
            current_user = request.user.id
            update_donation = Donation(user_Id = current_user, project_Id = project_id, donated = donated)
            update_donation.save()
            return redirect('thankyou')
    else:
        form = NewDonationForm()
        project_list = Project.objects.get(pk=project_id)
        template = loader.get_template('project_info.html')
        context = {
            'project_list': project_list,
        }
    return render(request, 'project_info.html', {'project_list': project_list, 'form': form})
    
def thankyou(request):
    return render(request, 'thank_you.html')    
    
def about(request):
    return render(request, 'about.html')   
