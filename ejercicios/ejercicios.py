import pandas as pd

# Lectura del archivo
data = pd.read_csv('users.csv')

# Obtener los nombres de usuarios con edad mayor a 40
data[ data.age > 40 ]
data[ data['age'] > 40 ]

data.query('age > 40')

# Obtener el nombre de los usuarios con una edad mayor a 20 y de sexo femenino.
# En Numpy and -> &
data[ (data.age > 20) & (data.gender == 'female') ]
data[ (data['age'] > 20) & (data['gender'] == 'female') ]

data.query('age > 20 and gender == "female"')

# Obtener todos los usuarios cuyo correo no termine con @example.com
data[ ~ data['email'].str.endswith('@example.com') ]

data.query('~email.str.endswith("@example.com")')

# Obtener el nombre y correo electrónico de todos aquellos usuarios del pais 
# Germany, Finland o Canadá.
data.loc[ (data['country']=="Germany") | (data['country']=="Finland") | (data['country']=="Canada") , ['name', 'email'] ]
data.loc[ (data['country'].isin(["Germany", "Finland", "Canada"])), ['name', 'email'] ]

data.query('country in ("Germany", "Finland", "Canada")')

# Obtener el nombre y correo electrónico de todos los usuarios del sexo femenino 
# del pais Germany.
data.loc[ (data['gender']=="female") & (data['country']=="Germany" ), ['name', 'email'] ]

data.query('gender == "female" and country=="Germany"')[['name', 'email']]

# Obtener la cantidad de usuario de sexo masculino de Canadá
data[ (data['gender']=="male") & (data['country']=="Canada") ]['gender'].count()

# Mostrar en consola la cantidad de hombres y mujeres.
data.groupby(['gender'])['gender'].count()
data.value_counts(data['gender'])

# Mostrar en consola del país con más mujeres
data[ data['gender']=="female" ].groupby('country')['country'].count().sort_values(ascending=False).head(1)

# Obtener los países con más usuarios
data.groupby('country')['country'].count().sort_values(ascending=False).head(5)