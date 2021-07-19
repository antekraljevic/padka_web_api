"""padka_web_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transitions',views.showTransitions),
    path('transitions/createTransition', views.transitions),  
    path('transitions/downloadJsonTransitions',views.downloadJsonTransitions),  
    path('transitions/editTransition/<int:id>', views.editTransition),  
    path('transitions/updateTransition/<int:id>', views.updateTransition),  
    path('transitions/deleteTransition/<int:id>', views.destroyTransition),
    path('reactions',views.showReactions),
    path('reactions/createReaction', views.reactions),  
    path('reactions/downloadJsonReactions',views.downloadJsonReactions),  
    path('reactions/editReaction/<int:id>', views.editReaction),  
    path('reactions/updateReaction/<int:id>', views.updateReaction),  
    path('reactions/deleteReaction/<int:id>', views.destroyReaction),
    path('music',views.showMusic),
    path('music/createMusic', views.music),  
    path('music/downloadJsonMusic',views.downloadJsonMusic),  
    path('music/editMusic/<int:id>', views.editMusic),  
    path('music/updateMusic/<int:id>', views.updateMusic),  
    path('music/deleteMusic/<int:id>', views.destroyMusic),
    path('downloadAllAsJSON', views.downloadAllAsJSON),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
