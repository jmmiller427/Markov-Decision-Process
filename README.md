# Markov-Decision-Process

This code starts out by defining a Reward State and empty direction matrix. A nested for loop then runs through the length of the reward state matrix. For each position of the matrix, calculate the surrounding values. If there is a wall then check if a successful forward movement is found from bouncing off the wall back to the same state. Calculate the forward state, then the oppostite direction, and the probability of it staying in the same state. This total is multiplied by the gamma value and added to the reward for that state. This gives the directions it should go. 

The gamma value used to find V^6 was 1 and the gamma value used to find V^* was 0.96. Graphs for the value function and corresponding policies are found below:

	V^6:

		96.0  138.5 207.5 284.8 
		139.7 188.7 253.5 333.7 
		197.9 169.7 195.2 255.1 
		254.9 194.9 155.9 199.8 

	 	v   >   >   v  
	 	v   >   >   >  
	 	v   <   >   ^  
	 	v   <   <   ^ 

	 V^*:

	 	869.28 921.02 990.64  1065.04 
		913.24 967.59 1033.34 1113.6 
		892.80 923.72 972.68  1037.18
		932.71 889.05 921.69  985.92

		 >   >   >   v  
		 >   >   >   >  
		 v   >   >   ^  
		 v   <   >   ^ 
