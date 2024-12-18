"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('latest-transfers/', LatestransfersView.as_view(), name='latest-transfers'),
    path('players/', PlayersView.as_view(), name='players'),
    path('u20players/', U20playersView.as_view(), name='u20players'),
    path('tryouts/', TryoutsView.as_view(), name='tryouts'),
    path('about/', AboutView.as_view(), name='about'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('statistics/transfer-records/', TransferRecordsView.as_view(), name='transfer-records'),
    path('statistics/top-50-clubs-by-income/', Top50IncomeView.as_view()),
    path('statistics/top-50-clubs-by-expenditure/', Top50ExpenditureView.as_view()),
    path('statistics/accurate-prediciton/', AccuratePredictionView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
