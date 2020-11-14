def main():
    wszystkie = []
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    przegrywy = [1]
    wygrywy = []
    first = False
    second = False
    third = False
    fourth = False

    for i in range(0, 101):
        wszystkie.append(i)

    for j in range(1, 101):
        print(wszystkie[j], end=": ")
        if wszystkie[j]-1 in prime_numbers: #jesli liczba mniejsza o 1 jest prime to ja wypisz
            print(wszystkie[j]-1, end="")
            wygrywy.append(wszystkie[j])
            first = True

        if wszystkie[j] in prime_numbers: #jesli ta liczba jest prime to ja wypisz
            if first:
                print(",", wszystkie[j])
            else:
                print(wszystkie[j])
            wygrywy.append(wszystkie[j])
            second = True

        elif wszystkie[j] in przegrywy:  #jesli ta liczba jest przegrywem przejdz do nowej linii bez pisania zadnej liczby
            print("")
            third = True

        if first and not second:
            print("")
            fourth = True


        if not first and not second and not third:
            przegrywy.append(wszystkie[j])
            print("")


        first = False
        second = False
        third = False
        fourth = True


main()
