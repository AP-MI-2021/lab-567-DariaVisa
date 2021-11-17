from Logic.CRUD import adauga_rezervare, get_by_id


def operatii(undo_list, redo_list, lista):
    undo_list.append(lista)
    redo_list.clear()


def test_ui_undo_redo():
    undo_list = []
    redo_list = []

    lista = []

    operatii(undo_list, redo_list, lista)
    lista = adauga_rezervare("1", "Daniel", "economy plus", 1200, True, lista)
    assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adauga_rezervare("2", "Daniel", "economy", 10, False, lista)
    assert len(lista) == 2

    operatii(undo_list, redo_list, lista)
    lista = adauga_rezervare("3", "Star", "economy plus", 100, True, lista)
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
        assert get_by_id(lista[1]) == "2"

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    assert get_by_id(lista[0]) == "1"

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 0

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert len(lista) == 0

    operatii(undo_list, redo_list, lista)
    lista = adauga_rezervare("1", "Daniel", "economy plus", 1200, True, lista)
    assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adauga_rezervare("2", "Daniel", "economy", 10, False, lista)
    assert len(lista) == 2

    operatii(undo_list, redo_list, lista)
    lista = adauga_rezervare("3", "Star", "economy plus", 100, True, lista)
    assert len(lista) == 3

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adauga_rezervare("4", "Helou", "economy plus", 230, False, lista)
    assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 0

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 1
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2

    assert get_by_id(lista[0]) == "1"
    assert get_by_id(lista[1]) == "4"

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
