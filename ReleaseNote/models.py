from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title
    

class ReleaseNote(models.Model):
    version_number = models.CharField(max_length=6)
    published_date = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"یادداشت انتشار {self.version_number} پروژه {self.project.title}"


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.full_name


class ReleaseNoteDetail(models.Model):
    class SizeChoices(models.IntegerChoices):
        SMALL = 1, "SMALL"
        MEDIUM = 2, "MEDIUM"
        LARGE = 3, "LARGE"

    class PriorityChoices(models.IntegerChoices):
        LOW = 1, "LOW"
        MEDIUM = 2, "MEDIUM"
        HIGH = 3, "HIGH"

    class TypeChoices(models.IntegerChoices):
        ERROR = 1, "ERROR"
        FEATURE = 2, "FEATURE"
        IMPROVEMENT = 3, "IMPROVEMENT"

    class DomainChoices(models.IntegerChoices):
        SYSTEM = 1, "SYSTEM"
        ADMIN = 2, "ADMIN"
        END_USER = 3, "END_USER"

    release_note = models.ForeignKey(ReleaseNote, on_delete=models.CASCADE)
    note = models.CharField(max_length=1000, null=True, blank=True)
    task_size = models.PositiveSmallIntegerField(choices=SizeChoices.choices)
    priority = models.PositiveSmallIntegerField(choices=PriorityChoices.choices)
    task_type = models.PositiveSmallIntegerField(choices=TypeChoices.choices)
    task_domain = models.PositiveSmallIntegerField(choices=DomainChoices.choices)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"اطلاعات تکمیلی {self.release_note}"