## COORDENADAS DEL EPICENTRO DE CADA DISTRITO

distritos = [
    {"district": "Centro", "latitude": 40.415363, "longitude": -3.707398},
    {"district": "Arganzuela", "latitude": 40.398068, "longitude": -3.693734},
    {"district": "Retiro", "latitude": 40.411894, "longitude": -3.676574},
    {"district": "Salamanca", "latitude": 40.427919, "longitude": -3.680877},
    {"district": "Chamartín", "latitude": 40.462428, "longitude": -3.676057},
    {"district": "Tetuán", "latitude": 40.466676, "longitude": -3.698984},
    {"district": "Chamberí", "latitude": 40.436247, "longitude": -3.703830},
    {"district": "Fuencarral-El Pardo", "latitude": 40.515923, "longitude": -3.785586},
    {"district": "Moncloa-Aravaca", "latitude": 40.439883, "longitude": -3.744509},
    {"district": "Latina", "latitude": 40.388981, "longitude": -3.753525},
    {"district": "Carabanchel", "latitude": 40.377818, "longitude": -3.751209},
    {"district": "Usera", "latitude": 40.383553, "longitude": -3.706070},
    {"district": "Puente de Vallecas", "latitude": 40.389491, "longitude": -3.669062},
    {"district": "Moratalaz", "latitude": 40.407251, "longitude": -3.644992},
    {"district": "Ciudad Lineal", "latitude": 40.448431, "longitude": -3.650495},
    {"district": "Hortaleza", "latitude": 40.474457, "longitude": -3.640892},
    {"district": "Villaverde", "latitude": 40.345610, "longitude": -3.695956},
    {"district": "Villa de Vallecas", "latitude": 40.367040, "longitude": -3.612046},
    {"district": "Vicálvaro", "latitude": 40.396584, "longitude": -3.576622},
    {"district": "San Blas-Canillejas", "latitude": 40.428918, "longitude": -3.609064},
    {"district": "Barajas", "latitude": 40.477628, "longitude": -3.579394}
]

## FUNCIONES DE UTILIDAD 

ORIGEN_CSV = "distrito"

def LoadSetCSV(lista):
    '''Función que genera un unico dataframe resultante de la concatenacion de varios csv añadiendo una columna adicional con un
       codigo identificador del origen de los datos.

    Input (lista): Lista de Tuplas (ruta del archivo csv, codigo identificador de los datos)
        
    Output: pd.DataFrame
    
    '''
    import pandas as pd 

    df = pd.DataFrame()    # Los DataFrames que se importan se van concatenando en esta variable.
    for i in lista:
        df_loaded = pd.read_csv(i[0])
        df_loaded[ORIGEN_CSV] = i[1]
        df = pd.concat([df , df_loaded])
    return df