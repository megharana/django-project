from django.shortcuts import render

def home(request):
	from social_core.backends.github import GithubOAuth2
	return render(request,'auth_social.html')