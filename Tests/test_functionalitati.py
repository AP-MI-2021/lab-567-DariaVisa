from Domain.rezervari import get_clasa, get_pret
from Logic.CRUD import adauga_rezervare
from Logic.functionalitati import update_clasa, ieftinire_rezervare, pret_maxim_clasa, ordonare_descrescatoare, \
    suma_pret


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


def test_pret_maxim_clasa():
    lista = adauga_rezervare("1", "Daniel", "economy plus", 1200, True, [])
    lista = adauga_rezervare("2", "Daniel", "economy", 100, False, lista)
    lista = adauga_rezervare("3", "Star", "economy plus", 1800, True, lista)
    lista = adauga_rezervare("4", "Star", "business", 1800, True, lista)
    rezultat = pret_maxim_clasa(lista)
    assert rezultat["economy"] == 100
    assert rezultat["economy plus"] == 1800
    assert rezultat["business"] == 1800


def test_ordonare_descrescatoare():
    lista = adauga_rezervare("1", "Daniel", "economy plus", 1200, True, [])
    lista = adauga_rezervare("2", "Daniel", "economy", 10, False, lista)
    lista = adauga_rezervare("3", "Star", "economy plus", 100, True, lista)
    lista = adauga_rezervare("4", "Star", "business", 1800, True, lista)
    rezultat = ordonare_descrescatoare(lista)
    assert rezultat[0]["pret"] == 1800
    assert rezultat[1]["pret"] == 1200
    assert rezultat[2]["pret"] == 100
    assert rezultat[3]["pret"] == 10


def test_suma_pret():
    lista = adauga_rezervare("1", "Daniel", "economy plus", 1200, True, [])
    lista = adauga_rezervare("2", "Daniel", "economy", 10, False, lista)
    lista = adauga_rezervare("3", "Star", "economy plus", 100, True, lista)
    lista = adauga_rezervare("4", "Star", "business", 1800, True, lista)
    rezultat = suma_pret(lista)
    assert rezultat["Daniel"] == 1210
    assert rezultat["Star"] == 1900
