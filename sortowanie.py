import random
import time


def bubble_sort(lista):
    flaga = True
    i = 0
    while i < len(lista)-1 and flaga:
        j = 0
        flaga = False
        while j < len(lista) - 1 -i:
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
                flaga = True
            j+=1
        i += 1 
    return lista


    






def selection_sort(lista):
    i = 0
    while i < len(lista)-1:
        minI = i
        j = i + 1
        while j < len(lista):
            if lista[minI] > lista[j]:
                minI = j
            j += 1
        lista[i], lista[minI] = lista[minI],lista[i]
        i += 1
    return lista






def insertion_sort(lista):
    i = 1
    while i < len(lista):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and klucz < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = klucz
        i += 1
    return lista


def merge_sort(lista):
    if len(lista) > 1:
        srodek = len(lista) // 2
        prawa = lista[srodek:]
        lewa = lista[:srodek]
        merge_sort(lewa)
        merge_sort(prawa)
        

        l = r = k = 0

        while l < len(lewa) and r < len(prawa):
            if lewa[l] < prawa[r]:
                lista[k] = lewa[l]
                l += 1  
            else:
                lista[k] = prawa[r]
                r += 1
            k += 1
        while l < len(lewa):
            lista[k] = lewa[l]
            l += 1
            k += 1
        while r < len(prawa):
            lista[k] = prawa[r]
            r += 1
            k += 1


def podziel(lista, start, end):
    znacznik = lista[end]
    low = start
    high = end - 1

    while True:
        while low <= high and lista[low] <= znacznik:
            low += 1
        while low <= high and lista[high] >= znacznik:
            high -= 1
        if low <= high:
            lista[low],lista[high] = lista[high], lista[low]
        else:
            break
    lista[end],lista[low] = lista[low], lista[end]
    return low

def quick_sort(lista,start,end):
    if start < end:
        znacznik = podziel(lista,start,end)
        quick_sort(lista,start,znacznik - 1)
        quick_sort(lista,znacznik + 1,end)
        

        
            
                    
        


    
    
        






def pods(funkcja,lista,metoda,poka_liste = True):
    kopia = lista.copy()
    t1 = time.time()
    funkcja(kopia)
    t2 = time.time()
    
    print()
    print(f"To jest lista posortowana metodą {metoda}:")
    if poka_liste:
        if len(kopia) > 50:
            print("To jest 25 pierwszych i ostatnich elementów listy")
            print(kopia[:25],"...",kopia[-25:])
        else:
            print(kopia)
    print("Czas z jaką funkcja wykonała sortowanie to:",t2-t1,"sekund.")
    print()





while True:
    print("Jaką metode sortowania chcesz przetestować?")
    print('''
[1] bubble_sort
[2] selection_sort
[3] insertion_sort
[4] merge_sort
[5] quick_sort
[9] Test wszytskich funkcji (bez wypisywania tablicy)
[0] Wyjdz
    ''')
    wybor = input()
    if wybor == "0":
        print("Do zobaczenia")
        break
    while True:
        lista = []
        zasieg = input("Z ilu elementów ma sie składać lista?")
        if zasieg.isdigit():
            zasieg = int(zasieg)
            for i in range(0,zasieg):
                lista.append(random.randint(-1000,1000))
            break
        else:
            print("Musisz podać liczbe")
    if wybor == "1":
        pods(bubble_sort,lista,"bubble_sort")               
    elif wybor == "2":
        pods(selection_sort,lista,"selection_sort")
    elif wybor == "3":
        pods(insertion_sort,lista,"insertion_sort")
    elif wybor == "4":
        pods(merge_sort,lista,"merge_sort")
    elif wybor == "5":
        pods(lambda l: quick_sort(l, 0, len(l)-1),lista,"quick_sort")
        
        
    elif wybor == "9":
        pods(bubble_sort,lista,"bubble_sort",False)
        pods(selection_sort,lista,"selection_sort",False)
        pods(insertion_sort,lista,"insertion_sort",False)
        pods(merge_sort,lista,"merge_sort",False)
        pods(lambda l: quick_sort(l, 0, len(l)-1),lista,"quick_sort",False)
        











