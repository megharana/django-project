from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from login import views
# from social_django.urls import extra
# from login.views import complete


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
   
    url(r'auth/social/', views.home, name='auth-social'),
    url(r'auth-social/', include('social_django.urls',namespace='social')),
	url(r'accounts/profile/', views.getName, name='getName'),
	url(r'^auth/posts/',include(("login.api.urls",'login'),namespace='posts-api')),
	
	
	
	#url(r'^complete/(?P<backend>[^/]+){0}$'.format(extra), complete, name='complete'),

]
