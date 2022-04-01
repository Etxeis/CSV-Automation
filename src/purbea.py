import csv


def DoctorListCreator():
    doctorFile = open('PROFESIONALES.csv', encoding='iso-8859-1')

    doctorList = []

    for line in doctorFile:
        columns = line.split(';')
        doctorList.append(columns[1])

    doctorListCorrect = []

    for doctor in doctorList:
        name = doctor.split(' ')
        transition = []
        for part in name:
            transition.append(part)

        doctorListCorrect.append(transition)

    return doctorListCorrect

