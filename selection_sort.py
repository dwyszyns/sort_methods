def selectionSort(tab=[]):
    tab = tab.copy()
    for i in range(0, len(tab) - 1):
        pmin = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[pmin]:
                pmin = j
        tab[pmin], tab[i] = tab[i], tab[pmin]
    return tab
