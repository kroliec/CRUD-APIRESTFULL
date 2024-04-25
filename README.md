# CRUD-CON-PYTHON-FLASK-MONGODB-Y-RESTFUL-API
## Integrantes
- Sting Buritica Londoño
- Bryan Cardona Valencia
- Juan Felipe Salazar Muñoz
## Marco Teorico
### Python
Python es un lenguaje de programación utilizado en desarrollo de aplicaciones web, desarrollo de software, la ciencia de datos y machine learning. Utilizado popularmente por su eficiencia y facilidad de aprender. 

Python posee ciertas características:  

Es un lenguaje de tipeado dinámicamente 
Es un lenguaje orientado a objetos
Fácil de utilizar 
Lenguaje interpretado

Python posee algunos beneficios, de entre muchos se destacan los siguiente: 
Los desarrolladores pueden leer y comprender fácilmente los programas de Python debido a su sintaxis básica.
Python permite que los desarrolladores sean más productivos, ya que pueden escribir un programa de Python con menos líneas de código en comparación con muchos otros lenguajes.
Los desarrolladores pueden utilizar Python fácilmente con otros lenguajes de programación conocidos, como Java, C y C++.
Python se puede trasladar a través de diferentes sistemas operativos de computadora, como Windows, macOS, Linux y Unix.

Origen de la información: [¿Que es Python?](https://aws.amazon.com/es/what-is/python/).
### Flask
Es un micro framework de python para desarrollar aplicaciones web, lo que quiere decir que con esta herramienta se pueden crear aplicaciones pequeñas, mediana y/o grandes con poco código, ya que flask proporciona un enrutador URL y herramientas básicas para manejar solicitudes HTTP, a su vez flask da libertad al desarrollador de elegir las bibliotecas y extensiones que mejor se ajusten a sus necesidades. 

Flask ofrece una gran cantidad de flexibilidad y personalización, lo que lo hace adecuado tanto para proyectos pequeños o aplicaciones de gran escala. 

Algunas de sus ventajas son: 

- Fácil de usar 
- Flexibilidad 
- Pequeño y ligero
- Bajo nivel de abstracción 
- Fácil de integrar a otro servicios

Origen de la información: [Flask](https://www.youtube.com/watch?v=W-SfC_V7P6o). 

### MongoDB
Es un gestor de bases de datos en la nube que cuenta con una arquitectura NoSQL, esto quiere decir que es una base de datos no relacional. Las bases de datos No relacionales permiten el manejo de grandes cantidades de datos dejando de lado el estándar basado en una estructura base la cual seguir, esta arquitectura está orientada a documentos, a diferencia de las bases de datos relacionales como Mysql o postgres que utilizan tablas y columnas para almacenar la información, MongoDB hace uso de colecciones y documentos para almacenar grandes cantidades de información.

#### Atlas
Para utilizar los servicios en la nube de mongoDB es necesario utilizar MongoDB Atlas, por medio de esta plataforma se pueden administrar de forma más detallada y eficiente las bases de datos que hayamos creado en la herramienta para escritorio MongoDB compass, la cual es utilizada por aquellas personas que prefieren un entorno de trabajo más visual, MongoDB también cuenta con su propia terminal en la cual se pueden realizar la creación y administración de las bases de datos, cabe resaltar que esta terminal también se puede instalar de forma independiente en caso de no querer instalar MongoDB Compass.

Tanto MongoDB como MongoDB Compass como MongoDB shell se pueden descargar por medio de la página oficial, está disponible tanto para Windows como para Linux y Mac.

Pag MongoDB: [MongoDB.com](https://www.mongodb.com/es).

### Replication MongoDB
Consiste en copias de seguridad realizadas por conjuntos de réplicas o servidores que son administrados por nodos, los cuales se dividen en dos grupos, el nodo primario y los nodos secundarios. Las copias de seguridad se realizan en diferentes servidores, esto permite asegurar los datos de la base principal en caso de que haya algún tipo de error.

El nodo primario es el encargado de administrar las copias de seguridad existentes, en caso de que este nodo falle, la administración pasa al nodo secundario para que este continúe con la tarea y así se mantenga la información actualizada en cada momento entre la base de datos principales y las copias existentes. Al momento en que el nodo secundario toma el papel de administración este pasa a ser el nuevo nodo primario.

### API

### REST

### Restful API
La API RESTful es una interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet. La mayoría de las aplicaciones para empresas deben comunicarse con otras aplicaciones internas o de terceros para llevar a cabo varias tareas. Por ejemplo, para generar nóminas mensuales, su sistema interno de cuentas debe compartir datos con el sistema bancario de su cliente para automatizar la facturación y comunicarse con una aplicación interna de planillas de horarios. Las API RESTful admiten este intercambio de información porque siguen estándares de comunicación de software seguros, confiables y eficientes.
La función básica de una API RESTful es la misma que navegar por Internet. Cuando requiere un recurso, el cliente se pone en contacto con el servidor mediante la API. Los desarrolladores de API explican cómo el cliente debe utilizar la API REST en la documentación de la API de la aplicación del servidor. A continuación, se indican los pasos generales para cualquier llamada a la API REST: 

1. El cliente envía una solicitud al servidor. El cliente sigue la documentación de la API para dar formato a la solicitud de una manera que el servidor comprenda.
2. El servidor autentica al cliente y confirma que este tiene el derecho de hacer dicha solicitud.
3. El servidor recibe la solicitud y la procesa internamente.
4. Luego, devuelve una respuesta al cliente. Esta respuesta contiene información que dice al cliente si la solicitud se procesó de manera correcta. La respuesta también incluye cualquier información que el cliente haya solicitado.

## Marco Metodologico

### Python
Para instalar python se debe descargar desde su pagina principal [Python.org](https://www.python.org/downloads/). 
Posterior a su descarga, ejecutamos el instalador y permitimos el uso de la variable PATH el cual es una lista de directorios que el sistema operativo busca para encontrar ejecutables cuando se emite un comando desde la línea de comandos o el terminal., tras su instalación, abrimos nuestro editor de texto en este caso Vscode y procedemos a intalar la extencion de Python. 
### Flask
Para instalar flask en vscode debemos permitir el uso de scripts por medio de la terminal de powershell en donde se debe usar el comando:

```
Set-ExecutionPolicy RemoteSigned
```
Posterior a esto se debe ingresar a nuestro editor de texto Vscode, para usar el comando: 
```
pip install flask
```
Hay que tener en cuenta que, para que el comando sea reconocido, es necesario tener instalado python en el dispositivo y tener instaladas las extenciones necesarias de python en Visual Studio code.

En el siguiente comando vamos a lanzar un archivo index.html el una carpeta llamada templates, ya que la función (render_template) buscara dicho archivo en una carpeta llamada de igual forma es decir template: 

```
@app.route('/')
def home():
    return render_template('index.html')
```

### MongoDB
Para que la variable en la que realizamos la conexion con MongoAtlas funcione debemos instalar pymongo en la terminal de vscode con el siguiente comando:
```
pip install pymongo
```
Y posterior a esto procedemos a instalar el certifi con el siguiente comando: 
```
pip install certifi
```
y por ultimo utilizamos el comando: 
```
pip install pymongo[srv]
```
Luego de realizar la instalacion se debe importar el Mongoclient desde pymongo e importar el certifi que nos permite realizar la conexion con la base de datos como se  muetra en el siguiente comando: 

```
from pymongo import MongoClient
import certifi

MONGO_URI='mongodb+srv://shadow:sololeveling@clustersockets.7tvakqr.mongodb.net/'
ca=certifi.where()

def dbConnection():
    try:
        client=MongoClient(MONGO_URI, tlsCAFile=ca)
        db=client["db_crud"]
    except ConnectionError:
        print("Error de conexion con la base de datos")
    return db

```
En el siguiente comando nos conectamos a nuestra base de datos, pero si la base de datos no existe esta es creada automaticamente con el nombre (db_crud)

### Restful API

## Bibliografia
