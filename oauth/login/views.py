from django.http import HttpResponse
from django.shortcuts import render
from social_core.backends.github import GithubOAuth2
from github import Github
from login.forms import HomeForm
from login.models import User

def index(request):
	return HttpResponse("<h1>This is login page</h1>")
def home(request,*args,**kwargs):
	all_users=User.objects.all()
	for user in all_users:
		print (user.username, user.usertype)
	return render(request,'auth_social.html')

def getName(request):
	if request.method == 'POST':
		form = HomeForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			print(name)
			g = Github("873cf040ccddfa9ed50d579b49abf2b963055e08")
			users = g.search_users(name, location="India")[0:10]
			# for user in users:
			# 	u=User.objects.create(username=user.login, usertype=user.type)
			# 	u.save()
			return render(request,'auth_profile.html',{'data':users})

	else:
			form=HomeForm()
	return render(request, 'auth_profile.html', {'form': form})
