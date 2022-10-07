from django.contrib import admin
from documanager.models import Document
from documanager.models import Revision
from documanager.models import User

admin.site.register(Document)
admin.site.register(Revision)
admin.site.register(User)
