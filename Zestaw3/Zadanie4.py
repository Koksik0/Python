x = input("Podaj liczbę zmiennoprzecinkową: \n")
while True:
    if x == "stop":
        break;
    try:
        temp = float(x)
        print(temp, temp**3)
    except ValueError:
        print("Musisz podać liczbe zmiennoprzecinkową lub \'stop\' jeśli chcesz zatrzymać program \n")
        x = input("Podaj liczbę zmiennoprzecinkową: \n")
        continue
    x = input("Podaj liczbę zmiennoprzecinkową: \n")

