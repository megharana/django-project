from django.shortcuts import render

def home(request,*args,**kwargs):
	from social_core.backends.github import GithubOAuth2
	return render(request,'auth_social.html')
def profile(request):
	from social_core.backends.github import GithubOAuth2
	from github import Github
	g = Github("6a492d69f880a6e9fb59044c4321e182555466b1")
	
	u = g.search_users("Megha", location="India")[0:10]
	second_repo = u
	return render(request,'auth_profile.html',{'data':second_repo})
	
