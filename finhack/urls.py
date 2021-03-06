"""finhack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^project/(?P<projectID>\S+)', 'main.views.project', name='project'),
    url(r'^ngo/(?P<ngoID>\S+)', 'main.views.ngo', name='ngo'),
    url(r'^donate/(?P<targetmilestone>\S+)', 'main.views.donate', name='donate'),
    url(r'^review/(?P<milestoneID>\S+)', 'main.views.review_milestone', name='review_milestone'),
    url(r'^mytrans/(?P<myid>\S+)', 'main.views.mytrans', name='mytrans'),
    url(r'^seeblockchain/', 'main.views.seeblockchain', name='seeblockchain'),
]
