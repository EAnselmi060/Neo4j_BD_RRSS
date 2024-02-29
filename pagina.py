from neo4j import GraphDatabase

# URI del servidor Neo4j
URI = "neo4j+s://48ad4ed7.databases.neo4j.io"

# Credenciales de autenticación
AUTH = ("neo4j", "mHL09XP0RFp9E7_jRSJ5PdB4flgMCr0UNl5FCyUrSYE")

# Función para ejecutar la consulta en Neo4j
def execute_query(query):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            result = session.run(query)
            records = [record for record in result]
    return records

# Consulta para obtener todos los nodos Hombre
query_hombres = "MATCH (h:Hombre) RETURN h"
hombres = execute_query(query_hombres)

# Consulta para obtener todos los nodos Mujer
query_mujeres = "MATCH (m:Mujer) RETURN m"
mujeres = execute_query(query_mujeres)

# Imprimir los resultados
print("Nodos Hombres:")
for hombre in hombres:
    print(hombre)

print("\nNodos Mujeres:")
for mujer in mujeres:
    print(mujer)
