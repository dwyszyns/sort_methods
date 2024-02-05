def mergeSort(tab):
    tab = tab.copy()
    if len(tab) > 1:
        mid = len(tab) // 2 
        left_half = tab[:mid]
        right_half = tab[mid:]
        left_half = mergeSort(left_half)
        right_half = mergeSort(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                tab[k] = left_half[i]
                i += 1
            else:
                tab[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):  
            tab[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):  
            tab[k] = right_half[j]
            j += 1
            k += 1
    return tab
