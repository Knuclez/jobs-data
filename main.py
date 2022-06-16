from dataclasses import replace
from distutils.log import error
from aux_func import sueldo_a_int
import pandas as pd
import matplotlib

df = pd.read_csv("./Naukri Jobs Data.csv")
#print(df.head)
#print(df.dtypes), queria saber con que trabajaba, imprimir head no me deja ver todas las columnas
#print(df.salary_offered)

serie_salary = df.salary_offered.str.replace('PA.','', regex = False)
#logre modificar un dato string interno. Sueldo tiene rango (min - max), podre partirlo en dos columnas? 

splited = df.salary_offered.apply(lambda x : x.split('-'))
first_column = splited.apply(lambda x: sueldo_a_int(x[0]))
second_column = splited.apply(lambda x: sueldo_a_int(x[1]) if len(x) > 1 else 'NaN')

df['min_salary'] = first_column
df['max_salary'] = second_column

print(df.min_salary.mean())
