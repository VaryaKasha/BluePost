"""bluepost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from post.views import IndexView
from post.views import TrackView, TrackResultView
from post.views import OperatorView
from post.views import LoginView, LogoutView
from post.views import NewPackageView, EditPackageView, PackageStatisticView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('track', TrackView.as_view(), name='track'),
    path('operator', OperatorView.as_view(), name='operator'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    url(r'^track/(?P<pk>\d+)$', TrackResultView.as_view(), name='track_result'),
    path('package/new', NewPackageView.as_view(), name='new_package'),
    url(r'^package/edit/(?P<pk>\d+)$', EditPackageView.as_view(), name='edit_package'),
    path('statistic', PackageStatisticView.as_view(), name='statistic'),
]
