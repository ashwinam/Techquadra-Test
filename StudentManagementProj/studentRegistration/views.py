import datetime
from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import F
from .forms import StudentRegistrationForm
from .models import StudentRegistration

class StudentRegistrationView(CreateView):
    form_class = StudentRegistrationForm
    model = StudentRegistration
    success_url = '/'
    template_name = 'st_form.html'

    def post(self, request, *args, **kwargs):
        form = StudentRegistrationForm(data=self.request.POST, files=self.request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            email(request, form.email) # type: ignore
            messages.success(self.request, 'ToDo added successfully')

            return render(self.request, 'st_form.html', {'form': StudentRegistrationForm()})
        else:
            error_msg = ''
            for field, errors in form.errors.items():
                error_msg += f'{field}: {",".join(errors)}'
            messages.error(self.request, error_msg)

            return render(self.request, 'st_form.html', {'form': StudentRegistrationForm(self.request.POST)})

def email(request, recipient_mail):
    subject = 'Thank you for registering to our site'
    message = ' it means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient_mail,]
    send_mail( subject, message, email_from, recipient_list )
    return render(request, 'index.html')


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

def logoutUser(request):
    logout(request)
    return redirect('login')


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['todays_std_count'] = StudentRegistration.objects.filter(add_date=datetime.datetime.today().date()).count()
        return super().get_context_data(**kwargs)
    
class ReportView(ListView):
    model = StudentRegistration
    template_name = 'reports.html'
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        kwargs['objects'] = self.model.objects.filter(date_of_birth__range=[start_week, end_week]).order_by('-date_of_birth')
        
        object_list = []
        for object1 in kwargs['objects']:

            blank_dict = {}
            new_date = datetime.date(datetime.date.today().year, object1.date_of_birth.month, object1.date_of_birth.day)
            blank_dict['st_name'] = object1.st_name
            blank_dict['new_date'] = new_date.strftime("%d/%m/%Y")
            object_list.append(blank_dict)

        kwargs['objects'] = object_list
        print(object_list)
        
        return super().get_context_data(**kwargs)