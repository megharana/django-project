from django.http import HttpResponse
from django.shortcuts import render
from social_core.backends.github import GithubOAuth2
from github import Github
from login.forms import HomeForm,InfoHome
from login.models import User

def index(request):
	return HttpResponse("<h1>This is login page</h1>")
def home(request,*args,**kwargs):
	
	return render(request,'auth_social.html')

def getName(request):
	if request.method == 'POST' and 'name' in request.POST:
		form1 = HomeForm(request.POST)
		#form2 = HomeForm(request.POST,prefix="loginInfo")
		if form1.is_valid():
			name=form1.cleaned_data['name']
			print(name)
			g = Github("0d61bdde2f6507723cd28e040ecc9853973ca9ef ")
			users = g.search_users(name, location="India")[0:10]
			# for user in users:
			# 	print(user.avatar_url)
			return render(request,'auth_profile.html',{'data':users})
			# if form2.is_valid():
			# 	loginInfo=form2.cleaned_data['loginInfo']
			# return render(request,'auth_profile.html',{'data':users,'loginInfo':loginInfo})

	else:
			form1 = HomeForm()
			
	

	if request.method=='POST' and 'loginInfo' in request.POST:
		print("sandhya")
		form1 = InfoHome(request.POST)
		if form1.is_valid():
			#print("hello")
			userdetails=[]
			loginInfo=form1.cleaned_data['loginInfo']
			#print(loginInfo)
			detail=loginInfo.split(",")		
			#print(detail[0])
			
			u=User.objects.create(username=detail[0],usertype=detail[1],userAvatarUrl=detail[2])
			u.save()
	else:
		form1 = InfoHome()

	all_users=User.objects.all()
	for user in all_users:
		print (user.username)
	return render(request, 'auth_profile.html', {'form1': form1,'all_users':all_users})