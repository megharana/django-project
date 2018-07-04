from django.shortcuts import render

def home(request,*args,**kwargs):
	from social_core.backends.github import GithubOAuth2
	return render(request,'auth_social.html')
def profile(request):
	from social_core.backends.github import GithubOAuth2
	return render(request,'auth_profile.html')