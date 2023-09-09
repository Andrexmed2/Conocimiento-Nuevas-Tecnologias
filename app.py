FLAG = True
USUARIOS = []
BICICLETAS = [
    {
        id: 1,
        "nombre": "Cross",
        "marca": "GW"
    },
    {
         id: 2,
        "nombre": "Cross",
        "marca": "SHIMANO"
    }
    ]

BICICLETASPRESTADAS = []

def registrarUsuario():
    print("\n *** Registrar usuario ***\n")
    identificacion = input("Ingrese identificacion: ")
    nombre = input("Ingrese el nombre: ")
    email = input("Ingrese el email: ")
    password = input("Ingrese el password: ")
    
    newUser = {
        "identificacion": identificacion,
        "nombre": nombre,
        "email": email,
        "password": password
    }
    USUARIOS.append(newUser)
    print("\n Registro Exisoto! \n")
    
def obtenerUsuarios():
    if len(USUARIOS) == 0:
        print("\nNO HAY USUARIOS EN LA LISTA!\n")
    else:
        print("\n USUARIOS EN LA LISTA!\n")
        for user in USUARIOS:
            print(f"Identificcion: {user['identificacion']}\nNombre: {user['nombre']}\nEmail: {user['email']}\n")

def prestarBicicleta():
    print("\nIngrese las credenciales de acceso\n")
    idToLogin = input("Id To Login: ")
    passw = input("Pass To Login: ")
    
    for user in USUARIOS:
        if user["identificacion"] == idToLogin and user["password"] == passw:
            print("El usuario existe")
            usuarioAprobadoParaPrestamo(idToLogin)
            break
        else:
             print("El usuario NO existe ")
             break
             
            
def usuarioAprobadoParaPrestamo(idPersona):
    print("\n LISTA BICICLETAS \n")
    for bici in BICICLETAS:
        print(f"Identificacion BICI: {bici[id]}\nNombre bici: {bici['nombre']}\nMarca: {bici['marca']}\n")
    
        opcion2 = int(input("Escoja el id de la bicicleta"))
        origin = input("Origen")
        destino = input("Destino")
            
        if opcion2 == bici[id]:
            print("Bicicleta valida")
            newPrestamo = {
                "id_persona": idPersona,
                "idBicicleta": bici[id],
                "origen": origin,
                "destino": destino
            }
            BICICLETASPRESTADAS.append(newPrestamo) 
            break   
        else:
            print("No selecciono una bici valida")
            break
            
def bicisPrestadas():
    if len(BICICLETASPRESTADAS) == 0:
        print("\nNO HAY BICIS PRESTADAS EN LA LISTA!\n")
    else:
        print("\n BICIS PRESTADAS EN LA LISTA!\n")
        for bicis in BICICLETASPRESTADAS:
            print(f"Identificacion Persona: {bicis['id_persona']}\nId Bicicleta: {bicis['idBicicleta']}\nOrigen: {bicis['origen']}\nDestino: {bicis['destino']}\n")
                    
while FLAG:
    print("***1. REGISTRO DE USUARIO: ")
    print("***2. LISTAR USUARIOS: ")
    print("*** 3. PRESTAR BICICLETA: ")
    print("*** 4. BICICLETAS PRESTADAS: ")
    print("*** 5. CERRAR: ")
    print("*** PRESTAR BICILETA ***")
    opcion = int(input("Seleccione una opcion: "))
    
    if(opcion == 1):
        registrarUsuario()
    elif(opcion == 2):
        obtenerUsuarios()
    elif(opcion == 3):
        prestarBicicleta()
    elif(opcion == 4):
        bicisPrestadas()
    elif(opcion == 5):
        FLAG = False
        print("Good bye")
    else:
        print("*** OPCION INVALIDA !!! ***")