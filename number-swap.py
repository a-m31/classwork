# This program sorts a list of numbers sequentially in ascending order

user_input=""

while user_input!="exit":
    user_input=input("Enter a list of numbers separated by commas: ")
    
    if not(user_input.isalpha()):
        try:  # Convert string to integers if only containing numbers & commas
            original=[int(num) for num in user_input.split(",")]
        except ValueError:
            print("Sorry, that was not a valid entry.")
            continue

        # Print original list
        res=str(original)[1:-1]  # Remove brackets
        print("Original list: ",res)

        def insertion_sort(original):
            count=0
            for i in range(1,len(original)):
                # If value to the right is smaller than previous value
                # Swap values and increment counter
                while i>0 and original[i-1]>original[i]:
                    original[i],original[i-1]=original[i-1],original[i]
                    i-=1
                    count+=1
                    # Print each individual swap
                    res=str(original)[1:-1]
                    print("Swap {}: ".format(count),res)
            return original

        # Print final sorted list
        res=str(insertion_sort(original))[1:-1]       
        print("Sorted list: ",res)

        # Calculate mean of list: sum of terms / number of terms
        def calculate_mean(original):
            avg=sum(original)/len(original)
            return avg
        print("Mean value: ",round(calculate_mean(original),1))

    else:
        if user_input.lower()=="exit":
            user_input=user_input.lower()
            print("Goodbye.\n")
        else:
            print("I don't understand. Try again.\n")

