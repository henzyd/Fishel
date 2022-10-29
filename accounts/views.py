from django.shortcuts import render, redirect
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import CustomUser
# from rest_framework import status
# from drf_yasg.utils import swagger_auto_schema


# Create your views here.

def user_create_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserRegistrationForm(request.POST, request.FILES)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # form_user_name = form.cleaned_data.get('username')
            print(form.data)
            form_first_name = form.cleaned_data.get('first_name')
            form_last_name = form.cleaned_data.get('last_name')
            form_email = form.cleaned_data.get('email')
            form_password1 = form.cleaned_data.get('password')
            form_password2 = form.cleaned_data.get('password_2')
            hashed_password = make_password(form_password1, salt=None, hasher='default')
            form_teacher = form.cleaned_data.get('teacher')
            form_student = form.cleaned_data.get('student')
            form_school_attend = form.cleaned_data.get('school_attend')
            form_student_class = form.cleaned_data.get('student_class')
            form_teacher_school_teach = form.cleaned_data.get('teacher_school_teach')
            form_teacher_class_teach = form.cleaned_data.get('teacher_class_teach')
            form_professional_qualification_file = form.cleaned_data.get('professional_qualification_file')
            form_professional_qualification_url = form.cleaned_data.get('professional_qualification_url')
            form_username = f'{form_first_name} {form_last_name} {form_email}'
            if form_password1 == form_password2:
                user = CustomUser.objects.create(
                    username=form_username, 
                    first_name=form_first_name, 
                    last_name=form_last_name, 
                    email=form_email, 
                    password=hashed_password,
                    teacher=form_teacher,
                    student=form_student,
                    school_attend=form_school_attend,
                    student_class=form_student_class,
                    teacher_school_teach=form_teacher_school_teach, 
                    teacher_class_teach=form_teacher_class_teach,
                    professional_qualification_file=form_professional_qualification_file,
                    professional_qualification_url=form_professional_qualification_url,

                )
                user.save()
                # form.save()
            # form.save()
            messages.success(request, f'{form_first_name} {form_last_name} Saved')
            # redirect to a new URL:
            return redirect('home_page')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


