# Out of N integers given, pick M numbers so that their sum would be S
# User inputs filename (out of which the program will gather N integers from), numbers M and S

import os # to check if file exists

N_max = 99 # the elements in the file shouldn't be larger than 99
N_min = -99

def combinations(numbers, index_tracker, S, M, partial=[], p_index=[]):
    s_sum = sum(partial)
    if (s_sum >= S or len(partial)==M) and negative == 0:
        
        if s_sum==S and len(partial)==M:
            if_statements(1, partial, p_index)

        elif ((s_sum>S and len(partial)<M) or (len(partial)==M and s_sum>S)) and len(partial)>0: 
            if_statements(2, partial, p_index)

        elif len(partial)==M and s_sum<S:
            if_statements(3, partial, p_index)
        
        if (not (s_sum==S and len(partial)<M)) and len(partial)>0: 
            return  # if we reach or go overboard S, there's no point in continuing so it returns to the for cycle below            

    elif len(partial)==M and negative == 1: 

        if s_sum==S and len(partial)==M:
            if_statements(1, partial, p_index)

        elif len(partial)==M and s_sum>S:
            if_statements(2, partial, p_index)

        elif len(partial)==M and s_sum<S:
            if_statements(3, partial, p_index)
        
        if len(partial)==M:
            return # with negatives there's a chance the large sum will diminish so we wait until the combo is made up of M

    for i in range(len(numbers)): 
        n = numbers[i] # the current element we are checking
        ni = index_tracker[i]+1
        remaining = numbers[i+1:] # from i+1 to the end of the array
        remainingi = index_tracker[i+1:]

        depth = depth_tracker.pop(0) + 1 # I could've just made len(partial) and it would've been the same...
        depth_tracker.append(depth)

        combinations(remaining, remainingi, S, M, partial + [n], p_index + [ni]) # recursion

    depth = depth_tracker.pop(0) - 1
    depth_tracker.append(depth)

def if_statements(i, partial, p_index):
    depth = depth_tracker.pop(0)

    index_to_str = ', '.join([str(elem) for elem in p_index]) # turns the elem into string and seperates elem by ,
    combo_to_str = ', '.join([str(elem) for elem in partial])
    index_len = (max_len_i*M)+(M-1)*2 - len(index_to_str) # (M-1)*2 for spaces and commas
    nr_len = (max_len_n*M)+(M-1)*2 - len(combo_to_str)
    
    if i==1:
        step = step_tracker.pop(0) + 1
        step_tracker.append(step)
        sum_combo.append(partial)
        sum_index.append(p_index)
        
        print ('{:5d}'.format(step), end= ") ", file = output_file) # 5d is for alignment
        print (f"{'-'*depth:>{M}}", index_to_str, " "*index_len, " | ", combo_to_str, " "*nr_len, "   CORRECT", file = output_file)
    elif i==2:
        step = step_tracker.pop(0) + 1
        step_tracker.append(step)

        print ('{:5d}'.format(step), end= ") ", file = output_file) 
        print (f"{'-'*depth:>{M}}", index_to_str, " "*index_len, " | ", combo_to_str, " "*nr_len, "   bad", end="", file = output_file)
        print(", since ", sum(partial), ">S", sep="", file = output_file)
    elif i==3:
        step = step_tracker.pop(0) + 1
        step_tracker.append(step)

        print ('{:5d}'.format(step), end= ") ", file = output_file) 
        print (f"{'-'*depth:>{M}}", index_to_str, " "*index_len, " | ", combo_to_str, " "*nr_len, "   bad", end="", file = output_file)
        print(", since ", sum(partial), "<S", sep="", file = output_file)

    depth = depth - 1
    depth_tracker.append(depth)

def remove_repetition():
    for seq in sum_combo:
        j = 0
        count = 0
        for seq2 in sum_combo:
            if seq == seq2:
                count = count + 1
            if count > 1:
                sum_combo.pop(j) #if there's (1, 4) (1,4) then it will remove the 2nd one
                sum_index.pop(j)
                count = 1
            j = j + 1            

    for seq in sum_combo:
        j = 0
        count = -M
        for seq2 in sum_combo:
            for el in seq:
                for el2 in seq2:
                    if el == el2:
                        count = count + 1
                        break
            if count == M:
                sum_combo.pop(j) # if there's (1, 4) (4, 1), then it wil remove the 2nd one
                sum_index.pop(j)
            j = j + 1

def printscreen_combos():
    print("\nPart III", file = output_file)

    if sum_combo: # if not empty
        print("Combinations found: ")
        print("Combinations found: ", file = output_file)

        el_step = 1 # for numeration of results
        for seq in sum_combo:
            if(len(sum_combo)>1):
                len_sum = len(str(len(sum_combo))) # so we know how much to push from the left, when numerating results
                print (f"{el_step:>{len_sum}}", end= ") ")
                print (f"{el_step:>{len_sum}}", end= ") ", file = output_file)

            sumy_index = sum_index.pop(0)

            # alignment calculation
            index_to_str = ', '.join([str(elem) for elem in sumy_index]) 
            sum_index.append(sumy_index)
            combo_to_str = ', '.join([str(elem) for elem in seq])
            index_len = (max_len_i*M)+(M-1)*2 - len(index_to_str) # (M-1)*2 for spaces and commas
            if (negative):
                nr_len = (max_len_n*(M*2)) + (M-2)*2 - len(combo_to_str)
            else:
                nr_len = (max_len_n*M)+(M-1)*2 - len(combo_to_str)

            print (index_to_str, " "*index_len, " | ", combo_to_str, " "*nr_len)
            print (index_to_str, " "*index_len, " | ", combo_to_str, " "*nr_len, file = output_file)

            el_step = el_step + 1

        print("", file = output_file)

    else:
        print("No combinations found")
        print("No combinations found\n", file = output_file)

if __name__ == "__main__":
    sum_combo = [] # to keep track of correct combinations
    sum_index = [] # to keep track of the indexes of correct combinations

    # for printing a specifc way
    index_to_str = 0 
    combo_to_str = 0

    # for alignment
    index_len = 0 
    nr_len = 0

    f_nr = 0 # keep track of file numbers
    contin = 1 # wether to continue checking files or not

    out_filename = input("\nOutput file: ")
    output_file = open(out_filename, "a")

    while(contin == 1):
        print(f_nr+1, end="") 
        filename = input(" Input file: ")  

        if os.path.isfile(filename):
            f_nr = f_nr + 1

            with open(filename, "r") as f: 
                num = f.read()
            numbers = [int(j) for j in num.split()]

            if max(numbers)<=N_max and min(numbers)>=N_min: # the elements should fit into the interval
                numero = numbers # just in case numbers gets lost
                index_tracker = []

                for i in range(len(numbers)):
                    index_tracker.append(i) # pushing values to the list, in this case they work like indexes
                f.close()

                while True: # validation
                    try:
                        M = int(input("Number of elements in a combination M: "))
                    except ValueError:
                        print("Not a number")
                    else:
                        break
                
                if(M>len(numero)):  # otherwise there wont be correct combos, when it wants to add 7 elements when there are only 5 in the array
                    print("M is too large for the file") # M > N
                else: 
                    while True:
                        try:
                            S = int(input("Sum S: "))
                        except ValueError:
                            print("Not a number")
                        else:
                            break

                    print("*****************************************************************************************", file = output_file)
                    print("The file being checked:", filename, file = output_file)
                    print("Part I", file = output_file)
                    print("Out of N integers given, pick M numbers so that their sum would be S", file = output_file)
                    print("User inputs filename (out of which the program will gather N integers from), numbers M and S", file = output_file)
                    print ("Numbers in the file: ", numbers)
                    print ("Numbers in the file: ", numbers, file = output_file)
                    print("N = ", len(numero), ". M = ", M, ". S = ", S, ".", sep="", file = output_file) # sep is seperator
                    
                    max_len_n = len(str(max(numero))) # for number allignment
                    max_len_i = len(str(len(numero))) # for index allignment

                    negative = 0
                    if(min(numero)<0):
                        negative = 1
                        min_len_n = len(str(min(numero))) #if theres a negative, it can make the string longer with -
                        max_len_n = max(max_len_n, min_len_n)
                    
                    step_tracker = [0]
                    depth_tracker = [0]
                    
                    print("Part II", file = output_file)
                    combinations(numbers, index_tracker, S, M)
                    remove_repetition()
                    printscreen_combos()

                    # erase everything so we can start all over again
                    step_tracker.clear()
                    depth_tracker.clear()
                    index_tracker.clear()
                    negative=0
            else:
                print ("File elements don't fit into the interval [-99; 99]")

            while True:
                    try:
                        contin = int(input("\nKeep analyzing?\n1. Yes\n2. No:\n"))
                    except ValueError:
                        print("Not a number")
                    else:
                        break
            print("")
        else:
            print ("File doesn't exist, try again")
        sum_combo.clear()
        sum_index.clear()
    output_file.close()
