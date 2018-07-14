from Github import github
from django.shortcuts import render
def users(request):
	g = Github("25d0d092365a3e640fc210f6175423751f01395")
	u = g.get_user()
	return render(request,'auth_profile.html',{'data':'u.name'})