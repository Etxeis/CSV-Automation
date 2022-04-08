import csv
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Generador CSV')
root.resizable(False, False)
root.geometry('300x150')

archName = ''
errorName = ''

def select_file():
    filetypes = (
        ('Archivos CSV', '*.csv'),
    )

    filename = fd.askopenfilename(
        title='Seleccionar Archivo',
        initialdir='/',
        filetypes=filetypes)
    
    global archName
    archName = str(filename)
    listaSalida = archName.split("/")
    global errorName
    listaError = listaSalida.copy()
    listaError.pop(-1)
    errorName = "/".join(listaError)
    set_text(listaSalida[-1])

def set_text(text):
    e.delete(0, tk.END)
    e.insert(0, text)
    return

e = tk.Entry(root,width=30)
e.place(relx=.5, rely=.5, anchor="center", y=-55)

def automatizacion():
    file = open(archName, encoding='iso-8859-1') 

    header = []
    rows = []

    for line in file:
        columns = line.split(";")
        header.append(columns)
        break

    for line in file:
        columns = line.split(";")
        rows.append(columns)

    generatedFile = open(archName[:-4]+' - Generado.csv', 'w', encoding='iso-8859-1', newline='')
    generatedHeader = ['Rut', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Especialidad', 'Ani 1', 'Ani 2', 'Fecha Citacion', 'Hora Citacion', 'Tiempo Anticipacion', 'Policlinico', 'Nombre Doctor', 'Mail']
    generatedRow = []

    writer = csv.writer(generatedFile, delimiter=';')
    writer.writerow(generatedHeader)

    errorCounter = 0
    personCounter = 1
    errorList = []


    for person in rows:
        temporaryList = ['', '', '', '', '', '', '', '', '', '', '', '', '']
        flagFirstNumb = False
        flagSecondNumb = False

        for atribute in person:
            if (person[51].lower() != "agendado"):
                break

            personCounter += 1
            if (len(person) != 57): # Para detectar fallas de sobredigitacion
                errorCounter += 1
                errorList.append(personCounter)

            if (atribute == person[0]): # Para obtener el Rut
                temporaryList[0] = atribute

            if (atribute == person[1]): # Para obtener el primer nombre
                name = person[1]
                nameList = name.split(" ")
                temporaryList[1] = nameList[0]
            elif (atribute == person[2]): # Para fijar el apellido paterno
                temporaryList[2] = atribute
            elif (atribute == person[37]): # Para obtener la especialidad
                temporaryList[4] = atribute
            elif (atribute == person[30]): # Para obtener el policlinico
                temporaryList[10] = atribute
            elif (atribute == person[19]): # Arreglos de numeros telefonicos (Si tiene mas de 9 o menos de 7 se considera como mal digitado)
                if (len(person[19]) == 8): # Si tiene 8 numeros
                    if (2 <= int(person[19][0]) <= 3): 
                        temporaryNumber = '2'+person[19]
                        temporaryList[5] = temporaryNumber
                        flagFirstNumb = True
                    else:
                        temporaryNumber = '9'+person[19]
                        temporaryList[5] = temporaryNumber
                        flagFirstNumb = True

                if (len(person[19]) == 7): # Si tiene 7 numeros
                    temporaryNumber = '22'+person[19]
                    temporaryList[5] = temporaryNumber
                    flagFirstNumb = True
                if (len(person[19]) == 9): # Si tiene 9 numeros
                    if (int(person[19][0]) == 9):
                        temporaryList[5] = person[19]
                        flagFirstNumb = True
                    elif (int(person[19][:1]) == 22):
                        temporaryList[5] = person[19]
                        flagFirstNumb = True
                    elif (int(person[19][:1]) == 23):
                        temporaryList[5] = person[19]
                        flagFirstNumb = True

            elif (atribute == person[20]):
                if (flagFirstNumb == True):
                    if (len(person[20]) == 8): # Si tiene 8 numeros
                        if (2 <= int(person[20][0]) <= 3): 
                            temporaryNumber = '2'+person[20]
                            temporaryList[6] = temporaryNumber
                            flagSecondNumb = True
                        else:
                            temporaryNumber = '9'+person[20]
                            temporaryList[6] = temporaryNumber
                            flagSecondNumb = True

                    if (len(person[20]) == 7): # Si tiene 7 numeros
                        temporaryNumber = '22'+person[20]
                        temporaryList[6] = temporaryNumber
                        flagSecondNumb = True
                    if (len(person[20]) == 9): # Si tiene 9 numeros
                        if (int(person[20][0]) == 9):
                            temporaryList[6] = person[20]
                            flagSecondNumb = True
                        elif (int(person[20][:1]) == 22):
                            temporaryList[6] = person[20]
                            flagSecondNumb = True
                        elif (int(person[20][:1]) == 23):
                            temporaryList[6] = person[20]
                            flagSecondNumb = True

                else:
                    if (len(person[20]) == 8): # Si tiene 8 numeros
                        if (2 <= int(person[20][0]) <= 3): 
                            temporaryNumber = '2'+person[20]
                            temporaryList[5] = temporaryNumber
                            flagFirstNumb = True
                        else:
                            temporaryNumber = '9'+person[20]
                            temporaryList[5] = temporaryNumber
                            flagFirstNumb = True

                    if (len(person[20]) == 7): # Si tiene 7 numeros
                        temporaryNumber = '22'+person[20]
                        temporaryList[5] = temporaryNumber
                        flagFirstNumb = True
                    if (len(person[20]) == 9): # Si tiene 9 numeros
                        if (int(person[20][0]) == 9):
                            temporaryList[5] = person[20]
                            flagFirstNumb = True
                        elif (int(person[20][:1]) == 22):
                            temporaryList[5] = person[20]
                            flagFirstNumb = True
                        elif (int(person[20][:1]) == 23):
                            temporaryList[5] = person[20]
                            flagFirstNumb = True


            elif (atribute == person[21]):
                if (flagFirstNumb == False):
                    if (len(person[21]) == 8): # Si tiene 8 numeros
                        if (2 <= int(person[21][0]) <= 3): 
                            temporaryNumber = '2'+person[21]
                            temporaryList[5] = temporaryNumber
                            flagFirstNumb = True
                        else:
                            temporaryNumber = '9'+person[21]
                            temporaryList[5] = temporaryNumber
                            flagFirstNumb = True

                    if (len(person[21]) == 7): # Si tiene 7 numeros
                        temporaryNumber = '22'+person[21]
                        temporaryList[5] = temporaryNumber
                        flagFirstNumb = True
                    if (len(person[21]) == 9): # Si tiene 9 numeros
                        if (int(person[21][0]) == 9):
                            temporaryList[5] = person[21]
                            flagFirstNumb = True
                        elif (int(person[21][:1]) == 22):
                            temporaryList[5] = person[21]
                            flagFirstNumb = True
                        elif (int(person[21][:1]) == 23):
                            temporaryList[5] = person[21]
                            flagFirstNumb = True

                elif (flagFirstNumb == True and flagSecondNumb == False):
                    if (len(person[21]) == 8): # Si tiene 8 numeros
                        if (2 <= int(person[21][0]) <= 3): 
                            temporaryNumber = '2'+person[21]
                            temporaryList[6] = temporaryNumber
                            flagSecondNumb = True
                        else:
                            temporaryNumber = '9'+person[21]
                            temporaryList[6] = temporaryNumber
                            flagSecondNumb = True

                    if (len(person[21]) == 7): # Si tiene 7 numeros
                        temporaryNumber = '22'+person[21]
                        temporaryList[6] = temporaryNumber
                        flagSecondNumb = True
                    if (len(person[21]) == 9): # Si tiene 9 numeros
                        if (int(person[21][0]) == 9):
                            temporaryList[6] = person[21]
                            flagSecondNumb = True
                        elif (int(person[21][:1]) == 22):
                            temporaryList[6] = person[21]
                            flagSecondNumb = True
                        elif (int(person[21][:1]) == 23):
                            temporaryList[6] = person[21]
                            flagSecondNumb = True

            elif (atribute == person[45]): # Para el dia de la cita
                temporaryList[7] = person[45]

            elif (atribute == person[46]): # Para la hora de citacion
                temporaryList[8] = person[46][:5]


            elif (atribute == person[32]): # Para el nombre del doctor
                name = person[32]
                nameList = name.split(" ")
                if (len(nameList) == 2):
                    temporaryList[11] = nameList[1].upper()
                else:
                    temporaryList[11] = (name).upper()

            if ("@" in person[9]):
                temporaryList[12] = person[9].lower()
            else:
                temporaryList[12] = '.'
                

            temporaryList[9] = '.'
            temporaryList[3] = '.'

            if (flagFirstNumb == False):
                temporaryList[5] = '.'
                temporaryList[6] = '.'
            elif (flagFirstNumb == True and flagSecondNumb == False):
                temporaryList[6] = '.'

        if (temporaryList[0] != ''):
            writer.writerow(temporaryList)

    generatedFile.close()

    if (len(errorList) != 0):
        errorFile = open(errorName+'/Errores.txt', 'w', encoding='iso-8859-1', newline='')
        errorFile.write("Se han detectado errores de digitacion en los siguientes pacientes:\n")
        for error in errorList:
            errorFile.write(str(error))
            errorFile.write("\n")
        errorFile.close()
        showinfo(message="Archivo generado!\nSE HAN DETECTADO "+str(errorCounter)+" ERRORES!")

    else:
        showinfo(message="Archivo generado!")


def Intento():
    try:
        automatizacion()
    except:
        showinfo(message="No se ha seleccionado ningun archivo")

open_button = ttk.Button(
    root,
    text='Abrir Archivo ".csv"',
    command=select_file
)
open_button.place(relx=.5, rely=.5, anchor="center", y=-25)


ttk.Button(root, text="GENERAR", command=Intento).place(relx=.5, rely=.5, anchor="center", y=30)
ttk.Label(root, text="v1.0").place(x=264, y=127)




root.mainloop()
