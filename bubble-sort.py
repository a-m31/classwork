# This program sorts a list of numbers in ascending order using a bubble sort

def bubble_sort(original):
    print("Original List: ",','.join(map(str,original)))
    l=original.copy()
    passes = 0
    last = len(l)
    swapped = True
    while swapped:
        swapped = False
        for j in range(1,last):
            if l[j-1] > l[j]:
                l[j],l[j-1] = l[j-1],l[j]  # Swap
                swapped = True
                last = j
        if swapped:
            passes += 1
            print("Pass {}: ".format(passes),','.join(map(str,l)))

    print("\nOriginal List: ",','.join(map(str,original)))
    print("Sorted List: ",','.join(map(str,l)))
    print("Number of Passes: ",passes,"\n")
    return original

original = " "
while True:
    original = input("Enter a list of numbers separated by commas: ")
    if original.lower() == "exit":
        print("Goodbye")
        break
    elif not(original.isalpha()):
        try:  # Convert string to integers if only containing numbers & commas
            original = [int(num) for num in original.split(",")]
            bubble_sort(original)
        except ValueError:
            print("Sorry, that was not a valid entry. Try again.\n")
            continue
    else:
        print("Sorry, that was not a valid entry. Try again.\n")
