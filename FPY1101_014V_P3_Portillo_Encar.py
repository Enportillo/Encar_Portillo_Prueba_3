# FPY1101_014V_P3_Portillo_Encar
import os
os.system('cls')
import random

menu = {
    1 : 'Grabar',
    2 : 'Buscar',
    3 : 'Imprimir certificados',
    4 : 'Salir'
}


def menu_automotora():
        print('\nBienvenido a la automotora AUTO SEGURO')
        print('Seleccione una opción del Menú: \n')
        for i in menu:
            print(f'{i}. {menu[i]}')


menu_tipos = {
    1 : 'Automovil',
    2 : 'Camión',
    3 : 'Camioneta',
    4 : 'Moto'
}


lista_datos = []
        
usuario = 0
def grabar():
    dic_datos = {}
    elección = 0
    while elección >0 or elección <6:
        print('''Seleccione el tipo de vehiculo:
1. Automovil
2. Camión
3. Camioneta
4. Moto
''')
        try:
            elección = int(input('> '))
        except:
            elección = 0
        if elección not in menu_tipos:
            print('Opción fuera de rango')
            
        else:
            dic_datos['Tipo'] = menu_tipos[elección]
            print(menu_tipos[elección])
            break
    while True:
        patente = input('Ingrese patente (XXXX-00): ').strip()
        if patente == '' or (len(patente) != 7):
            print('Ingrese una opción de patenete valida XXXX-00')
        else:
            dic_datos['Patente'] = patente
            break
    while True:
        marca = input('Ingrese Marca del vehiculo: ').strip()
        if marca == '' or marca.isdigit() or len(marca) < 2 or len(marca) > 15:
            print('Por favor ingrese una marca valida')
        else:
            dic_datos['Marca'] = marca
            break
    while True:
        try:
            precio = int(input('Ingrese precio del vehículo: '))
        except:
            precio = 0
        if precio < 5000000:
            print('Ingrese un precio valido')
        else:
            dic_datos['Precio'] = precio
            break
    while True:
        try:
            multas = int(input('Ingrese num de multas \n\nSi no posee puede marcar 0: '))
        except:
            multas = -1
        if multas < 0:
            print('Ingrese un num valido.')
        else:
            if multas == 0:
                dic_datos['Multas'] = 0
                dic_datos['Fecha_Multa'] = ''
                break
            else:
                lista_multas =[]
                lista_fechas_multas = []
                for multa in range(multas):
                    
                    while True:
                        try:
                            fecha = input(f'Ingrese año de la multa {multa+1}: ')
                        except:
                            fecha = 0
                        if fecha > 2024:
                            print('Ingrese una fecha valida')
                        else:
                            lista_multas.append(f'multa {multa+1}')
                            lista_fechas_multas.append(fecha)
                            
                            dic_datos['Multas'] = lista_multas
                            dic_datos['Fecha_Multa'] = lista_fechas_multas
                            break
        break
    while True:
        try:
            fecha_reg = int(input('Ingrese año de registro del vehiculo: '))
        except:
            fecha_reg = 0
        if fecha_reg > 2024 or fecha_reg < 2000:
            print('Ingrese una fecha valida')
        else:
            dic_datos['Fecha_Registro'] = fecha_reg
            break
    while True:
        nombre = input('Ingrese nombre y apellido del dueño: ').strip()
        if nombre == '' or nombre.isdigit():
            print('Opcion de nombre invalido')
        else:
            try:
                run = int(input('Ingrese run del dueño sin puntos y sin digito verificador '))
            except:
                run = 0
            if run < 4000000 or run > 30000000:
                print('Run invalido')
            else:
                dic_datos['Nombre'] = nombre
                dic_datos['Run'] = run
                break
    
    lista_datos.append(dic_datos)

        

def buscar_patente():
    patente = input('Ingrese patente: ')
    print('Datos de la consulta: ')
    for elementos in lista_datos:
        if patente in elementos['Patente']:
            print(f'Tipo: {elementos['Tipo']}')
            print(f'Patente: {elementos['Patente']}')
            print(f'Marca: {elementos['Marca']}')
            print(f'Precio: {elementos['Precio']}')
            print(f'Multas: {elementos['Multas']}')
            print(f'Fecha de Multas: {elementos['Fecha_Multa']}')
            print(f'Fecha de Registro: {elementos['Fecha_Registro']}')
            print(f'Nombre del dueño: {elementos['Nombre']}')
            print(f'Run del dueño: {elementos['Run']}')
        else:
            print('Patente no encontrada')

        

def certificados():
    while True:
        try:
            opcion = int(input('''Seleccione una opcion
1. Emision de Gases contaminantes
2. Anotaciones vigentes
3. Multas
>'''))
        except:
            opcion = 0
        if opcion <1 or opcion>3:
            print('Opcion invalida')
        elif opcion == 1:
            num = random.randrange(1500,3500)
            print(f'Certificado de Emision de Gases contaminantes\nPrecio {num}')
            acepta = input('De acuerdo con el precio? s/n').lower()
            if acepta == 's':
                patente = input('Ingrese patente: ')
                print('Datos de la consulta: ')
                for elementos in lista_datos:
                    if patente in elementos['Patente']:
                        print(f'Patente: {elementos['Patente']}')
                        print(f'Dueño Actual: {elementos['Run']}')
                break
            else:
                print('Hasta luego')
                break
            
        elif opcion == 2:
            num = random.randrange(1500,3500)
            print(f'Certificado de emision de anotaciones vigentes\nPrecio {num}')
            acepta = input('De acuerdo con el precio? s/n').lower()
            if acepta == 's':
                patente = input('Ingrese patente: ')
                print('Datos de la consulta: ')
                for elementos in lista_datos:
                    if patente in elementos['Patente']:
                        print(f'Patente: {elementos['Patente']}')
                        print(f'Dueño Actual: {elementos['Run']}')
                break
            else:
                print('Hasta luego')
                break
            
        elif opcion == 3:
            num = random.randrange(1500,3500)
            print(f'Certificado de multas\nPrecio {num}')
            acepta = input('De acuerdo con el precio? s/n').lower()
            if acepta == 's':
                patente = input('Ingrese patente: ')
                print('Datos de la consulta: ')
                for elementos in lista_datos:
                    if patente in elementos['Patente']:
                        print(f'Patente: {elementos['Patente']}')
                        print(f'Dueño Actual: {elementos['Run']}')
                break
            else:
                print('Hasta luego')
                break
            
    
            
            



        


# Inicia el programa


opcion = 0
while opcion != 4:
    menu_automotora()
    try:
        opcion = int(input('> '))
    except:
        opcion = 0
    if opcion == 1:
        grabar()
    elif opcion == 2:
        
        buscar_patente()
        
    elif opcion == 3:
        certificados()
    elif opcion == 4:
        print('Gracias por visitarnos') 
        
    else:
        print('opcion invalida')

