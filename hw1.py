def strcounter(string): #сложность O(n * m)
    for symvol in set(string): 
        counter = 0
        for subsymvol in string:
            if symvol == subsymvol:
                counter += 1
    if counter == 2:
        print(True)
    else:
        print(False)
            
strcounter('abcde')
strcounter('abffba')

