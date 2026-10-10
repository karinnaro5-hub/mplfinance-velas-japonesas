import pandas as pd
import mplfinance as mpf

df = pd.read_csv("acciones_empresa.csv")

#1.2: CONVERTIR LA COLUMNA "Date" AL TIPO DATETIME
df["Date"] = pd.to_datetime(df["Date"])

#1.3: ESTABLECER LA COLUMNA "Date" COMO INDICE DATAFRAME: setear :)
df.set_index("Date", inplace=True)

#Style son los tonos de colores:; 
#suficiente con poner df para que capte todas las columnas y filas del csv
mpf.plot(
    df,
    type = "candle",
    style ="yahoo",
    volume = True,
    xlabel = "días",
    ylabel = "Precios en USD",
    title = "Precios y volumen de una acción",
    
)
