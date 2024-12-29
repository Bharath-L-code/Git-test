import os
import random

def makeCommits(days: int):
    if days < 1:
        os.system('git push')  # Push commits once done
        return 0  # Base case returns 0 to avoid NoneType
    else:
        dates = f"{days} days ago"
        
        # Get a random number of commits for today between 1 and 10
        num_commits = random.randint(1, 10)
        
        with open('data.txt', 'a') as file:
            for i in range(num_commits):
                file.write(f'{dates} <- this was commit number {i + 1} for the day!!\n')

        # Stage the file (you might want to stage at the start or after all commits)
        os.system('git add data.txt')

        # Commit multiple times with the same date
        for i in range(num_commits):
            os.system(f'git commit --date="{dates}" -m "First commit for the day, commit number {i + 1}!"')

        # Recursive call to make commits for the next day
        return 1 + makeCommits(days - 1)  # Add 1 for this day

# Start the process with 300 days
makeCommits(300)
