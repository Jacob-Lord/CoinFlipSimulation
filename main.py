import time
import random

def timeEfficiency(funcName, *args, **kwargs):
    '''
    Desc: Takes a function and any number of parameters and measures the
      time efficiency based on the difference of the start and end times.
    '''
    num = []
    
    #store argument in num
    for i in args:
        num.append(i)

    start_time = time.time() #record starting time
    val = funcName(*args) #test fxn
    end_time = time.time() #record finish time
    total_ttc = end_time - start_time # difference of final and start is total time to complete
    print('Function: ' + str(funcName))
    print('Start time: ' + str(start_time) + '\tEnd time: ' + str(end_time) + '\tTime Efficiency: ' + str(total_ttc) + '\n')

    return val

def init_rand_nums(n):
    '''
    Generates n amount of random float numbers and stores them in a list
    Parameters: num_list - empty list to store nums
                n - amount of numbers to generate
    Returns: list with n amount of random float values
    '''
    num_list = []
    for i in range(n):
        #time.sleep(0.1) #random() runs off of system time, so sleeping for a tenth of a second adds entropy to num_list
        rand_val = random.random()
        num_list.append(rand_val)

    return num_list

def simulate_coinflip(num_list):
    result = ''
    result_list = []
    #iterate through random number list and assign flip according to value
    for i in num_list:
        #if value is 0-0.4999 flip is a heads
        if (i < 0.5):
            result = 'H'
        #if value is 0.5 or greater than it is tails
        else:
            result = 'T'

        #add coin flip result to final list
        result_list.append(result)

    return result_list

def analyze_results(result_list):
    '''
    Desc: Analyze the coin flip results and provide insight on distribution of coin flips
    Parameters: result_list - a list containing 'H' or 'T' char values to represent heads or tails
    '''
    total_amt = len(result_list)
    head_amt = 0
    tail_amt = 0

    for i in result_list:
        if (i == 'H'):
            head_amt += 1
        else:
            tail_amt += 1
    
    head_pct = (head_amt / total_amt)
    tail_pct = (tail_amt / total_amt)

    print("The distribution after " + str(total_amt) + " tries is " + str(head_pct * 100) + "% for heads and " + str(tail_pct * 100) + "% for tails.")

def main():

    #set number of trials
    NUM_TRIALS = 1000000

    #initialize random numbers to simulate uniform probabilities.
    num_list = timeEfficiency(init_rand_nums, NUM_TRIALS)

    #simulate coin flip n times where n is NUM_TRIALS
    result_list = timeEfficiency(simulate_coinflip, num_list)

    #analyze results of simulation
    analyze_results(result_list)


main()



