def two_sum_pairs(numbers, target):
    for n in range(0,len(numbers)):
        for r in range(0,n):
            if(target-numbers[n]==numbers[r]):
                if (n!=r):
                    return ((numbers[r],numbers[n]))   
    
if __name__ == "__main__":


