import pickle
from icecream import ic

# Define the path to your .pkl file
file_path = '/home/manh/Documents/Data/linux-recrawl/bug-fix/commit_ids.pkl'

# Load data from the .pkl file
with open(file_path, 'rb') as file:
    loaded_data = pickle.load(file)

# Now, 'loaded_data' contains the data from the .pkl file
non_standard_commits = []

for commit_hash in loaded_data.keys():
    value = loaded_data[commit_hash]
    if value == -3:
        non_standard_commits.append(commit_hash)

ic(len(non_standard_commits))
    
# Export non_standard_commits as a .pkl file
with open('/home/manh/Documents/Data/linux-recrawl/bug-fix/non_standard_commit_ids.pkl', 'wb') as file:
    pickle.dump(non_standard_commits, file)
