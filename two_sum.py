def two_sum_pairs(numbers, target):
    listy = []
    for n in range(0,len(numbers)):
        for r in range(0,n):
            if(target-numbers[n]==numbers[r]):
                if (n!=r):
                     listy.append({numbers[r],numbers[n]})
    listy=listy[::-1] 
    return listy


