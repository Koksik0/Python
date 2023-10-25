L = [3, 5, 4] ; L = L.sort() #Po wykonaniu tych operacjacji do L zostanie przypisane None, ponieważ sort() zmienia listę na miejscu

x, y = 1, 2, 3 #Błąd ponieważ prubujemy przypisać 3 wartości do 2 zmiennych

X = 1, 2, 3 ; X[1] = 4 #Krotki nie można modyfikować

X = [1, 2, 3] ; X[3] = 4 #Bład ponieważ lista ma 3 elementy a nie 4

X = "abc" ; X.append("d") #Metoda append działa na listach a nie na String

L = list(map(pow, range(8))) #Funkcja pow wymaga dwóch argumentów
