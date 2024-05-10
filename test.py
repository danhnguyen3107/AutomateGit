import os

# Define the directory path
dir_path = 'D:/Repository/'

# Change the current working directory
os.chdir(dir_path)

# Define the new folder name
new_folder = 'repo-name'

# Create a new folder in the current working directory
os.makedirs(new_folder)