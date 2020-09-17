"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog():
    catalogo={
        "movies":None,
        "production_company":None
    } 
    catalogo['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalogo["moviesId"]=mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMoviesIds)
    
    catalogo["production_company"]=mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareProductionCompanies)
    return catalogo

def newMovie(data):
    data["id"]=int(data["id"])
    data["budget"]=int(data["budget"])
    data["genres"]=data["genres"]
    data["imdb_id"]=data["imdb_id"]
    data["original_language"]=data["original_language"]
    data["original_title"]=data["original_title"]
    data["popularity"]=float(data["popularity"])
    data["production_companies"]=data["production_companies"]
    data["production_countries"]=data["production_countries"]
    data["release_date"]=data["release_date"]
    data["revenue"]=int(data["revenue"])
    data["runtime"]=int(data["runtime"])
    data["spoken_languages"]=data["spoken_languages"]
    data["status"]=data["status"]
    data["tagline"]=data["tagline"]
    data["title"]=data["title"]
    data["vote_average"]=float(data["vote_average"])
    data["vote_count"]=int(data["vote_count"])
    data["production_companies_number"]=int(data["production_companies_number"])
    data["production_countries_number"]=int(data["production_countries_number"])
    data["spoken_languages_number"]=int(data["spoken_languages_number"])

def newProduction(Nombre):
    Company = {'name': "", "movies": None,  "vote_average": 0}
    Company['name'] = Nombre
    Company['movies'] = lt.newList('SINGLE_LINKED', compareMoviesByName)
    return Company

# Funciones para agregar informacion al catalogo

def addCompany(movie, nomb_compania, catalogo):
    Companias=catalogo["production_company"]
    Id=movie["id"]
    Nombre=movie["production_companies"]

    if mp.contain(Companias,Nombre):
        entry=mp.get(Companias,Nombre)
        Company=me.getValue(entry)
    else:
        Company=newProduction(nomb_compania)
        mp.put(Companias,Nombre,Company)
    lt.addLast(Company["movies"],movie)

    Average=Company["vote_average"]
    movieAvg=movie["vote_average"]
    if (movieAvg==0.0):
        Company["vote_average"]=float(movieAvg)
    else:
        n=lt.size(Company["movies"])
        Company["vote_average"]= (Average + float(movieAvg)) / 2

def addMovie(catalogo, dicc):
    lt.addLast(catalogo["movies"],dicc)
    mp.put(catalogo["moviesId"],dicc["id"],dicc) 
    addMovie(catalogo,dicc)




# ==============================
# Funciones de consulta
# ==============================

def detailsSize(catalog):
    return lt.size(catalog['movies'])

# ==============================
# Funciones de Comparacion
# ==============================
def compareMoviesIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareProductionCompanies(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareMoviesByName(keyname, movie):
    
    authentry = me.getKey(movie)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
