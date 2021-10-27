from Domain.rezervari import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare


def print_menu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modifica rezervare")
    print("a.Afisare rezervari")
    print("x.Iesire")


def ui_adauga_rez(lista):
    id = input("Dati id-ul:")
    nume = input("Dati numele:")
    clasa = input("Dati clasa:")
    pret = input("Dati pretul:")
    checkin = input("Dati checkin-ul:")
    return adauga_rezervare(id, nume, clasa, pret, checkin, lista)


def ui_sterge_rez(lista):
    id = input("Dati id-ul rezervarii de sters:")
    return sterge_rezervare(id, lista)


def ui_modifica_rez(lista):
    id = input("Dati id-ul rezervarii de modificat:")
    nume = input("Dati noul nume:")
    clasa = input("Dati noua clasa:")
    pret = input("Dati noul pret:")
    checkin = input("Dati noul checkin:")
    return modifica_rezervare(id, nume, clasa, pret, checkin, lista)


def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            lista = ui_adauga_rez(lista)
        elif optiune == "2":
            lista = ui_sterge_rez(lista)
        elif optiune == "3":
            lista = ui_modifica_rez(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")


