import gymnasium as gym
import time

env = gym.make("FrozenLake-v1", render_mode="human")

print(f"Action Space: {env.action_space}")
# Q1: What type of space is the action space? How many actions are there?
# - The action space is Discrete(2).
# - This means there are 2 possible actions:
#     0 → Push the cart to the left
#     1 → Push the cart to the right
# ===========================
print(f"Observation Space: {env.observation_space}")
# Q2: What type of space is the observation space?
# - The observation space is Box(4,).
# - This represents a continuous space with 4 values.
# - These four numbers correspond to:
#     1. Cart Position (where the cart is on the track)
#     2. Cart Velocity (speed and direction of the cart’s movement)
#     3. Pole Angle (the angle of the pole from vertical)
#     4. Pole Angular Velocity (how fast the pole is falling or rising)
# ===========================

# --- THE MAIN LOOP ---


observation, info = env.reset()


terminated = False
truncated = False
total_reward = 0.0


while not terminated and not truncated:
    
    env.render()

    
    action = env.action_space.sample()
    print(f"Taking action: {action} (0:L, 1:D, 2:R, 3:U)")

    
    next_observation, reward, terminated, truncated, info = env.step(action)

    
    total_reward += reward
    observation = next_observation

    
    time.sleep(5)


print(f"\nEpisode finished! Total Reward: {total_reward}")


env.close()
# Q3: What does the reward represent?
# - In CartPole, the agent receives a reward of +1 for every timestep
#   that the pole remains upright and the cart stays within bounds.
# - The total reward at the end of the episode equals the number of
#   steps the agent successfully balanced the pole.
# ===========================