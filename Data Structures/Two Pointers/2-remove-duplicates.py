def remove_duplicates(arr:list[int]) -> int:
    duplicate = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            duplicate +=1
    return len(arr) - duplicate

def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
main()