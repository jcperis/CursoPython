import requests

# Crear una URL para obtener los datos
# Datos de una vivienda
ref_cat = input("Introduce la referencia catastral: ")
url_ref_cat = f"https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC?RefCat={ref_cat}"


# Intentar realizar la petición a la API
try:
    response = requests.get(url_ref_cat)
    response.raise_for_status()
    # Imprimir la respuesta en formato JSON.
    # Aquí podriamos manejar los datos obtenidos a nuestra conveniencia.
    datos = response.json()
    print(datos["consulta_dnprcResult"]["control"])
except Exception as e:
    print(f"Error al acceder a la API: {e}")
