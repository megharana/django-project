from django.http import HttpResponse
from django.shortcuts import render
from social_core.backends.github import GithubOAuth2
from github import Github
from login.forms import HomeForm


def index(request):
	return HttpResponse("<h1>This is login page</h1>")
def home(request,*args,**kwargs):
	
	return render(request,'auth_social.html')

def getName(request):
	if request.method == 'POST':
		form = HomeForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			print(name)
			g = Github("5e3501899d3db07ba1603cc6c19726532d94f820")
			u = g.search_users(name, location="India")[0:10]
			return render(request,'auth_profile.html',{'data':u})

	else:
			form=HomeForm()
	return render(request, 'auth_profile.html', {'form': form})
