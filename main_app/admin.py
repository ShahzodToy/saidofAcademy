from django.contrib import admin
from .models import *


for a in [Partner,FAQ,DevelopingProgram,WhyUs,DevelopingProgramDetail]:
    admin.site.register(a)