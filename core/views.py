import uuid, re
from time import sleep
from collections import Counter
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django_htmx.http import HttpResponseLocation
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.contrib.auth.hashers import make_password
from .decorators import unauthenticated_user, starter_required, initialized_starter
from .models import Index_Section, Service_Excellence, Projects, SocialMedia, Settings
from .forms import IndexSectionFormA, IndexSectionFormB, IndexSectionFormC, IndexSectionFormD, ServiceExcellenceForm, ProjectForm, SettingsForm, SocialMediaForm, ChangeCredentialPasswordForm
from .initializers import initialize_content


@initialized_starter
def get_started(request):
    page_title = 'Get Started'

    unique_id = uuid.uuid4()

    context = {
        'page_title': page_title,
        'unique_id': unique_id,
    }
    return render(request, 'core/public/starter/get_started.html', context)

@starter_required
def index(request):
    try:
        content = Index_Section.objects.get(page_name='index')
        service_excellence = Service_Excellence.objects.order_by('created_at')[:4]
        projects = Projects.objects.order_by(F('project_status').desc(), '-project_date')[:5]

        interval = datetime.now() - timedelta(days=60)

        announce_latest_project = Projects.objects.filter(
            Q(visibility=True) & Q(project_date__gte=interval)
        ).order_by('-created_at')

        social_media = SocialMedia.objects.filter(social_visibility=True).order_by('created_at')[0:3]
        site_settings = Settings.objects.get()
    except ObjectDoesNotExist:
        content = None
        service_excellence = None
        projects = None
        social_media = None
        site_settings = None

    text_a = content.section_a_text_1 + ' ' + content.section_a_text_2
    text_b = content.section_b_text_1 + ' ' + content.section_b_text_2
    text_c = content.section_c_text_1 + ' ' + content.section_c_text_2
    text_d = content.section_d_text_1 + ' ' + content.section_d_text_2
    combined_text = ' '.join([text_a, text_b, text_c, text_d])

    cleaned_text = ' '.join(re.sub(r'[^\w\s]', '', combined_text).split())

    words = cleaned_text.split()

    word_freq = Counter(words)

    keywords = word_freq.most_common(10)

    keywords = [word for word, count in keywords]

    keyword_string = ', '.join(keywords)

    page_title = content.section_a_text_1
    page_description = content.section_a_text_2

    if request.method == 'POST':
        if 'section_a' in request.POST:
            form = IndexSectionFormA(request.POST, instance=content)
            if form.is_valid():
                form.save()
                messages.success(request, 'Section A content updated')
                return HttpResponseLocation('')
        elif 'section_b' in request.POST:
            form = IndexSectionFormB(request.POST, instance=content)
            if form.is_valid():
                form.save()
                messages.success(request, 'Section B content updated')
                return HttpResponseLocation('')
        elif 'section_c' in request.POST:
            form = IndexSectionFormC(request.POST, instance=content)
            if form.is_valid():
                form.save()
                messages.success(request, 'Section C content updated')
                return HttpResponseLocation('')
        elif 'section_d' in request.POST:
            form = IndexSectionFormD(request.POST, instance=content)
            if form.is_valid():
                form.save()
                messages.success(request, 'Section D content updated')
                return redirect('index')
    else:
        form = IndexSectionFormA(instance=content)

    context = {
        'page_title': page_title,
        'page_description': page_description,
        'keywords': keyword_string,
        'content': content,
        'service_excellence': service_excellence,
        'projects': projects,
        'announce_latest_project': announce_latest_project,
        'social_media': social_media,
        'site_settings': site_settings,
        'form': form,
    }
    return render(request, 'core/public/index/index.html', context)

@starter_required
def our_project(request):
    page_title = 'Our Projects'

    social_media = SocialMedia.objects.filter(social_visibility=True).order_by('created_at')[0:3]
    project_list = Projects.objects.order_by(F('project_status').desc(), '-project_date')
    interval = datetime.now() - timedelta(days=60)

    latest_project = Projects.objects.filter(
        Q(visibility=True) & Q(project_date__gte=interval)
        ).order_by('-project_date')[0:3]

    content = Index_Section.objects.get(page_name='index')

    context = {
        'page_title': page_title,
        'social_media': social_media,
        'project_list': project_list,
        'latest_project': latest_project,
        'content': content,
    }
    return render(request, 'core/public/projects/projects.html', context)

@login_required
def add_project(request):
    page_title = 'Add Project'
    project_list = Projects.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            messages.success(request, project.project_name + ' project has been added')
            return redirect('add-project')

    context = {
        'page_title': page_title,
        'project_list': project_list,
    }
    return render(request, 'core/public/projects/modify_project.html', context)

@login_required
def edit_project(request, project_id):
    page_title = 'Edit Project'
    
    project = Projects.objects.get(project_id=project_id)
    project_list = Projects.objects.all().order_by('-updated_at')

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, project.project_name + ' project has been updated')
            return redirect('edit-project', project_id=project_id)

    context = {
        'page_title': page_title,
        'project': project,
        'project_list': project_list,
    }
    return render(request, 'core/public/projects/modify_project.html', context)

@login_required
def delete_project(request, project_id):
    project = Projects.objects.get(project_id=project_id)
    project.delete()
    messages.success(request, 'Project deleted')
    return redirect('index')

@starter_required
@unauthenticated_user
def sign_in(request):
    page_title = 'Sign in'

    next_url = request.GET.get('next')

    social_media = SocialMedia.objects.filter(social_visibility=True).order_by('created_at')[0:3]

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.get_full_name() == '':
                user_full_name = 'Anonymous'
            else:
                user_full_name = user.get_full_name()
            if next_url:
                messages.success(request, 'Hi, {}'.format(user_full_name) + '. You are now logged in.')
                return redirect(next_url)
            else:
                messages.success(request, 'Hi, {}'.format(user_full_name) + '. You are now logged in.')
                return redirect('index')
        else:
            messages.info(request, 'Incorrect email or password')

    context = {
        'page_title': page_title,
        'next_url': next_url,
        'social_media': social_media,
    }
    return render(request, 'core/public/auth/sign_in.html', context)

@login_required
def site_settings(request):
    page_title = 'Settings'

    try:
        site_settings = Settings.objects.get()
        social_media = SocialMedia.objects.all()
        service_excellence = Service_Excellence.objects.all()
    except Settings.DoesNotExist:
        site_settings = None
        social_media = None
        service_excellence = None

    if request.method == 'POST':
        if 'settings_form' in request.POST:
            settings_form = SettingsForm(request.POST, instance=site_settings)
            if settings_form.is_valid():
                settings_form.save()
                messages.success(request, 'Settings saved')
                return redirect('settings')
        elif 'change_password_form' in request.POST:
            user = request.user
            change_password_form = ChangeCredentialPasswordForm(request.POST or None)
            if change_password_form.is_valid():
                new_password = change_password_form.cleaned_data['new_password']
                user.set_password(new_password)
                user.save()
                return redirect('settings')
    else:
        settings_form = SettingsForm(instance=site_settings)
        change_password_form = ChangeCredentialPasswordForm()

    context = {
        'page_title': page_title,
        'site_settings': site_settings,
        'social_media': social_media,
        'service_excellence': service_excellence,
        'settings_form': settings_form,
        'change_password_form': change_password_form
    }
    return render(request, 'core/public/settings/settings.html', context)

@login_required
def edit_social_media(request, social_name):
    page_title = 'Edit Social Media'

    try:
        social_media = SocialMedia.objects.all()
        social_media_edit = SocialMedia.objects.get(social_name=social_name)
    except SocialMedia.DoesNotExist:
        social_media = None
        social_media_edit = None

    if request.method == 'POST':
        form = SocialMediaForm(request.POST, instance=social_media_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social media updated')
            return redirect('settings')

    context = {
        'page_title': page_title,
        'social_media': social_media,
        'social_media_edit': social_media_edit,
    }
    return render(request, 'core/public/settings/settings.html', context)

@login_required
def edit_service_excellence(request, service_id):
    page_title = 'Edit Service Excellence'

    try:
        service_excellence = Service_Excellence.objects.all()
        service_excellence_edit = Service_Excellence.objects.get(service_id=service_id)
    except Service_Excellence.DoesNotExist:
        service_excellence = None
        service_excellence_edit = None

    if request.method == 'POST':
        service_excellence_form = ServiceExcellenceForm(request.POST, instance=service_excellence_edit)
        if service_excellence_form.is_valid():
            service_excellence_form.save()
            messages.success(request, 'Service excellence updated')
            return redirect('settings')


    context = {
        'page_title': page_title,
        'service_excellence': service_excellence,
        'service_excellence_edit': service_excellence_edit,
    }
    return render(request, 'core/public/settings/settings.html', context)

@initialized_starter
def initialize_tailnode_site_data(request, uuid):
    sleep(7)

    initialize_content(request)

    return redirect(reverse('get-started'))