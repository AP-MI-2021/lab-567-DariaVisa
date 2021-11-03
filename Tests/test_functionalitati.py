from Domain.rezervari import get_clasa, get_pret
from Logic.CRUD import adauga_rezervare
from Logic.functionalitati import update_clasa, ieftinire_rezervare


def test_update_clasa():
    lista = adauga_rezervare("1", "Daniel", "economy plus", 1200, True, [])
    lista = adauga_rezervare("2", "Daniel", "economy", 100, True, lista)
    lista = adauga_rezervare("3", "Star", "economy plus", 1800, True, lista)
    lista = update_clasa("Daniel", lista)
    assert get_clasa(lista[0]) == "business"
    assert get_clasa(lista[1]) == "economy plus"
    assert get_clasa(lista[2]) == "economy plus"


def test_ieftinire_rezervare():
    lista = adauga_rezervare("1", "Daniel", "economy plus", 1200, True, [])
    lista = adauga_rezervare("2", "Daniel", "economy", 100, False, lista)
    lista = adauga_rezervare("3", "Star", "economy plus", 1800, True, lista)
    lista = ieftinire_rezervare(lista, 50)
    assert get_pret(lista[0]) == 600
    assert get_pret(lista[1]) == 100
    assert get_pret(lista[2]) == 900