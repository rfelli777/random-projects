#interval_timer program

import time

# i declared as loc var in func below
f= int(input('how many seconds do you want timer? '))
r_count=0
r_tot= int(input('# intervals rounds? '))

print('tot time ='+ str(f*r_tot)+ " sec")
t= input('start timer? y/n ')




# mnemonic: remember to group & visualize to connect concepts!

def timer():
	i=f	 		
				#NOTE: when using funciton-reset count w/local variables
	while i>0: 	#NOTE: convert strings to variables (done in glob var)
		print(i)
		i -= 1
		time.sleep(1)

while t == 'y' and r_count != r_tot:
	print('new timer:')
	timer()
	r_count += 1
	print('BEEP')				#ADD BEEP
	print('timer '+ str(r_count)+ ' just finished')

print('done!')


#to-do
#	1. create UI on website
# 		mimic after interval timer website
#	2. create beeps