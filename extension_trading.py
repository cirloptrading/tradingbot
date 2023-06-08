# Importar las funciones necesarias del código principal
from bot_trading import obtener_criptomonedas, obtener_historial, analizar_senales, invertir

# Configurar los parámetros de la estrategia de trading
umbral_rsi_compra = 30
umbral_rsi_venta = 70
umbral_bandas_compra = -2
umbral_bandas_venta = 2

# Obtener todas las criptomonedas disponibles en Binance
criptomonedas = obtener_criptomonedas()

if criptomonedas:
    # Iterar sobre cada criptomoneda y realizar el análisis y la inversión
    for cripto in criptomonedas:
        # Obtener el historial de precios de la criptomoneda específica
        historial = obtener_historial(cripto, '1h', 100)

        if historial:
            # Analizar las señales en función del análisis técnico
            senales = analizar_senales(historial)

            # Tomar decisiones de inversión basadas en las señales
            for i, senal in enumerate(senales):
                # Calcular el RSI y las bandas de Bollinger
                rsi = calcular_rsi(historial, i)
                bandas_superior, _, bandas_inferior = calcular_bollinger_bands(historial, i)

                # Tomar decisiones basadas en el análisis técnico y las señales
                if senal == 'COMPRA' and rsi < umbral_rsi_compra and historial[i][4] < bandas_inferior * umbral_bandas_compra:
                    invertir(cripto, 100)
                    print(f"Señal {i+1}: Se realizó una compra de {cripto}")

                if senal == 'VENTA' and rsi > umbral_rsi_venta and historial[i][4] > bandas_superior * umbral_bandas_venta:
                    invertir(cripto, -100)
                    print(f"Señal {i+1}: Se realizó una venta de {cripto}")

                if senal == 'HOLD':
                    print(f"Señal {i+1}: Mantener posición en {cripto}")
        else:
            print(f"No se pudo obtener el historial de precios de {cripto}.")
else:
    print("No se pudo obtener la lista de criptomonedas disponibles.")
