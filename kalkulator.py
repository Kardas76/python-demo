


def main():


    koniec = False
    while not koniec:
        print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:")

        try:
            liczba1 = float(input())
            operacja = (input())
            liczba2 = float(input())

            if operacja == "+":
                wynik = liczba1 + liczba2

            elif operacja == "-":
                wynik = liczba1 - liczba2

            elif operacja == "*":
                wynik = liczba1 * liczba2

            elif operacja == "/":
                wynik = liczba1 / liczba2

            elif operacja == "%":
                wynik = liczba1 % liczba2

            else:
                print("blad")
                break

            print("wynik: " +str(wynik))
        finally:
            print("blad")


if __name__ == "__main__":
    main()
