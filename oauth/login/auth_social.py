from django.shortcuts import render

def home(request,*args,**kwargs):
	from social_core.backends.github import GithubOAuth2
	return render(request,'auth_social.html')
def profile(request):
	from social_core.backends.github import GithubOAuth2
	from github import Github
	g = Github("fbaaaa43e58016f57e9a66ef9397d9a6b44f425b")
	u = g.search_users("abhishek", location="India")[1]
	second_repo = u.id
	return render(request,'auth_profile.html',{'data':second_repo})
	
