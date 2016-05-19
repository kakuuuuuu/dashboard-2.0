from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.contrib.auth.models import User
from models import UserProfile
from ..posts.models import Post, Comment
class Main(View):
    template = ''
    context = None
    user = None
    def get(self, request):
        context = {'templateData': self.user}
        return render(request, self.get_template(), context)
    def get_template(self):
        if self.template == '':
            raise ImproperlyConfigured("'Template' is not defined.")
        return self.template
# Create your views here.
class Index(Main, View):
    template = 'dash/index.html'

class Dashboard(ListView):
    model = User
    template_name = 'dash/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        return context
def userpage(request, user_id):
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)
    posts = Post.objects.all().filter(reciever=user)
    comments = Comment.objects.all()
    context={
        'user':user,
        'profile':profile,
        'posts':posts,
        'comments':comments
    }
    return render(request,'dash/userpage.html',context)
