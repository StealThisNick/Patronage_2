import pandas as pd
from pathlib import Path
import os
from django_pandas.io import read_frame
import numpy as np
import statsmodels.formula.api as smf
from .models import SalaryOverYears


def import_csv_to_model(path_to_file):
    salary_path = Path(path_to_file) 
    SalaryOverYears.objects.all().delete()
    df = pd.read_csv(salary_path, na_values=[' '])
    for idx, row in df.iterrows():
        local_salary_brutto = row['salaryBrutto']
        if pd.isna(local_salary_brutto):
            local_salary_brutto = None
        x = SalaryOverYears(id=idx, workedYears=row['workedYears'], salaryBrutto=local_salary_brutto)
        x.save()


def linary_estimate_salary_over_year(model_linary):
    model_to_frame = model_linary.objects.all()
    query_values = list(model_to_frame.values_list('workedYears', 'salaryBrutto'))
    df = pd.DataFrame.from_records(columns=['workedYears', 'salaryBrutto'],data=query_values)
    filtred_df = df[pd.notna(df['salaryBrutto'])]
    worked_years = filtred_df['workedYears']
    salary_brutto = filtred_df['salaryBrutto']
    model1 = smf.ols(formula='salaryBrutto~workedYears', data=filtred_df)
    res = model1.fit(q=.5)
    pred_value = res.params.get_values()
    salary_pred = res.predict(pd.DataFrame(worked_years))
    filtred_df = filtred_df.assign(
        salary_pred=pd.Series(salary_pred).values)
    return filtred_df

if __name__ == "__main__":
    import_csv_to_model('salary.csv')
    linary_estimate_salary_over_year(SalaryOverYears)
