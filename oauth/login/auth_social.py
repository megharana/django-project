from django.http import HttpResponseRedirect
from django.shortcuts import render
from social_core.backends.github import GithubOAuth2
from github import Github
from login.forms import HomeForm

def home(request,*args,**kwargs):
	
	return render(request,'auth_social.html')
def profile(request):
	
	g = Github("6a492d69f880a6e9fb59044c4321e182555466b1")
	
	u = g.search_users("Megha", location="India")[0:10]
	second_repo = u
	return render(request,'auth_profile.html',{'data':second_repo})
	
def getName(request):
	if request.method == 'POST':
		form = HomeForm(request.POST)
		if form.is_valid():

			return HttpResponseRedirect('https://www.google.com/')
	else:
			form=HomeForm()
	return render(request, 'auth_profile.html', {'form': form})
