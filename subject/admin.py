from django.contrib import admin
from subject.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(SubjectTitle)
admin.site.register(UserSubject)
admin.site.register(Vacancy)
admin.site.register(Step)
admin.site.register(Club)
admin.site.register(UserClub)
admin.site.register(ClubMeeting)
admin.site.register(StepLesson)
admin.site.register(StepTest)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)
admin.site.register(UserTestResult)
admin.site.register(UserTotalTestResult)


