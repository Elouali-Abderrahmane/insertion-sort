sort_list = []
length_list = int(input("Please, Enter the length of the list that you want to sort: "))

for _ in range(length_list):
    sort_list.append(int(input("Enter a number: ")))

print(f"Unsorted list is {sort_list}")


for i in range(1, length_list):
    key = sort_list[i]
    j = i - 1
    while(j >= 0 and sort_list[j] > key):
        sort_list[j + 1] = sort_list[j]
        j -= 1
    sort_list[j + 1] = key


print(f"Sorted list is {sort_list}")