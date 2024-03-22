import os
from random import randint
from datetime import datetime, timedelta

# Change directory to the repository
repo_path = "/Users/akramyakhyaev/PycharmProjects/pythonProject/"
os.chdir(repo_path)

# Loop through each day of the past year
for i in range(1, 366):
    # Generate a random number of commits for each day
    for _ in range(randint(1, 5)):
        # Calculate the commit date
        commit_date = datetime.now() - timedelta(days=i)
        # Format the commit date
        formatted_date = commit_date.strftime('%a, %d %b %Y %H:%M:%S %z')

        # Write commit message to file
        with open('file.txt', 'a') as file:
            file.write(f'Commit on {formatted_date}\n')

        # Add the file to the staging area
        os.system('git add file.txt')
        # Commit with the specified date
        os.system(f'GIT_COMMITTER_DATE="{formatted_date}" git commit -m "Commit on {commit_date}"')
        # Push changes to the remote repository
        os.system('git push origin main')
