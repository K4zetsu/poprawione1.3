import random

liczba = random.randint(0, 100)
zgadnij = int(input("Spróbuj zgadnąć liczbę wylosowaną przez komputer: "))
petla = True
liczba_prob = 0
while petla:
    if zgadnij > liczba:
         print("wylosowana liczba jest mniejsza!")
         zgadnij = int(input("Spróbuj jeszcze raz: "))
         liczba_prob += 1
    elif zgadnij < liczba:
        print("Wylosowana liczba jest większa!")
        zgadnij = int(input("Spróbuj jeszcze raz!: "))
        liczba_prob += 1
    elif zgadnij == liczba:
            print("Tak!! udało ci się!!1")
            print(f"Udało ci się zgadnąć za {liczba_prob} razem.")
            liczba_prob = 0
            decyzja = input("Czy chcesz zagrać ponownie? t/n: ")
            decyzja = decyzja.lower()
            if decyzja == "t" or decyzja == "tak":
                 liczba = random.randint(0, 100)
                 zgadnij = int(input("Spróbuj zgadnąć liczbę wylosowaną przez komputer: "))
                 continue
            else:
                petla = False

