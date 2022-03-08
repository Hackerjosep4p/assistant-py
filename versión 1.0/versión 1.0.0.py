#import
import time
from subprocess import check_output
import pathlib
import os
import random

#crear funciones
def establecer_archivo(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

def establecer_archivo2(ruta):
    archivo = open(ruta)
    return archivo

def leer_archivo(archivo):
    contenido = archivo.read()
    return contenido

def cerrar_archivo(archivo):
    archivo.close()

def crear_ajuste_bool(ajustestr, apartirDe, linia):
    ajustestr = str(ajustestr)
    apartirDe = int(apartirDe)
    linia = int(linia)
    ajuste = ""

    i = apartirDe
    while i < len(ajustestr):
        ajuste += ajustestr[i]
        i += 1

    ajuste = ajuste.lower()

    if ((ajuste == "true") or (ajuste == " true")) or ((ajuste == "si") or (ajuste == " si")):
        ajuste = True
    elif ((ajuste == "false") or (ajuste == " false")) or ((ajuste == "no") or (ajuste == " no")):
        ajuste = False
    else:
        print("Error en \"" + "\033[1m" + "Ajustes Linia " + str(linia) + "\033[0m" + "\" El ajuste no es correcto, solo puede ser \"Si\", \"No\", \"True\", \"False\".")
        salir(10)
    return ajuste

def crear_ajuste_str(ajustestr, apartirDe, linia):
    ajustestr = str(ajustestr)
    apartirDe = int(apartirDe)
    linia = int(linia)
    ajuste = ""

    i = apartirDe
    while i < len(ajustestr):
        ajuste += ajustestr[i]
        i += 1
    
    if ajuste == "Nombre sin definir":
        print("Error en \"" + "\033[1m" + "Ajustes de usuario Linia " + str(linia) + "\033[0m" + "\" El ajuste no es correcto, has de poner un nombre de usuario valido.")
        salir(10)
    elif ajuste == ajuste.lower():
        print("Error en \"" + "\033[1m" + "Ajustes Linia " + str(linia) + "\033[0m" + "\" El ajuste no es correcto, el nombre ha de empezar por mayuscula.")
        salir(10)
    elif " " in ajuste:
        print("Error en \"" + "\033[1m" + "Ajustes de usuario Linia " + str(linia) + "\033[0m" + "\" El ajuste no es correcto, el nombre de usuario no puede contener espacios.")
        salir(10)
    else:
        pass

    return ajuste

def salir(i):
    time.sleep(i)
    exit()

#crear ruta
ruta = str(pathlib.Path().absolute())
print(ruta)
directory_separator = os.path.sep
ruta_2 = ruta.split(os.path.sep)
if ruta_2[len(ruta_2) - 1] == "versión 1.0":
    pass
else:
    print("Error Fatal")
    salir(5)

#declarar ajustes
archivo = establecer_archivo2(ruta + directory_separator + "ajustes" + directory_separator + "Ajustes de usuario.txt")
ajuste1 = crear_ajuste_str(archivo.readline(), 19, 1)
cerrar_archivo(archivo)

#crear variables
nombre_del_usuario = ajuste1
modo_de_prueba = False
necesidad = -1
insultos = ["abanto", "abrazafarolas", "adufe", "alcornoque", "alfeñique", "andurriasmo", "arrastracueros", "artabán", "atarre", "baboso", "barrabás", "barriobajero", "bebecharcos", "bellaco", "belloto", "berzotas", "besugo", "bobalicón", "bocabuzón", "bocachancla", "bocallanta", "boquimuelle", "borrico", "botarate", "brasas", "cabestro", "cabezaalberca", "cabezabuque", "cachibache", "cafre", "cagalindes", "cagarruta", "calambuco", "calamidad", "caldúo", "calientahielos", "calzamonas", "cansalmas", "cantamañanas", "capullo", "caracaballo", "caracartón", "caraculo", "caraflema", "carajaula", "carajote", "carapapa", "carapijo", "cazurro", "cebollino", "cenizo", "cenutrio", "ceporro", "cernícalo", "charrán", "chiquilicuatre", "chirimbaina", "chupacables", "chupasangre", "chupóptero", "cierrabares", "cipote", "comebolsas", "comechapas", "comeflores", "comestacas", "cretino", "cuerpoescombro", "culopollo", "descerebrado", "desgarracalzas", "dondiego", "donnadie", "echacantos", "ejarramantas", "energúmeno", "esbaratabailes", "escolimoso", "escornacabras", "estulto", "fanfosquero", "fantoche", "fariseo", "filimincias", "foligoso", "folla", "folle", "follo", "fulastre", "ganapán", "ganapio", "gandúl", "gañán", "gaznápiro", "gilipuertas", "giraesquinas", "gorrino", "gorrumino", "guitarro", "gurriato", "habahelá", "huelegateras", "huevón", "imbecil", "lamecharcos", "lameculos", "lameplatos", "lechuguino", "lerdo", "letrín", "lloramigas", "longanizas", "lumbreras", "maganto", "majadero", "malasangre", "malasombra", "malparido", "mameluco", "mamon", "mamporrero", "manegueta", "mangarrán", "mangurrián", "maric", "marik", "mastuerzo", "matacandiles", "meapilas", "melón", "mendrugo", "mentecato", "mequetrefe", "merluzo", "metemuertos", "metijaco", "mindundi", "morlaco", "morroestufa", "muerdesartenes", "orate", "ovejo", "pagafantas", "palurdo", "pamplinas", "panarra", "panoli", "papafrita", "papanatas", "papirote", "paquete", "pardillo", "parguela", "pasmarote", "pasmasuegras", "pataliebre", "patán", 
"pavitonto", "pazguato", "pecholata", "pedorro", "peinabombillas", "peinaovejas", "pelagallos", "pelagambas", "pelagatos", "pelatigres", "pelazarzas", "pelele", "pelma", "percebe", "perrocostra", "perroflauta", "peterete", "petimetre", "picapleitos", "pichabrava", "pillavispas", "piltrafa", "pinchauvas", "pintamonas", "piojoso", "pitañoso", "pitofloro", "plomo", "pocasluces", "polla", "pollopera", "puto", "puta", "quitahipos", "rastrapajo", "rebañasandías", "revientabaules", "ríeleches", "robaperas", "sabandija", "sacamuelas", "sanguijuela", "sinentraero", "sinsustancia", "sonajas", "sonso", "soplagaitas", "soplaguindas", "sosco", "tagarote", "tarado", "tarugo", "tiralevitas", "tocapelotas", "tocho", "tolai", "tontaco", "tonto", "tontucio", "tordo", "tragaldabas", "tuercebotas", "tunante", "zamacuco", "zambombo", "zampabollos", "zamugo", "zángano", "zarrapastroso", "zascandil", "zopenco", "zoquete", "zote", "zullenco", "zurcefrenillos"]
print(ruta + "\n")



print('Hola ' + nombre_del_usuario + ', que tal, ¡yo soy Steve tu asistente!')

while not necesidad == 0:

    print()
    necesidad = input('Dime o preguntame lo que quieras: ')
    print()

    necesidad = necesidad.lower()

    for i in insultos:
        if i in necesidad:
            if not modo_de_prueba:
                necesidad = -1
                check_output(ruta + os.path.sep + "insultos" + os.path.sep + "insultos True.bat", shell=True)
            elif modo_de_prueba:
                necesidad = -1
                check_output(ruta + os.path.sep + "insultos" + os.path.sep + "insultos False.bat", shell=True)
            else:
                necesidad = -1
                print("Error Fatal")
                salir(5)

    if 'adios' in necesidad:
        necesidad = 0
    elif "hola" in necesidad:
        necesidad = 1
    elif "quien eres" in necesidad:
        necesidad = 1
    elif "pagina web" in necesidad:
        necesidad = 2
    elif "paginaweb" in necesidad:
        necesidad = 2
    else:
        necesidad = -2



    if necesidad == -1:
        pass
    elif necesidad == 0:
        print('\nAdios')
        check_output(ruta + os.path.sep + "audios" + os.path.sep + "Adios.mp3", shell=True)
    elif necesidad == 1:
        numeroalazar = random.randint(0, 1)
        if numeroalazar == 0:
            print("Hola " + nombre_del_usuario + ", soy Steve, tu asistente personal, y estoy aqui para ayudarte.")
            check_output(ruta + os.path.sep + "audios" + os.path.sep + "hola,-soy-steve-tu-asistente-personal-y-estoy-aqui-para-ayudarte.mp3", shell=True)
        else:
            print("Hola " + nombre_del_usuario + ".")
    elif necesidad == 2:
        necesidad = input("Que parte de la pagina web quieres abrir (\"" + "\033[1m" + "Inicio" + "\033[0m" + "\", \"" + "\033[1m" + "Download asistent" + "\033[0m" + "\", \"" + "\033[1m" + "Download py" + "\033[0m" + "\", \"" + "\033[1m" + "Insulto" + "\033[0m" + "\", \"" + "\033[1m" + "Error" + "\033[0m" + "\", \"" + "\033[1m" + "Download" + "\033[0m" + "\")? ")

        necesidad = necesidad.lower()

        if "inicio" in necesidad:
            necesidad = 2
        elif "download asistent" in necesidad:
            necesidad = 3
        elif "download py" in necesidad:
            necesidad = 4
        elif "insulto" in necesidad:
            necesidad = 5
        elif "error" in necesidad:
            necesidad = 6
        elif "download" in necesidad:
            necesidad = 7
        else:
            necesidad = -2

        if necesidad == 2:
            print("Abriendo enlace...")
            check_output(ruta + os.path.sep + "audios" + os.path.sep + "Abriendo-enlace.mp3", shell=True)
            check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - INICI.url", shell=True)
        elif necesidad == 3:
            print("Abriendo enlace...")
            check_output(ruta + os.path.sep + "audios" + os.path.sep + "Abriendo-enlace.mp3", shell=True)
            check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - DOWNLOAD-ASISTENT.url", shell=True)
        elif necesidad == 3:
            print("Abriendo enlace...")
            check_output(ruta + os.path.sep + "audios" + os.path.sep + "Abriendo-enlace.mp3", shell=True)
            check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - DOWNLOAD-PY.url", shell=True)
        elif necesidad == 5:
            print("Abriendo enlace...")
            check_output(ruta + os.path.sep + "audios" + os.path.sep + "Abriendo-enlace.mp3", shell=True)
            check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - INSULTS.url", shell=True)
        elif necesidad == 6:
            print("Abriendo enlace...")
            check_output(ruta + os.path.sep + "audios" + os.path.sep + "Abriendo-enlace.mp3", shell=True)
            check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - ERRORS.url", shell=True)
        elif necesidad == 7:
            necesidad = input("Que quieres descargar el \"ASISTENT\" o el \"PY\"")

            necesidad = necesidad.lower()

            if "asistent" in necesidad:
                print("Abriendo enlace...")
                check_output(ruta + os.path.sep + "audios" + os.path.sep + "Abriendo-enlace.mp3", shell=True)
                check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - DOWNLOAD-ASISTENT.url", shell=True)
            elif "py" in necesidad:
                print("Abriendo enlace...")
                check_output(ruta + os.path.sep + "audios" + os.path.sep + "Abriendo-enlace.mp3", shell=True)
                check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - DOWNLOAD-PY.url", shell=True)
            else:
                print("No era una opcion correcta")
                check_output(ruta + os.path.sep + "audios" + os.path.sep + "No-era-una-opción-correcta.mp3", shell=True)
        else:
            print("No era una opcion correcta")
            check_output(ruta + os.path.sep + "audios" + os.path.sep + "No-era-una-opción-correcta.mp3", shell=True)
    elif necesidad == -2:
        print('Lo siento, no puedo hacer eso, aun estoy aprendiendo.')
        check_output(ruta + os.path.sep + "audios" + os.path.sep + "Lo-siento,-no-puedo-hacer-eso,-aun-estoy-aprendiendo.mp3", shell=True)
    else:
        print("\"" + "\033[1m" + "Pequeño error interno" + "\033[0m" + "\"")
        print('Lo siento, no puedo hacer eso, aun estoy aprendiendo.')
        check_output(ruta + os.path.sep + "audios" + os.path.sep + "Lo-siento,-no-puedo-hacer-eso,-aun-estoy-aprendiendo.mp3", shell=True)


print()
#print('Adios')

salir(5)