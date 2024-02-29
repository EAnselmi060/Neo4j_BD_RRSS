from flask import Flask, render_template, request
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
    registros_hombres = execute_query(query_hombres)
    
    # Consulta para obtener todos los nodos Mujer
    query_mujeres = "MATCH (m:Mujer) RETURN m"
    registros_mujeres = execute_query(query_mujeres)
    
    # Renderizar la plantilla HTML y pasar los datos de hombres y mujeres
    return render_template('index.html', hombres=registros_hombres, mujeres=registros_mujeres)

@app.route('/bruto')
def bruto():
    # Consulta para obtener todos los nodos Hombre
    query_hombres = "MATCH (n) RETURN n"
    todos = execute_query(query_hombres)
    
    
    # Renderizar la plantilla HTML y pasar los datos de hombres y mujeres
    return render_template('bruto.html', personas=todos)

@app.route('/buscador')
def buscar():
    query = request.args.get('query')  # Obtener la consulta del formulario de búsqueda

    # Consulta Cypher para buscar nodos que coincidan con el nombre o apellido
    query_busqueda = f"MATCH (n) WHERE n.nombre CONTAINS '{query}' RETURN n"
    resultados = execute_query(query_busqueda)

    return render_template('resultados_busqueda.html', personas=resultados, query=query)

@app.route('/cypher')
def cypher():
    query = request.args.get('query')  # Obtener la consulta del formulario de búsqueda
    
    # Verificar si se proporciona una consulta en la URL
    if query:
        # Ejecutar la consulta Cypher y obtener los resultados
        resultados = execute_query(query)
    else:
        # Si no se proporciona una consulta, establecer resultados como una lista vacía
        resultados = []

    # Renderizar la plantilla HTML y pasar los resultados y la consulta
    return render_template('cypher.html', query=query, personas=resultados)

if __name__ == '__main__':
    app.run(debug=True)
