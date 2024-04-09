"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
csv.field_size_limit(2147483647) 

def new_controller():
    """
    Crea una instancia del modelo
    """
    tipo_estructura = input("Ingrese el tipo de estructura (1 para CHAINING o 2 para PROBING): ")
    factor_carga = input("Ingrese el factor de carga (1, 2, 3, o 4 para CHAINING; 1, 2, 3, o 4 para PROBING): ")
    num_elementos = int(input("Ingrese la cantidad de elementos iniciales: "))

    control = {
        'model': None
    }

    control['model'] = model.new_data_structs(tipo_estructura, factor_carga, num_elementos)
    return control


# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    data_structs = control['model'] 
    message = """        Ingrese 1 si quiere cargar una muestra pequeña de los datos.
        Ingrese 1 si quiere cargar el 10 porciento de los datos. 
        Ingrese 2 si quiere cargar el 20 porciento de los datos.
        Ingrese 3 si quiere cargar el 30 porciento de los datos 
        Ingrese 4 si quiere cargar el 50 porciento de los datos.
        Ingrese 5 si quiere cargar el 80 porciento de los datos 
        Ingrese 6 si quiere cargar TODOS los datos. \n"""
    data_size = int(input(message))

    if data_size == 1:
        file = "10-por"
    elif data_size == 2:
        file = "20-por"
    elif data_size == 3:
        file = "30-por"
    elif data_size == 4:
        file = "50-por"
    elif data_size == 5:
        file = "80-por"
    elif data_size == 6:
        file = "large"

    jobs_by_date = load_job_by_date(data_structs, file)
    employment_type = load_employment_type(data_structs, file)
    return jobs_by_date, employment_type


def load_job_by_date(data_structs, file):

    input_file = csv.DictReader(open(cf.data_dir + f"{file}-jobs.csv", encoding='utf-8'),delimiter=";")
    for job in input_file:
        model.add_job_by_date(data_structs, job)
    return model.data_size(data_structs["jobs_by_date"])

def load_employment_type(data_structs, file):

    input_file = csv.DictReader(open(cf.data_dir + f"{file}-employments_types.csv", encoding='utf-8'),delimiter=";")
    for employment_type in input_file:
        model.add_employment_type(data_structs, employment_type)
    return model.data_size(data_structs["employments_types"])





# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
