import logging

# Konfiguracja logowania — poziom INFO, bez daty, tylko wiadomość
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Pobranie typu działania
dzialanie = input(">> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

# Pobranie dwóch liczb jako float (działamy na ułamkach)
a = float(input("Podaj składnik 1: "))
b = float(input("Podaj składnik 2: "))

# Logika kalkulatora
if dzialanie == "1":
    logging.info(f"Dodaję {a:.2f} i {b:.2f}")
    wynik = a + b
elif dzialanie == "2":
    logging.info(f"Odejmuję {b:.2f} od {a:.2f}")
    wynik = a - b
elif dzialanie == "3":
    logging.info(f"Mnożę {a:.2f} razy {b:.2f}")
    wynik = a * b
elif dzialanie == "4":
    logging.info(f"Dzielę {a:.2f} przez {b:.2f}")
    wynik = a / b
else:
    print("Nieprawidłowy wybór działania.")
    wynik = None

# Wyświetlenie wyniku, jeśli został obliczony
if wynik is not None:
    print(f"Wynik to {wynik:.2f}")

