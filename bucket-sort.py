
def bucket_sort (array_to_sort, n) :

    #create list that will hold all the buckets (also lists)
    bucket_list = []
    bucket_number = n
    while (bucket_number > 0):
        new_bucket = []
        bucket_list.append(new_bucket)
        bucket_number = bucket_number - 1


    maximum = max(array_to_sort)
    minimum = min(array_to_sort)

    #the numerical range that each bucket can hold
    element_range = (maximum - minimum) // n+1

    #place elements in their respective buckets
    for index in range(len(array_to_sort)):
        number = array_to_sort[index]
        difference = number - minimum
        bucket_number = (int) (difference // element_range)
        bucket_list[bucket_number].append(number)


    #sort all the buckets and merge them
    sorted_list = []
    for bucket in range(len(bucket_list)):
        current = bucket_list[bucket]
        current.sort()
        if len(current) != 0:
            sorted_list.extend(current)


    return sorted_list

def main():
    example_list = [3,1,5,2,1]
    sorted_list = bucket_sort(example_list,5)
    print(example_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
