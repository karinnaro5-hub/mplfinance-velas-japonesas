#VELAS JAPONESAS FUNCIONAN CON PANDAS, PERO HACE FALTA INSTALAR OTRA LIBRERIA LLAMADA: 
#pip install mplfinance y es para MATPLOTLIB:

import pandas as pd
import mplfinance as mpf

#El profesor o la IA creara un dataframe, 
datos = {
    "D1": {
        "fecha": "2024-01-01",
        "horas": ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
        "open":  [100.0, 102.5, 101.0, 103.0, 104.5, 103.0, 105.0, 106.0, 107.5],
        "high":  [103.0, 104.0, 103.5, 105.0, 106.0, 105.5, 107.0, 108.0, 109.0],
        "low":   [ 99.5, 101.0, 100.0, 102.0, 103.5, 102.0, 104.0, 105.0, 106.5],
        "close": [102.5, 101.0, 103.0, 104.5, 103.0, 105.0, 106.0, 107.5, 108.0],
        "volume":[1200,  1500,  1100,  1800,  1300,  1600,  1400,  1700,  1250],
    },
    "D2": {
        "fecha": "2024-01-02",
        "horas": ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
        "open":  [108.0, 109.0, 110.5, 109.5, 111.0, 112.0, 110.5, 113.0, 114.0],
        "high":  [110.0, 111.5, 112.0, 112.0, 113.5, 113.0, 113.0, 115.0, 116.0],
        "low":   [107.0, 108.5, 109.0, 108.5, 110.0, 111.0, 109.5, 112.0, 113.0],
        "close": [109.0, 110.5, 109.5, 111.0, 112.0, 110.5, 113.0, 114.0, 115.5],
        "volume":[1350,  1600,  1450,  1700,  1550,  1800,  1300,  1900,  1400],
    },
}

#El APEND era un añadido
filas = []
for dia in datos.values():
    for i, hora in enumerate(dia["horas"]):
        filas.append({
            "datetime": pd.Timestamp(f"{dia['fecha']} {hora}"),
            "Open":     dia["open"][i],
            "High":     dia["high"][i],
            "Low":      dia["low"][i],
            "Close":    dia["close"][i],
            "Volume":   dia["volume"][i],
        })

df = pd.DataFrame(filas).set_index("datetime")
df.index.name = "Date"

mpf.plot(
    df,
    type="candle",
      
    style="charles",
    figsize=(12, 6),
    title="Precio de la acción",
    ylabel="Precio en $",
    xlabel="Volumen",
    savefig="imagenes/velas_intradia.png",
)
