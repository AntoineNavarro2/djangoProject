from django.db import models
from datetime import datetime

# Create your models here.
class Cursus(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        default='aucun'
)
    year_from_bac = models.SmallIntegerField(
        help_text ="year since le bac",
        verbose_name="year",
        blank=False,
        null=True,
        default=0
)
    scholar_year = models.CharField(
        max_length=9,
        blank=False,
        null=True,
        default='0000-00001'
)
    class Meta:
        verbose_name_plural = 'Cursus'
    def __str__(self):
        return '{} {}: {}'.format(self.name,self.year_from_bac,self.scholar_year)

class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False
)
    birth_date = models.DateField(
        verbose_name='date of birth',
        blank=False,
        null=True
)
    last_name = models.CharField(
        verbose_name="lastname",
        help_text="last name of the student",
        blank=False, # pas de champ vide
        null=False, # pas de champ null (a conjuguer avec default
        default="??",
        max_length=255, # taille maximale du champ
)
    phone = models.CharField(
        verbose_name="phonenumber",
        help_text="phone number of the student",
        blank=False, # pas de champ vide
        null=False, # pas de champ null (a conjuguer avec default
        default="0123456789",
        max_length=10, # taille maximale du champ
)
    email = models.EmailField(
        verbose_name="email",
        help_text="phone number of the student",
        blank=False, # pas de champ vide
        null=False, # pas de champ null (a conjuguer avec default
        default="x@y.z",
        max_length=255, # taille maximale du champ
)
    comments = models.CharField(
        verbose_name="comments",
        help_text="some comments about the student",
        blank=True,
        null=False, # pas de champ null (a conjuguer avec default
        default="",
        max_length=255, # taille maximale du champ
)
    cursus = models.ForeignKey(
        Cursus,
        on_delete=models.CASCADE, # necessaire selon la version de Django
        null=True
)
    def __str__(self):
        return '{} {}: {}'.format(self.first_name,self.last_name,self.id)
class Presence(models.Model):
    reason = models.CharField(
        verbose_name="Reason",
        help_text="reason of missing",
        max_length= 80,
        blank=False,
        null=False
    )
    isMissing = models.BooleanField(
        verbose_name="isMissing",
        null=False,
        blank=False,
        help_text="The student is missing or no",
        default = True
    )
    date = models.DateTimeField(
        verbose_name='Date of Student Missing',
        default=datetime.now(),
        blank=False,
        null=False
    )
    start_time = models.TimeField(
        help_text="Start of the missing",
        default="00:00"

    )
    stop_time = models.TimeField(
        help_text="End of the missing",
        default="00:00"

    )

    student = models.ForeignKey(
        Student,
        related_name="Student",
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=False
    )