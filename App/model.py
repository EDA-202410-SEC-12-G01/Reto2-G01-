﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import date 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(tipo_estructura, factor_carga, num_elementos):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    
    data_struct = {"jobs_by_date":None,
                    "employments_types":None,
                    "multilocations":None,
                    "skills":None}

    map_type = 'CHAINING' if tipo_estructura == '1' else 'PROBING'


    if map_type == 'CHAINING':
        if factor_carga == '1':
            factor_carga = 2  
        elif factor_carga == '2' :
            factor_carga = 4
        elif factor_carga == '3' :
            factor_carga = 6 
        else: factor_carga = 8

    elif map_type == 'PROBING':
        if factor_carga == '1':
            factor_carga = 0.1
        if factor_carga == '2':
            factor_carga = 0.5
        if factor_carga == '4':
            factor_carga = 0.7
        else: factor_carga = 0.9
        
    data_struct["jobs_by_date"] = mp.newMap(numelements=num_elementos, maptype=map_type, loadfactor=factor_carga)
    data_struct["employments_types"]  = mp.newMap(numelements=num_elementos, maptype=map_type, loadfactor=factor_carga)
    data_struct["multilocations"]  = mp.newMap(numelements=num_elementos, maptype=map_type, loadfactor=factor_carga)
    data_struct["skills"]  = mp.newMap(numelements=num_elementos, maptype=map_type, loadfactor=factor_carga)
    
    return data_struct

##ADD_DATA##
def add_job_by_date(data_struct,data):
    job= new_job_by_date(data)
    mp.put(data_struct["jobs_by_date"],data["published_at"],job)
    return data_struct

def add_employment_type(data_struct,data):
    employment_type= new_employment_type(data)
    mp.put(data_struct["employments_types"],data["id"],employment_type)
    return data_struct






##NEW DATA##
def new_job_by_date(data):
    job = {"title":data["title"],
           "street":data["street"],
           "city":data["city"],
           "country_code":data["country_code"],
           "address_text":data["address_text"],
           "marker_icon":data["marker_icon"],
           "workplace_type":data["workplace_type"],
           "company_name":data["company_name"],
           "company_url":data["company_url"],
           "company_size":data["company_size"],
           "experience_level":data["experience_level"],
           "published_at":data["published_at"],
           "remote_interview":data["remote_interview"],
           "open_to_hire_ukrainians":data["open_to_hire_ukrainians"],
           "id":data["id"],
           "display_offer":data["display_offer"]}
    return job

def new_employment_type(data):
    employment_type={"type":data["type"],
                     "id":data["id"],
                     "currency_salary":data["currency_salary"],
                     "salary_from":data["salary_from"],
                     "salary_to":data["salary_to"]}
    return employment_type

def new_multilocation(data):
    multilocation={"city":data["city"],
                     "street":data["street"],
                     "id":data["id"],}
    return multilocation

def new_skill(data):
    skill={"name":data["name"],
           "level":data["level"],
           "id":data["id"]}
    return skill

def data_size(data_structs):
    return mp.size(data_structs)





def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
