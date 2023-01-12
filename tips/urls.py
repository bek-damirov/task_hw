"""tips URL Configuration

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from interview import views as inter_view
from interview import views


schema_view = get_schema_view(
   openapi.Info(
      title="Tips Clone API",
      default_version='v-0.01-alpha',
      description="API для взаимодействия с Task API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bek@gmail.com"),
      license=openapi.License(name="No Licence"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


acc_router = DefaultRouter()
acc_router.register('', inter_view.CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', include(acc_router.urls)),
    path('api/question/', views.QuestionView.as_view()),
    path('api/question/<int:pk>/', views.QuestionAnswerView.as_view()),

    # documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_doc'),

]
