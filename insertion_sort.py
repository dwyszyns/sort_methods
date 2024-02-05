def insertionSort(tab):
    tab = tab.copy()
    for i in range(0, len(tab)):
        chosen = tab[i]
        j = i-1
        while (j >= 0 and tab[j] > chosen):
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = chosen
    return tab
