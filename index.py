from flask import Flask, render_template
from neo4j import GraphDatabase

# URI del servidor Neo4j
URI = "neo4j+s://48ad4ed7.databases.neo4j.io"

# Credenciales de autenticación
AUTH = ("neo4j", "mHL09XP0RFp9E7_jRSJ5PdB4flgMCr0UNl5FCyUrSYE")

# Inicializar la aplicación Flask
app = Flask(__name__)

# Función para ejecutar la consulta en Neo4j
def execute_query(query):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            result = session.run(query)
            records = [record for record in result]
    return records

# Ruta para mostrar los nodos Hombres y Mujeres en una vista web
@app.route('/')
def index():
    # Consulta para obtener todos los nodos Hombre
    query_hombres = "MATCH (h:Hombre) RETURN h"
    hombres = execute_query(query_hombres)

    # Consulta para obtener todos los nodos Mujer
    query_mujeres = "MATCH (m:Mujer) RETURN m"
    mujeres = execute_query(query_mujeres)

    # Renderizar la plantilla HTML y pasar los datos a la vista
    return render_template('index.html', hombres=hombres, mujeres=mujeres)

if __name__ == '__main__':
    # Ejecutar la aplicación Flask
    app.run(debug=True)
