#import
import pyttsx3
import time
from subprocess import check_output
import pathlib
import os

#crear funciones
def establecer_archivo(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

def leer_archivo(archivo):
    contenido = archivo.read()
    return contenido

def cerrar_archivo(archivo):
    archivo.close()

def salir():
    time.sleep(5)
    exit()

#declarar pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', '''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0''')

#crear variables
ruta = str(pathlib.Path().absolute())
print(ruta)
directory_separator = os.path.sep
#ruta = str(ruta + directory_separator + "versión 1.0")
ruta_2 = ruta.split(os.path.sep)
if ruta_2[len(ruta_2) - 1] == "versión 1.0":
    pass
else:
    print("Error Fatal")
    salir()
modo_de_prueba = True
necesidad = -1
insultos = ["abanto", "abrazafarolas", "adufe", "alcornoque", "alfeñique", "andurriasmo", "arrastracueros", "artabán", "atarre", "baboso", "barrabás", "barriobajero", "bebecharcos", "bellaco", "belloto", "berzotas", "besugo", "bobalicón", "bocabuzón", "bocachancla", "bocallanta", "boquimuelle", "borrico", "botarate", "brasas", "cabestro", "cabezaalberca", "cabezabuque", "cachibache", "cafre", "cagalindes", "cagarruta", "calambuco", "calamidad", "caldúo", "calientahielos", "calzamonas", "cansalmas", "cantamañanas", "capullo", "caracaballo", "caracartón", "caraculo", "caraflema", "carajaula", "carajote", "carapapa", "carapijo", "cazurro", "cebollino", "cenizo", "cenutrio", "ceporro", "cernícalo", "charrán", "chiquilicuatre", "chirimbaina", "chupacables", "chupasangre", "chupóptero", "cierrabares", "cipote", "comebolsas", "comechapas", "comeflores", "comestacas", "cretino", "cuerpoescombro", "culopollo", "descerebrado", "desgarracalzas", "dondiego", "donnadie", "echacantos", "ejarramantas", "energúmeno", "esbaratabailes", "escolimoso", "escornacabras", "estulto", "fanfosquero", "fantoche", "fariseo", "filimincias", "foligoso", "fulastre", "ganapán", "ganapio", "gandúl", "gañán", "gaznápiro", "gilipuertas", "giraesquinas", "gorrino", "gorrumino", "guitarro", "gurriato", "habahelá", "huelegateras", "huevón", "imbecil", "lamecharcos", "lameculos", "lameplatos", "lechuguino", "lerdo", "letrín", "lloramigas", "longanizas", "lumbreras", "maganto", "majadero", "malasangre", "malasombra", "malparido", "mameluco", "mamon", "mamporrero", "manegueta", "mangarrán", "mangurrián", "mastuerzo", "matacandiles", "meapilas", "melón", "mendrugo", "mentecato", "mequetrefe", "merluzo", "metemuertos", "metijaco", "mindundi", "morlaco", "morroestufa", "muerdesartenes", "orate", "ovejo", "pagafantas", "palurdo", "pamplinas", "panarra", "panoli", "papafrita", "papanatas", "papirote", "paquete", "pardillo", "parguela", "pasmarote", "pasmasuegras", "pataliebre", "patán", 
"pavitonto", "pazguato", "pecholata", "pedorro", "peinabombillas", "peinaovejas", "pelagallos", "pelagambas", "pelagatos", "pelatigres", "pelazarzas", "pelele", "pelma", "percebe", "perrocostra", "perroflauta", "peterete", "petimetre", "picapleitos", "pichabrava", "pillavispas", "piltrafa", "pinchauvas", "pintamonas", "piojoso", "pitañoso", "pitofloro", "plomo", "pocasluces", "pollopera", "puto", "puta", "quitahipos", "rastrapajo", "rebañasandías", "revientabaules", "ríeleches", "robaperas", "sabandija", "sacamuelas", "sanguijuela", "sinentraero", "sinsustancia", "sonajas", "sonso", "soplagaitas", "soplaguindas", "sosco", "tagarote", "tarado", "tarugo", "tiralevitas", "tocapelotas", "tocho", "tolai", "tontaco", "tonto", "tontucio", "tordo", "tragaldabas", "tuercebotas", "tunante", "zamacuco", "zambombo", "zampabollos", "zamugo", "zángano", "zarrapastroso", "zascandil", "zopenco", "zoquete", "zote", "zullenco", "zurcefrenillos"]
print(ruta + "\n")



print('Hola, que tal, ¡yo soy Steve tu asistente!')

while not necesidad == 0:

    necesidad = input('Dime o preguntame lo que quieras: ')
    print()

    necesidad.lower()

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
                salir()

    if 'adios' in necesidad:
        necesidad = 0
    elif "hola" in necesidad:
        necesidad = 1
    elif "quien eres" in necesidad:
        necesidad = 1
    elif "inici" in necesidad:
        necesidad = 2
    elif "download asistent" in necesidad:
        necesidad = 3
    elif "download py" in necesidad:
        necesidad = 4
    elif "insult" in necesidad:
        necesidad = 5
    elif "error" in necesidad:
        necesidad = 6
    elif "download" in necesidad:
        necesidad = 7
    else:
        necesidad = -2



    if necesidad == -1:
        pass
    elif necesidad == 0:
        print('\nAdios')
    elif necesidad == 1:
        print("Hola, soy Steve tu asistente personal y estoy aqui para ayudarte.")
        check_output(ruta + os.path.sep + "audios" + os.path.sep + "hola,-soy-steve-tu-asistente-personal-y-estoy-aqui-para-ayudarte.mp3", shell=True)
    elif necesidad == 2:
        print("Abriendo enlace...")
        check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - INICI.url", shell=True)
    elif necesidad == 3:
        print("Abriendo enlace...")
        check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - DOWNLOAD-ASISTENT.url", shell=True)
    elif necesidad == 3:
        print("Abriendo enlace...")
        check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - DOWNLOAD-PY.url", shell=True)
    elif necesidad == 5:
        print("Abriendo enlace...")
        check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - INSULTS.url", shell=True)
    elif necesidad == 6:
        print("Abriendo enlace...")
        check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - ERRORS.url", shell=True)
    elif necesidad == 7:
        necesidad = input("Que quieres descargar el \"ASISTENT\" o el \"PY\"")
        if "asistent" in necesidad:
            check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - DOWNLOAD-ASISTENT.url", shell=True)
        elif "py" in necesidad:
            check_output(ruta + os.path.sep + "enlaces" + os.path.sep + "ASISTENT PY - DOWNLOAD-PY.url", shell=True)
        else:
            print("Error")
    elif necesidad == -2:
        print('Lo siento, no puedo hacer eso, aun estoy aprendiendo.')
        #check_output(ruta + os.path.sep + "audios" + os.path.sep + "Lo-siento,-no-puedo-hacer-eso,-aun-estoy-aprendiendo.mp3", shell=True)
        engine.say("Lo siento, no puedo hacer eso, aun estoy aprendiendo.")
        engine.runAndWait()
    else:
        print('Lo siento, no puedo hacer eso, aun estoy aprendiendo.')
        #check_output(ruta + os.path.sep + "audios" + os.path.sep + "Lo-siento,-no-puedo-hacer-eso,-aun-estoy-aprendiendo.mp3", shell=True)
        engine.say("Lo siento, no puedo hacer eso, aun estoy aprendiendo.")
        engine.runAndWait()


print()
print('Adios')

salir()