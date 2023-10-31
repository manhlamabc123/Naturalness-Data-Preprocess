import pickle
from icecream import ic

bug_file_name = 'bug_commit_ids.pkl'
fix_file_name = 'fix_commit_ids.pkl'
preprocessed_file_name = '/data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/bug-fix/linux_bug-fix.pkl'

# Load data from the .pkl file
with open(bug_file_name, 'rb') as file:
    bug_commit_ids = pickle.load(file)

with open(fix_file_name, 'rb') as file:
    fix_commit_ids = pickle.load(file)

with open(preprocessed_file_name, 'rb') as file:
    preprocessed_commits = pickle.load(file)

ic(len(bug_file_name))
ic(len(fix_file_name))

ids, labels, messages, codes = preprocessed_commits

ic(len(ids))

ic(labels[:10])

for index, commit_hash in enumerate(ids):
    if commit_hash in bug_commit_ids:
        labels[index] = 'bug'
    if commit_hash in fix_commit_ids:
        labels[index] = 'fix'

relabeled_commits = [ids, labels, messages, codes]

ic(labels[:10])
    
# Export non_standard_commits as a .pkl file
with open('relabeled_commit_ids.pkl', 'wb') as file:
    pickle.dump(relabeled_commits, file)
