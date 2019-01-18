from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .trymybest import import_csv_to_model, linary_estimate_salary_over_year
from .models import SalaryOverYears
import pandas as pd


def index(request):
    return render(request, 'machine/index.html', {})


def import_defult_value(request):
    import_csv_to_model('salary.csv')
    return HttpResponseRedirect(reverse('machine:index'))


def detail_view(request):
    sample = linary_estimate_salary_over_year(SalaryOverYears)
    contex = sample.to_dict()
    contex_new = []
    for i in range(len(contex['workedYears'])):
        contex_new.append({'workedYears':contex['workedYears'][i],
                            'salaryBrutto':contex['salaryBrutto'][i],
                            'salaryPred':contex['salary_pred'][i]})
    return render(request, 'machine/detail.html', {'contex': contex_new})
