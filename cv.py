import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="CV Carlos Carrillo Villavicencio",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

Titulo = """
<head>
  <style>
    h1 { color: black; }
  </style>
</head>
<body>
  <center><h1> Curriculum Vitae</h1><center>
</body>
"""
st.markdown(Titulo, unsafe_allow_html=True)
st.sidebar.title("Carlos Carrillo Villavicencio")
contenido = st.sidebar.radio('Seleccione una opcion',
 ("Perfil profesional",
  "Educación",
  "Experiencia",
  "Idiomas",
  "Manejo de herramientas informáticas",
  "Publicaciones Python",
  "Cursos",
  "Referencias personales"
  ),
  index = 0)

if contenido == "Perfil profesional":

	
	foto = Image.open("Foto.jpg")
	st.image(foto, caption='Ing. Carlos Carrillo Villavicencio')
	st.header("Perfil profesional")
	st.write("""

	Soy ingeniero de petróleos, me considero una persona muy organizada y con gran motivación,
	capaz de adaptarme a cualquier circunstancia y dar siempre lo mejor en cualquier proyecto, al
	mismo tiempo que me esfuerzo por trabajar en equipo y fomentar valores. Soy muy profesional
	y puedo ofrecer mis altos conocimientos de programador, analista de información, estadístico y
	manejo avanzado de base de datos. Me adapto rápidamente a los sistemas de trabajo de
	cualquier empresa, me gusta trabajar en múltiples proyectos y tener la oportunidad de aplicar
	todos mis conocimientos, y al mismo tiempo que me permita desarrollarme profesionalmente.
	Mi paso por la Agencia de Regulación y Control Hidrocarburífero en su Centro de Monitoreo de
	las operaciones hidrocarburíferas me permitió desarrollarme mucho más con mis habilidades de
	análisis de información, y actualmente me dedico de manera independiente a temas de
	desarrollo de Dashboard, Aplicaciones Python en la parte de Backend y Frontend, Machine
	Learning y Ciencia de datos.
	Adoro los retos y no me rindo fácilmente, soy detallista y autodidacta cada día, nunca dejo de
	aprender. Considero que el cambio es un signo de capacidad de superación y creo que siempre
	sería capaz de aportar valor en la empresa en la que me encuentr

		""")
if contenido == "Educación":
	st.write("""
	### **Ingeniero de Petróleos**
	Universidad Central del Ecuador
	""")
	st.write("""
	Número de Registro: 1005-2020-221790 
	""")
	uce = Image.open("uce.png")
	st.image(uce)
	st.write("""
	### **Bachiller Físico Matemático**
	Colegio Nacional Juan de Salinas
	""")
	colegio = Image.open("Colegio.jpg")
	st.image(colegio)
if contenido == "Experiencia":
	st.write("""
	### **ADSA Up-DownStream Analytics**
	- **Cargo:**CEO & Founder
	- **Tiempo :** Febrero 2021 - Actualidad
	- **Dirección:** Av. Gribaldo Miño y Av. Javier Vallarino , Conocoto
	- ** Contactos:** 0998040820
	""")
	st.write("""
	### **Papas Tukas del Valle (Emprendimiento)**
	- **Cargo:**Gerente Administrador
	- **Tiempo :**Noviembre 2019- Actualidad
	- **Dirección:** Av. Ilaló y 8va Tranversal, Valle de los Chillos
	- ** Contactos:** 0996641748
	""")
	st.write("""
	### **Analista de Datos y Desarrollador Python**
	- **Cargo:**Consultor, colaborador, Programador de aplicaciones y desarrollo de
	de Dashboard con principales KPI en Python.
	- **Tiempo :**Julio 2019 – Actualidad
	- **Dirección:** Av. Ilaló y 8va Tranversal, Valle de los Chillos
	- ** Empresas:** Industrias Catedral S.A. , Mekinova
	""")
	st.write("""
	### **Agencia de Regulación y Control Hidrocarburífero (Centro de monitoreo)**
	- **Cargo:**Analista de datos, Programador, Estadístico y Desarrollador Python
	- **Tiempo :**Mayo 2019 – Junio 2020
	- **Dirección:**Armenia Matriz Central
	- ** Contactos:** 023-996-500
	""")

	st.write("""
	### **Royal Prestige**
	- **Cargo:**Vendedor-Sales Person
	- **Tiempo :**Julio 2011 – Agosto 2012
	- **Dirección:**Portugal y Juan de Dios Martínez N34-449, Quito
	- ** Contactos:** 1800 894 1012
	""")
if contenido == "Idiomas":
	st.write(""" 
	### **Español**
	- **Nivel:** Nativo
	- 🟠🟠🟠🟠🟠🟠🟠🟠🟠🟠
	""")
	st.write(""" 
	### **Ingles**
	- **Nivel:** Intermedio
	- 🟠🟠🟠🟠🟠🟠⚪⚪⚪⚪
	""")

if contenido == "Manejo de herramientas informáticas":
	st.write(""" 
	### **Microsoft Word, Excel, Power Point y Access**
	- Programación de Formularios, Macros, Visualización y Base de datos
	- Nivel: Avanzado
	- 🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢
	""")
	st.write(""" 
	### **Power BI, Power Pivot, Power Query**
	- Visualización, DAX y Base de datos
	- Nivel: Avanzado
	- 🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢
	""")
	st.write(""" 
	### **SPSS, Minitab 18 y R-Studio**
	- Pruebas estadísticas, estadística aplicada, descriptiva e inferencial.
	- Nivel: Intermedio - Avanzado
	- 🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪
	""")
	st.write(""" 
	### **Python 3**
	- Desarrollo de aplicaciones, reportes y análisis de bases de datos, Machine Learning, Ciencia de datos.
	- Nivel: Avanzado
	- 🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢
	""")

if contenido == "Publicaciones Python":
	st.write("""
		### **Aplicaciones desarrolladas en Python códigos personales**

		- Downstream Petrolero Análisis del margen de refinación
		- https://margin-refining-app.herokuapp.com/

		""")
	video_1 = open('Video-APP 1 Machine learning en refinerias Python.mp4', 'rb')
	video_bytes_1 = video_1.read()
	st.video(video_bytes_1)

	st.write("""
		- Upstream Petrolero Construcción de pozo tipo J
		- https://well-type-j-app.herokuapp.com/
		""")
	video_2 = open('Video-APP 2  Pozo tipo J Python.mp4', 'rb')
	video_bytes_2 = video_2.read()
	st.video(video_bytes_2)


	st.write("""
		- Downstream Petrolero IPR
		- https://ipr-app.herokuapp.com/
		""")
	video_3 = open('Video-APP 3 IPR App.mp4', 'rb')
	video_bytes_3 = video_3.read()
	st.video(video_bytes_3)
if contenido == "Cursos":
	st.write("""

		|Institucion|Nombre del Curso|Horas|
		|-----------|-|----------------------|
		|Corporación Wolf S.A.|Curso de Análisis y Manejo de información y datos, en sistemas SCADA’s – PLC’s.|24 Horas|
		|Scrum fundation certificate (SFC)|Examen de certificación.|12 Horas|	
		|Women in data science Guayaquil|Participación de taller práctico de análisis de datos con R.|2 Horas|			
		|Robotron Club de Robótica|Introducción a Redes Neuronales con Tensorflow (Python)|6 Horas|	
		|Itoo|Master en Python 3.x Aprende de 0 a EXPERTO con Práctica|5 Horas|
		|Itoo|Programación Básica|3 Horas|
		|Itoo|Inversiones y Trading con Python. De 0 a Experto. Año 2020.|9 Horas|
		|Udemy|Java Programming Complete Beginner to Advanced|2 Horas|
		|Udemy|HTML5 & CSS3 Course: Ultimate and Super Guide (Step by Step)|5 Horas|
		|Udemy|Python, Flask, Framework and Django Course for Beginners|18,5 Horas|
		|Udemy|Advanced & Complete Software Engineering Course with Python|6,5 Horas|
		|Udemy|Programacion en C# desde cero|4,5 Horas|
		|Udemy|Master en Desarrollo – de Cero a Avanzado. Muchos Lenguajes de Programación|29,5 Horas|

	""")
if contenido == "Referencias personales":
	st.write(""" 
	### **PhD. José Flores**
	- Reservoir Engineering Expert
	- SPE Distinguished Lecture
	- +51985065763
	""")
	st.write(""" 
	### **PhD. Rony Parra**
	- Director del Institito de investigaciones FIGEMPA -UCE
	- rmparra@uce.edu.ec
	- +593998261150
	""")
	st.write(""" 
	### **Ing. Janneth Salazar**
	- Personal Assistant abd Supervisor de Presidencia Andes Petroleum
	- Currently Energy Trader Dubai UAE
	- +971505052745
	""")
	st.write(""" 
	### **Ing. Magda Cevallos**
	- Especialista del Centro de Monitoreo y Control Hidrocarburífero
	- magda.cevallos@controlhidrocarburos.gob.ec
	- +593994033611
	""")

qr = Image.open("CV_Qr.png")
st.sidebar.image(qr, caption='Elaborado por Ing. Carlos Carrillo Programador Python')
	
