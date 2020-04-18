import json
from django.shortcuts import render

file = open("json_data.json", "r", encoding="utf-8")
structure = json.loads(file.read())
file.close()

administration_units = len(structure["units"]["administration"]) #количество административных подразделений
megafaculties = len(structure["units"]["education"]) #количесвто мегафакультетов
faculties = 0 #количество факультетов
for i in structure["units"]["education"]: #подсчет количество факультетов
    faculties += len(i["faculties"])
education_programs = [] #список с программами,группами и кафедрами
cathedrs = [] #список кафедр
groups = [] #список групп
for i in structure["units"]["education"]: #заполнение массивов
    for faclt in i["faculties"]:
        cathedrs.extend(faclt["cathedr"])
        for cathedra in faclt["cathedr"]:
            for education_program in cathedra["education_programs"]:
                education_programs.append(education_program)
                for year in education_program["year"]:
                    groups.extend(education_program["year"][year])
eduсation_units = faculties + len(cathedrs) + megafaculties #количество научно-образовательных подразделений
def universityInfo(request):
    return render(request, 'universityInfo.html', {
        "json": structure,
        "faculties": faculties,
        "cathedrs": len(cathedrs),
        "megafaculties": megafaculties,
        "administration_units": administration_units,
        "eduсation_units": eduсation_units
    })
def disciplineInfo(request):
    return render(request, 'disciplineInfo.html', {
        "numberof_education_programs": len(education_programs),
        "education_programs": education_programs
    })
def groupsInfo(request):
    return render(request, 'groupsInfo.html', {
        "groups": groups
    })
def departmentsInfo(request):
    return render(request, 'departmentsInfo.html', {
        "cathedrs": cathedrs
    })
def universityStructure(request):
    return render(request, 'universityStructure.html', {
        "structure": structure
    })