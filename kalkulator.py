def kalkulator():
    print("Prosty kalkulator")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wybierz operację (1/2/3/4): ")

    if wybor in ['1','2','3','4']:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print(f"Wynik: {a + b}")
        elif wybor == '2':
            print(f"Wynik: {a - b}")
        elif wybor == '3':
            print(f"Wynik: {a * b}")
        elif wybor == '4':
            if b == 0:
                print("Błąd: dzielenie przez zero!")
            else:
                print(f"Wynik: {a / b}")
    else:
        print("Nieprawidłowy wybór!")

if __name__ == "__main__":
    kalkulator()
