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
