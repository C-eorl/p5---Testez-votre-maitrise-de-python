students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}


def affiche_note (student):
    if student not in students:
        return print(f"L'étudiant {student} n'existe pas dans la liste.")
    print(f"Note de {student} :")
    for matiere, note in students[student].items():
        print(f"{matiere}: {note}")

def moyenne_eleve(student):
    student_notes =[note for note in students[student].values()]
    moyenne = sum(student_notes) / len(student_notes)
    return print(f"Moyenne de {student}: {moyenne:.2f}")

student = input("Entrez le nom de l’étudiant : ")
affiche_note(student)
moyenne_eleve(student)

