"""documanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from documanager.settings import MEDIA_URL, MEDIA_ROOT
from documanager.views.v1.document import create_single_revision
from documanager.views.v1.document import single_document
from documanager.views.v1.document import revision_list
from documanager.views.v1.user import document_list
from documanager.views.v1.user import user_list
from documanager.views.v1.user import create_single_document
from documanager.views.v1.user import single_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/users/", user_list),
    path("v1/user/", single_user),
    path("v1/user/<int:id>", single_user),
    path("v1/user/<int:id>/documents", document_list),
    path("v1/user/<int:id>/document", create_single_document),
    path("v1/document/<int:id>", single_document),
    path("v1/document/<int:id>/revisions", revision_list),
    path("v1/document/<int:id>/revision", create_single_revision)
]

""" To see response on json format -> /users/1?format=json """
urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json", "html"])
""" To allow files to be retrieved from http """
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
