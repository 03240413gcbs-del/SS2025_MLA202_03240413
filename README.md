MLA202 Reinforcement Learning
Sonam Rinzin Lhendup
03240413

#Reflection #A brief summary of the tasks you completed?
I printed the action space and observation space after making changes to the provided FrozenLake code in accordance with Exercise 1.  I made an outer loop to run the code a thousand times in exercise 2.  Since we know how many times the loop will run, I choose to use a while loop.  A variable named num_episode was also established by me to monitor which track the function is running on.  In order to speed up the env.render(), print(), and sleep() functions, I have also eliminated time.

#The answers to the questions from Exercise 1 about the CartPole environment's action and observation spaces.
The four continuous spaces are as follows: #1. Cart position: the distance from the center; #2. Cart velocity: the speed at which the cart is moving to the left or right; #3. Pole angle: the pole's title; and #4. Pole angular velocity: the speed at which the pole rotates.

#The final average reward you calculated for the random agent in Exercise 2.
Average reward over 1000 episodes: 0.0080


#Q.A section on challenges: What was the most difficult part of this practical for you? (e.g., setting up the environment, understanding the step function's return values, structuring the loops).
Understanding and utilizing the return values from the step() method in the loop was the most challenging aspect of this practical.  The episode initially flowed poorly since I wasn't sure how to manage the information, truncation, termination, reward, and observation values.  Another challenging task was making sure the loop finished at the appropriate moment.  I corrected this by reading the guide, examining the examples, and printing the results to observe how each value performed.

#A section on key takeaways: What is the most important or surprising thing you learned?
The step() method's control over the agent-environment interaction was the most significant lesson I took away from this practical.  The amount of information that was returned in a single call and the part that each component plays in controlling the episode amazed me.  Another surprising discovery was that the average total reward remained low even after 1000 iterations of the while loop.  It demonstrated to me that appropriate learning techniques are required to attain better outcomes and that the agent does not necessarily get better with more runs.

