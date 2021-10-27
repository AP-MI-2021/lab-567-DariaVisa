from Tests.test_all import run_all_tests
from UI.console import run_menu


def main():
    run_all_tests()
    lista = []
    run_menu(lista)


if __name__ == "__main__":

    main()
