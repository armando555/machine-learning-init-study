import pandas as pd
df = pd.read_csv("../data/articles.csv")
print(df.tail(20))
#traspuesta la matriz
print(df.describe().T)
#Convertir data en json
df.to_json("data_out.json")

#.info() me trae data como usao de memoria, los tipos de datos que hay, etc
print(df.info(show_counts=True, memory_usage=True, verbose=True))

#shape df.shape # Get the number of rows and columns
#df.shape[0] # Get the number of rows only
#df.shape[1] # Get the number of columns only

print(df.shape)
print(df.shape[0])
print(df.shape[1])

# .columns  returns the column names in the form of an Index object
print(df.columns)
#and convert it to list
print(list(df.columns))


#.copy() makes a copy of the dataframe
df2 = df.copy()
# modificar de la fila 2 a la 5 la columna article por None
#puedo traer filas por condiciones o etiquetas con .loc() .iloc(integer location)
df2.loc[2:5,'Article'] = None

print(df2.head(n=7))

#retorna un dataframe mapeando qué atributos están en nan o none  o null
print(df2.isnull().head(7))

#ahora quiero contarlos
print(df2.isnull().head(7).sum())


# obtener toda una columna o varias
print(df['Article'])
print(df[['Article','Quantity']])

#traer rows ya sea 1 o varias
print(df[df.index==1])
print(df[df.index.isin(range(2,10))])


# CLEANING DATA WITH PANDAS

#esto es viable cuando sé que la porción de data a eliminar es poca
df3 = df.copy()
df3 = df3.dropna()
print(df.shape)
print(df3.shape)

#El axis argumento le permite especificar si está eliminando filas o columnas con valores faltantes. El valor predeterminado axis elimina las filas que 
# contienen NaN. Úselo axis = 1para eliminar las columnas con uno o más valores de NaN. Además, observe cómo estamos usando el argumento inplace=True 
# que le permite omitir guardar la salida .dropna()en un nuevo DataFrame.  

df3 = df.copy()
df3.dropna(inplace=True, axis=1)
print(df3.head())


#También puede eliminar filas y columnas con valores faltantes estableciendo el howargumento en'all'
df3 = df.copy()
df3.dropna(inplace=True, how='all')
print(df3.head())


#REEMPLAZAR VALORES FALTANTES

df3 = df.copy()
#poner un valor por defecto ya sea un promedio, mediana o cosas así
mean_value = "test"
# llenar los datos faltantes con ese valor por defecto
df3 = df3.fillna(mean_value)
print(df3.head())

# DATOS DUPLICADOS

#aca duplico los datos pa probar
df3 = pd.concat([df, df])
print(df3.shape)

#elimino los duplicados
df3 = df3.drop_duplicates()
print(df3.shape)


# CAMBIAR NOMBRE A LAS COLUMNAS
df3.rename(columns = {'Article':'Arti'}, inplace = True)
print(df3.head())


# CREAR COLUMNA A PARTIR DE EXISTENTES

# este es un ejemplo pero no tnego el CSV  para probarlo
#df2['Glucose_Insulin_Ratio'] = df2['Glucose']/df2['Insulin']
#df2.head()

# Además puedo agruparlos
#print(df.groupby('Quantity').mean())


#   GRAFICAR EN PANDAS
df[["Quantity"]].plot.line()

