import os, pickle

# Specify the folder path
folder_path = '/home/manh/Documents/Data/ratna-data/linux_commit_change/bug_commit_change'  # Replace with the actual folder path

# Create an empty list to store file names
file_names = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_names.append(filename)

print(len(file_names))

# Export non_standard_commits as a .pkl file
with open('bug_commit_ids.pkl', 'wb') as file:
    pickle.dump(file_names, file)
