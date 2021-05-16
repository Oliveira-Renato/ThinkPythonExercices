#3. If I leave my house at **6:52 am and run **1 mile at an easy pace **(8:15 per mile), then **3 miles at tempo **(7:12 per mile) and **1 mile at easy pace again, what time do I get home for breakfast?
inicial_time = 6.52 
easy_pace = 8.15
pace_tempo = 7.12
total_run = (easy_pace * 2) + (pace_tempo * 3)
total_run_time = (total_run / 24) + inicial_time 

print('You gonna get home at {:.2f} am'.format(total_run_time))