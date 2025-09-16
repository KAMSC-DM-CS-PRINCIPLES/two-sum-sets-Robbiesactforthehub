def two_sum_pairs(numbers, target):
    list = []
    for n in range(0,len(numbers)):
        for r in range(0,n):
            if(target-numbers[n]==numbers[r]):
                if (n!=r):
                     list.append({numbers[r],numbers[n]})
    reversed(list)   
    return list


