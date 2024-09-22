Proyecto Urban Grocers

Miguel Eduardo Garcia Lopez 13vo Cohort, 8vo Sprint

El siguiente proyecto aborda una prueba UI como caso de prueba en una aplicacion web Urban Grocers la cual es una aplicacion 
que calcula rutas, modos y ofertas de transporte.

Tecnologias Utilizadas

-Python (lenguaje de programacion utilizado gracias a su versatilidad y facilidad de sintaxis) 
-PyCharm (IDE utilizado por generar un ambiente muy propicio para Python y el cual contiene Pytest  incluido como package listo para descargar) 
-Pytest (framework usado en el testing por facilitar una reporteria de cada prueba y en conjunto) 
-Selenium Webdriver(framework o parte de la Suit de Selenium usado para automatizar pruebas UI en aplicaciones web apoyado mediante drivers para intervenir en navegadores)

Caso de prueba(Validar el pedido de un taxi con ciertas configuraciones)

Ingresar direcciones desde y hacia donde sera el trayecto
Seleccionar el boton adecuado del taxi
Elegir el modo de viaje
Ingresar el numero de telefono
Ingresar el metodo de pago mediante tarjeta
Ingresar un comentario para el conductor
Elegir amenidades del viaje
Elegir comida en el viaje
Solicitar el viaje

La siguiente descripcion habla de como ejecutar las pruebas en el actual proyecto:

Si tienes descargado PyCharm ignora esta instruccion. Si no es el caso entonces descarga la version gratuita de PyCharm y elige la opcion que coincida con tu hardware. Abre la imagen para que veas donde tienes que elegir la version gratuita.
Captura de pantalla 2024-09-03 a la(s) 12 49 38 p m

-Asegurate de descargarlo con las configuraciones recomendadas y de facto. -Extrae el repositorio a travez de git y github -Abre PyCharm y te aparecera una ventana para iniciar un proyecto o abrirlo si ya existe (lo cual es la opcion que vamos a utilizar por que lo extrajiste de Github) -Elige la opcion "open" -Usa el path donde se guardo el repositorio en tu pc y abrelo.

Captura de pantalla 2024-09-03 a la(s) 1 06 00 p m

Para el actual proyecto se descargo "pytest" (si no estan instalados deben instalarse para poderse ejecutar) -En la parte inferior de la interfaz busca el simbolo de packages y haz click -Busca la libreria Pytest -Instalala. Captura de pantalla 2024-09-03 a la(s) 1 12 23 p m

Asegurate de instalar el driver que te ayudara como intermediario entre Selenium y tu navegador (en este caso particular sera Chrome). Aqui el enlace https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/.  Ten en cuenta que las ultimas versiones de Chrome ya viene con su driver incluido y no sera necesario instalarlo.
Al igual que Pytest tambien debe descargarse Selenium, una forma sencilla de hacerlo es siguiendo los mismos pasos para descargar Pytest pero ahora con Selenium.
data.py contiene URL y datos de prueba como variables 

Para asegurar efectividad de la automatizacion la variable urban_routes_URL en data.py debe actualizarse cada cierto tiempo a traves de iniciar el servidor en la plataforma de TripleTen

El archivo main.py se utilizo para generar correr las pruebas. Es un solo caso de prueba con una estructura asi:
Consta de las importaciones necesarias provenientes principalmente de la libreria Selenium y otros archivos .py
Una funcion llamada retrieve_phone_code para obtener un codigo necesario util en el desarrollo de la prueba
Una clase llamada UrbanRoutesPage que tiene como objetivo armar pruebas en base a la arquitectura POM para testing
dicha clase tiene como atributos de clase todas aquellas variables las cuales guardan en una tupla los selectores y elementos de dicha pagina web
posteriormente viene los metodos de clase comanzando con el metodo "init" el cual es un constructor que guarda relacion con el driver 
el resto de los metodos de clase son interraciones propias de Selenium con los atributos de clase.
A continuacion viene la clase TestUrbanRoutes que en si engloba el caso de prueba como tal.
Puede observarse que solo tiene metodos de clase y 2 de ellos (setup_class y teardown_class) tienen decoradores. La principal funcion de estos metodos es abrir y cerrar el navegador en el marco de realizar la prueba completa.
En medio de los 2 metodos de clase mencionados anteriormente estan como metodos tambien todas aquellas etapas de la prueba donde se haran comprobaciones mediante "asserts" para desarollar la prueba o el test completo.


Para ejecutar el programa se debe situar en el main.py (current file) y ejecutar Run (antes de hacer esto solo valida que al lado de todos los metodos de la clase TestUurbanRoutes que comiencen con test.. tengan el simbolo de "play" verde)

Una de las particularidades de Pytest es identificar las funciones que comienzan con test..... asi que las 9 pruebas contenidas en 9 funciones con dicho comienzo son las que deberian ejecutarse por lo tanto obtendras unas reporteria donde 2 casos de prueba fallan y 7 son exitosos.