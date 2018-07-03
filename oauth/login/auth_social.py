from django.shortcuts import render

def home(request, 'args, ''kwargs):
	from social_core.backends.github import GithubOAuth2
	return render(request,'auth/auth_social.html')