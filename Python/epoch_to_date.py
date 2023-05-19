#!/usr/bin/python3

#date = "5/19/2023 at 3:32:28"    #Unneeded date and epoch_time for calculating epoch time that passes each second.
#epoch_time = "1684524747.7698207"    #epoch time at time of date
#seconds_from_epoch_to_date = 1684510348


epoch_in_one_second = 1.0000085483415628   #Epoch time that passes in one second.

seconds_in_current_epoch_time = (time.time())/epoch_in_one_second

minutes_exact = seconds_in_current_epoch_time * 60

hours_exact = minutes * 60

days_exact = hours * 24

days = int(days_exact)

hours = days_exact - days

print("Current epoch time:", time.time())

print("Days since epoch:", days,  





