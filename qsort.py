def partition(tab, left, right):
    i = left - 1
    j = right + 1
    v = tab[left]

    while True:
        i += 1
        while i < right and tab[i] < v:
            i += 1
        j -= 1
        while j > left and tab[j] > v:
            j -= 1
        if i >= j:
            break
        tab[i], tab[j] = tab[j], tab[i]
    return j


def Qsort(tab):
    tab = tab.copy()
    sort(tab, 0, len(tab) - 1)
    return tab


def sort(tab, left, right):
    if right <= left:
        return
    j = partition(tab, left, right)
    sort(tab, left, j)
    sort(tab, j + 1, right)

