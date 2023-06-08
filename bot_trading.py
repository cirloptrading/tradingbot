import requests
import recopilacion_datos
import json
import numpy as np
from talib import RSI, BBANDS


# Configuración de la API de Binance
API_KEY = 'tu_api_key'
API_SECRET = 'tu_api_secret'
BASE_URL = 'https://api.binance.com'

# Importar la extensión
from extension_trading import trading_automatizado

# Punto de entrada del script
if __name__ == '__main__':
    # Ejecutar el trading automatizado utilizando la extensión
    trading_automatizado()
