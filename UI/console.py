from Domain.rezervari import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import update_clasa, ieftinire_rezervare


def print_menu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modifica rezervare")
    print("4.Trecerea tuturor rezervarilor pe un nume dat la o clasa superioara")
    print("5.Ieftinirea rezervarilor la care s-a facut checkin cu un procentaj dat")
    print("a.Afisare rezervari")
    print("x.Iesire")


def ui_adauga_rez(lista):
    id = input("Dati id-ul:")
    nume = input("Dati numele:")
    clasa = input("Dati clasa:")
    pret = int(input("Dati pretul:"))
    checkin = bool(input("Dati checkin-ul:"))
    return adauga_rezervare(id, nume, clasa, pret, checkin, lista)


def ui_sterge_rez(lista):
    id = input("Dati id-ul rezervarii de sters:")
    return sterge_rezervare(id, lista)


def ui_modifica_rez(lista):
    id = input("Dati id-ul rezervarii de modificat:")
    nume = input("Dati noul nume:")
    clasa = input("Dati noua clasa:")
    pret = int(input("Dati noul pret:"))
    checkin = bool(input("Dati noul checkin:"))
    return modifica_rezervare(id, nume, clasa, pret, checkin, lista)


def ui_update_clasa(lista):
    nume = input("Dati un nume pentru a modifica clasa:")
    return update_clasa(nume, lista)


def ui_ieftinire_rezervare(lista):
    reducere = int(input("Dati un numar pentru a reduce rezervarea:"))
    return ieftinire_rezervare(lista, reducere)


def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def run_menu(lista):
    lista = []
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
        elif optiune == "4":
            lista = ui_update_clasa(lista)
        elif optiune == "5":
            lista = ui_ieftinire_rezervare(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")
