# Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8 
# PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the 
# party venue within this time which takes him P minutes. The contest comprises 
# of N problems that are arranged in order of difficulty, with problem 1 being the 
# simplest and problem N being the most difficult. Max is aware that he will require 5*i 
# minutes to solve the ith problem.
# Your task is help Max find and return an integer value, representing the number of 
# problems Max can solve and reach the party venue within the given time frame of 4 
# hours.
# Note: Max will leave his home at exactly 8 PM to reach the party venue.
# Input Format:
# input1: An integer value N, representing the total number of problems.
# input2: An integer value P, Representing the time to travel in minutes from his home 
# to the party venue.
# Example Input:
# 6
# 180
# Output:
# 4

def num_problems(n,p):
    total_time=240
    remaining_time=240-p
    time_taken=p
    c=0
    
    for i in range(1,n+1):
        time_taken=time_taken+(i*5)
        remaining_time=total_time-time_taken
        if remaining_time>0:
            c=c+1
    return c
n=int(input())
p=int(input())
print(num_problems(n,p))     



