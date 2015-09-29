
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
	
url(r'^home$', TemplateView.as_view(template_name='news/home.html'), name="home"),

]


