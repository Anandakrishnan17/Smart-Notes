from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name= 'home/register.html'
    success_url= 'Notes_model/notes'

    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('Notes_mode.list')
        return super().get(request,*args,**kwargs)

class LoginInterfaceView(LoginView):
    template_name='home/login.html'

# class LogoutInterfaceView(HttpResponse,LogoutView):
#     template_name = 'home/logout.html'  
 
def logout_view(request):
    logout(request)
    return render(request,'home/logout.html')

    
    

class HomeView(TemplateView):
    template_name= 'home/welcome.html'


