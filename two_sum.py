def two_sum_pairs(numbers, target):
    list = []
    for n in range(0,len(numbers)):
        for r in range(0,n):
            if(target-numbers[n]==numbers[r]):
                if (n!=r):
                     list.insert(0,{numbers[r],numbers[n]})   
    return list


