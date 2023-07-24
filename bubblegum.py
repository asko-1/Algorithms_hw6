# bubble sort
def bubble_sort(spisok):
    for i in range(len(spisok)):
        for j in range(len(spisok) - i - 1):
            if spisok[j] > spisok[j + 1]:
                spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
    print(f'sort {spisok}')


# binary search
def binary_search(spisok, search_for):
    lowest = 0
    highest = len(spisok) - 1
    index = None
    while (lowest <= highest) and (index is None):
        mid = (lowest+highest) // 2
        if spisok[mid] == search_for:
          index = mid
        else:
            if search_for < spisok[mid]:
                highest = mid-1
            else:
                lowest = mid + 1
    print(f'search number {search_for} is under index {index}')


spisok = [1, 56, 5, 6, 7, 8, 7, 4, 14]
print(spisok)
bubble_sort(spisok)
binary_search(spisok, 8)
