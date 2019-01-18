from django.db import models


class SalaryOverYears(models.Model):
    workedYears = models.IntegerField()
    salaryBrutto = models.IntegerField(null=True)

    def __str__(self):
        return 'Worked years: ' + str(self.workedYears) + ' Salary Brutto ' + str(self.salaryBrutto)
