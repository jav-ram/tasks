# asumir conexion

import sqlite3
connection = sqlite3.connect("Buses.db")

db = connection.cursor()

db.execute("SELECT * FROM employee") 

def task2(idEscuela, lat, lon, distancia):
    query = ""
    select = " SELECT p.id FROM Parent as p, School as s, Student as st, RouteStop as rs "
    where = " WHERE s.id == " + idEscuela + " AND st.schoolid == s.id AND rs.studentid == st.id AND rs.latitude == " +lat+ " AND st.longitude == " + lon
    group = " GROUP BY p.id"
    query = select + where + group + ";"
    return db.execute(query) 

def task3():
    query1 = ""
    query2 = ""
    select = "SELECT DISTINCT st.id FROM Student as st, School as s, RouteStop as rs, Route as r "
    where =  "WHERE st.id == rs.studentid AND rs.id == r.routeid AND r.schoolid == s.id"
    #obtengo los estudiantes que si tienen paradas de rutas de su escuela
    query1 = select + where + ";"

    #obtengo todos los estudiantes
    select = "SELECT st.id FROM Student as s"
    query2 = select

    resultado = db.execute(query2 + "WHERE st.id NOT IN (" + query1 + ") ;")

