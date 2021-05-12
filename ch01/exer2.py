#1. How many seconds are there in 42 minutes 42 seconds?

#print((42 * 60) + 42) 2562
totalSeconds = 42.42 * 60

#2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
mile = 1.61
totalMiles = 10 * mile
#print('There are {} miles in 10km'.format(totalMiles))

#3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time permile in minutes and seconds)? What is your average speed in miles per hour?

secondMin = ( totalSeconds % 60) / 100
totalMinute = (totalSeconds/ 60 )
avgPace = (totalMinute / totalMiles ) - secondMin 
avgSpeed = (totalMiles  / (totalMinute / 60)) - secondMin


print('the average pace is {:.2f} mile/minutes and seconds'.format(avgPace))
print('the average speed is {:.2f} mile/hour'.format(avgSpeed ))


