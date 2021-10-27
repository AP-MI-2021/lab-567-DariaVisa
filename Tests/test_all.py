from Tests.test_CRUD import test_adauga_rezervare, test_sterge_prajitura, test_modifica_prajitura
from Tests.test_Domeniu import test_rezervare


def run_all_tests():
    test_rezervare()
    test_adauga_rezervare()
    test_sterge_prajitura()
    test_modifica_prajitura()