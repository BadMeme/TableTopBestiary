from django.contrib import admin
from .models import ProtoChar, ProtoCamp, ProtoSheet, MemberList, MemberRequest #fix with real models later

# Register your models here.
admin.site.register(ProtoChar)
admin.site.register(ProtoCamp)
admin.site.register(ProtoSheet)
admin.site.register(MemberList)
admin.site.register(MemberRequest)