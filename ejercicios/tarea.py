import pandas as pd 
import numpy as np
from pandas.core import groupby

data = pd.read_csv('users.csv')

# Mostrar en consola el nombre de todos los usuarios que no poseen un correo
data[ ~data['email'].notnull() ]['name']

# Listar el nombre y el correo del usuario más joven de Canadá
data.loc[ data['country']=="Canada", ['name', 'email', 'age']].sort_values('age').head(1)

# Listar el nombre y correo de los usuarios más jovenes de Germany y Canadá.
data.loc[ ((data['country']=="Germany") | (data['country']=="Canada")), ['name', 'email', 'age']].sort_values('age').head(2)

# Listar los 5 paises con mayor cantidad de usuarios.
data.groupby('country')['country'].count().sort_values(ascending=False).head(5)

# Obtener el país con más usuarios
data.groupby('country')['country'].count().sort_values(ascending=False).head(1)

# Obtener el país con más usuarios cuya edad sea mayot a 50.
data.loc[ (data['age']==50), ['country', 'age'] ].groupby('country')['country'].sum().head(1)

# Obtener la suma total de todos los usuarios de Canadá y Germany.
data[ (data['country']=="Germany") | (data['country']=="Canada")]['country'].count()

# Mostrar en consola la cantidad de países en el data set.
data['country'].unique().size

# Obtener el promedio de edad de cada uno de los países.
data.groupby('country')['country', 'age'].mean('age')

# Monstrar en consola el país con más hombres.
data[ data['gender']=="male" ].groupby('country')['gender'].count().sort_values(ascending=False).head(1)