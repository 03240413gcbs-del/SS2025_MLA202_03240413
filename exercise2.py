import gymnasium as gym
import time

env = gym.make("FrozenLake-v1", render_mode="human")

print(f"Action Space: {env.action_space}")
print(f"Observation Space: {env.observation_space}")

# --- THE MAIN LOOP ---
num_episodes = 1000
episode=0
rewards_per_episode = []
while episode<=num_episodes:#outer loop
    episode=episode+1

    observation, info = env.reset()


    terminated = False
    truncated = False
    total_reward = 0.0


    while not terminated and not truncated:#inner loop
        action = env.action_space.sample()
        f"Taking action: {action} (0:L, 1:D, 2:R, 3:U)"


        next_observation, reward, terminated, truncated, info = env.step(action)


        total_reward += reward
        observation = next_observation
        # Append the final reward for this episode to the list
        rewards_per_episode.append(total_reward)






    print(f"\nEpisode finished! Total Reward: {total_reward}")
average_reward = sum(rewards_per_episode) / num_episodes 
print(f"Average reward over {num_episodes} episodes: {average_reward:.4f}")
env.close()