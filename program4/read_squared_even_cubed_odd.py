#pseudocode
#create integers.txt
#list 20 integers
#open .txt file and separately read each line from the .txt file
with open("numbers.txt", "r") as integers_file:
    for line in integers_file:
        line = line.strip()

#separate even and odd numbers extracted from the file
#if the number is even

        if int(line) % 2 == 0:

#Put each even integer into double.txt and square them.
#open the "even.txt" file and write the squared even numbers extracted
#if the number is odd
#Put each odd integer into triple.txt and cube them.
#open the"odd.txt" file and write the cubed odd numbers extracted