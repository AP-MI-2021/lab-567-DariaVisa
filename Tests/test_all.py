from Tests.test_CRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare
from Tests.test_Domeniu import test_rezervare
from Tests.test_functionalitati import test_update_clasa, test_ieftinire_rezervare, test_pret_maxim_clasa, \
    test_ordonare_descrescatoare, test_suma_pret


def run_all_tests():
    test_rezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_update_clasa()
    test_ieftinire_rezervare()
    test_pret_maxim_clasa()
    test_ordonare_descrescatoare()
    test_suma_pret()
