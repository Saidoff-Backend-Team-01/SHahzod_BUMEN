from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(_("name"), max_length=100)
    clicked_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")


class SubjectTitle(models.Model):
    name = models.CharField(_("name"), max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("SubjectTitle")
        verbose_name_plural = _("SubjectTitle")


class Subject(models.Model):
    name = models.CharField(_("name"), max_length=100)
    type = models.TextField()
    subject_title = models.ForeignKey(SubjectTitle, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subject")


# class SubjectType(models.Model):
#     name = models.CharField(_("name"), max_length=100)
#     local = models.


class UserSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_test_ball = models.FloatField()

    class Meta:
        verbose_name = _("UserSubject")
        verbose_name_plural = _("UserSubject")


class Vacancy(models.Model):
    name = models.CharField(_("name"), max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(_("description"))

    class Meta:
        verbose_name = _("Vacancy")
        verbose_name_plural = _("Vacancy")


class Step(models.Model):
    title = models.CharField(_("title"), max_length=50)
    order = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField(_("description"))

    class Meta:
        verbose_name = _("Step")
        verbose_name_plural = _("Step")


class Club(models.Model):
    name = models.CharField(_("name"), max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField(_("description"))

    class Meta:
        verbose_name = _("Club")
        verbose_name_plural = _("Club")


class UserClub(models.Model):
    user = models.ManyToManyField(Club, related_name="users")
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("UserClub")
        verbose_name_plural = _("UserClub")


class ClubMeeting(models.Model):
    name = models.CharField(_("name"), max_length=100)
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    # club = models.

    class Meta:
        verbose_name = _("ClubMeeting")
        verbose_name_plural = _("ClubMeeting")


class StepLesson(models.Model):
    title = models.CharField(_("title"), max_length=50)
    # file = models.ForeignKey()
    step = models.ForeignKey(Step, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("StepLesson")
        verbose_name_plural = _("StepLesson")


################################
class StepTest(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    ball_for_each_test = models.FloatField()
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    question_type = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )
    type = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )
###########################


# class Mode(models.Model):
#     midterm =


class TestQuestion(models.Model):
    steptest = models.ForeignKey(StepTest, on_delete=models.CASCADE)
    text = models.TextField(_("test"))

    class Meta:
        verbose_name = _("TestQuestion")
        verbose_name_plural = _("TestQuestion")


class TestAnswer(models.Model):
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    text = models.TextField(_("text"))
    is_correct = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("TestAnswer")
        verbose_name_plural = _("TestAnswer")


class UserTestResult(models.Model):
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    test_answer = models.ForeignKey(TestAnswer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("UserTestResult")
        verbose_name_plural = _("UserTestResult")


class UserTotalTestResult(models.Model):
    step_test = models.ForeignKey(StepTest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#############################################
    ball = models.FloatField()
    # correct_ans = models.
##########################################

    class Meta:
        verbose_name = _("UserTotalTestResult")
        verbose_name_plural = _("UserTotalTestResult")


