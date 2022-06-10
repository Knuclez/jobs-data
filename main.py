from distutils.log import error
import pandas as pd
import matplotlib
from pyparsing import Regex

df = pd.read_csv("./Naukri Jobs Data.csv")

#print(df.head)
#print(df.dtypes), queria saber con que trabajaba, imprimir head no me deja ver todas las columnas
#print(df.salary_offered)

df2 = df.salary_offered.str.replace('PA.','', regex = False)
print(df2.value_counts())