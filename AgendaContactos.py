def menu():
    print("Agenda telefonica")
    print("1.-Ingresar nuevo contacto")
    print("2.-buscar contacto")
    print("3.-Modificar contacto")
    print("4.-Mostrar agenda")
    print("5.-Eliminar contacto")
    print("6.-salir")


def mod():
    print("Modificar")
    print("1.-Primer nombre")
    print("2.-Segundo nombre")
    print("3.-Apellido paterno")
    print("4.-Apellido materno")
    print("5.-Telefono celular")
    print("6.-Telefono de casa")
    print("7.-Perfil de facebook")
    print("8.-Correo electronico")
    print("9.-Salir")

telefonoscel={}
telefonoscasa={}
perfilfacebook={}
pnombres={}
segunnombres={}
correos={}
apellidop={}
apellidom={}
opcionmenu=0
contacto=[]
contador=0
while opcionmenu !=6:
    menu()
    opcionmenu= int(input("ingresa una opcion:"))
    if opcionmenu==1:#agregar contacto
        contador=contador+1
        print("ingresa datos del contacto:")
        print("id del contacto: ",contador)
        nom=input("Ingrese el primer nombre: ")
        snom=input("Ingrese el segundo nombre: ")
        apep=input("Ingrese el apellido paterno: ")
        apem=input("Ingrese el apellido materno: ")
        corr=input("Ingrese el correo electronico: ")
        telc=input("Ingrese el telefono celular: ")
        teca=input("Ingrese el telefono de casa: ")
        pf=input("Ingrese el perfil de facebook: ")
        telefonoscel[nom]=telc
        telefonoscasa[nom]=teca
        perfilfacebook[nom]=pf
        pnombres[nom]=nom
        segunnombres[nom]=snom
        correos[nom]=corr
        apellidop[nom]=apep
        apellidom[nom]=apem
        contacto.append([nom,apep,apem,corr,telc,teca,pf])
        print(" *GUARDADO* ")

    elif opcionmenu==2:#buscar
        print("Buscar")
        id=int(input("Ingrese el id del contacto a modificar"))
        id=id-1
        nombre = input("ingresa el nombre de contacto:  ")
        if nombre in pnombres:
            print(contacto[id])
        else:
            print(nombre, "no existe")
    elif opcionmenu==3:#Modificar
        mod()
        op=input("ingresa una opcion:")
        id=int(input("Ingrese el id del contacto a modificar"))
        if op== "1":#primer nombre
            op=input("Ingrese el nombre de contacto que desea modificar: ")
            if op in pnombres:
                aux=nom
                nom=input("Ingrese nuevo nombre: ")
                pnombres[aux]=nom
                id=id-1
                contacto[id][0]=nom 
            else:
                print("no existe")
            menu()
        elif op == "2":#segundo nombre
            op=input("Ingrese el nombre de contacto que desea modificar: ")
            if op in segunnombres:
                snom=input("Ingrese nuevo segundo nombre: ")
                segunnombres[op]=snom
                id=id-1
                contacto[id][1]=snom     
            else:
                print(" no existe")
        elif op == "3":#apellido paterno
            op=input("Ingrese el nombre de contacto que desea modificar: ")
            if op in apellidop:
                    apep=input("Ingrese nuevo apellido paterno: ")
                    apellidop[op]=apep
                    id=id-1
                    contacto[id][2]=apep
            else:
                print("apellido existe")
        elif op == "4":#apellido materno
            op=input("Ingrese el nombre de contacto que desea modificar: ")
            if op in apellidom:
                apem=input("Ingrese nuevo nombre: ")
                pnombres[op]=apem
                id=id-1
                contacto[id][3]=apem
            else:
                print(" no existe")
        elif op == "5": #tel cel
            op=input("Ingrese el nombre de contacto que desea modificar: ")
            if op in telefonoscel:
                telc=input("Ingrese nuevo numero celular: ")
                telefonoscel[op]=telc
                id=id-1
                contacto[id][4]=telc
            else:
                print("no existe")
            
        elif op == "6":#tel casa
            op=input("Ingrese el nombre de contacto que desea modificar: ")
            if op in telefonoscasa:
                teca=input("Ingrese nuevo numero de casa: ")
                telefonoscasa [op]=teca
                id=id-1
                contacto[id][5]=teca
            else:
                print(" no existe")  
        elif op == "7":#perfil de facebook
            op=input("Ingrese el nombre de contacto que desea modificar: ")
            if op in perfilfacebook:
                pf=input("Ingrese nuevo perfil de facebook: ")
                perfilfacebook[op]=pf    
                id=id-1
                contacto[id][6]=pf
            else:
                print(" no existe")
        elif op == "8":#correo electronico
            op=input("Ingrese el nombre de contacto que desea modificar: ")
            if op in correos:
                corr=input("Ingrese nuevo correo electronico: ")
                correos[op]=corr
                id=id-1
                contacto[id][7]=corr
            else:
                print(" no existe")
        elif op == 9:  
            menu()
        else:
            print("Error, intentelo de nuevo")
            mod() 
    elif opcionmenu==4:#Mostrar

        print("\nContactos: ",contacto)
        print("\nLa agenda tiene: ", pnombres)
    elif opcionmenu==5:#Eliminar
        id=int(input("Ingrese el id del contacto que desea eliminar: "))
        id=id-1
        eli=input("Ingrese nombre del contacto: ")
        if eli in pnombres:
            del telefonoscel[eli]
            del telefonoscasa[eli]
            del perfilfacebook[eli]
            del pnombres[eli]
            del segunnombres[eli]
            del correos[eli]
            del apellidop[eli]
            del apellidom[eli]
            del contacto[id]
            print("contacto eliminado")
        else:
            print("El numero no existe, intentelo de nuevo")
    elif opcionmenu !=6:
        menu()