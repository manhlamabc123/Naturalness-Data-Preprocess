import pickle
from icecream import ic

bug_file_name = 'bug_commit_ids.pkl'
fix_file_name = 'fix_commit_ids.pkl'
preprocessed_file_name = '/data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/bug-fix/linux_bug-fix.pkl'

# Load data from the .pkl file
with open(bug_file_name, 'rb') as file:
    bug_commit_ids = pickle.load(file)

bug_commit_ids = [item.split('.')[0] for item in bug_commit_ids]

with open(fix_file_name, 'rb') as file:
    fix_commit_ids = pickle.load(file)

fix_commit_ids = [item.split('.')[0] for item in fix_commit_ids]

with open(preprocessed_file_name, 'rb') as file:
    preprocessed_commits = pickle.load(file)

ic(len(bug_commit_ids))
ic(len(fix_commit_ids))

ids, labels, messages, codes = preprocessed_commits

ic(len(ids))

# Convert the lists to sets
set1 = set(bug_commit_ids)
set2 = set(fix_commit_ids)
set3 = set(ids)

# Find the common elements
common_elements = set3.intersection(set1)

# Get the count of common elements
bug_all = len(common_elements)

ic(bug_all)

# Find the common elements
common_elements = set3.intersection(set2)

# Get the count of common elements
fix_all = len(common_elements)

ic(fix_all)

# Find the common elements
common_elements = set1.intersection(set2)

# Get the count of common elements
bug_fix = len(common_elements)

ic(bug_fix)

relabels = []

for index, commit_hash in enumerate(ids):
    if commit_hash in bug_commit_ids:
        relabels.append('bug')
    if commit_hash in fix_commit_ids:
        relabels.append('fix')
    if (commit_hash in bug_commit_ids) and (commit_hash in fix_commit_ids):
        relabels.append('fix-bug')

ic(relabels.count('bug'))
ic(relabels.count('fix'))
ic(relabels.count('fix-bug'))

relabeled_commits = [ids, relabels, messages, codes]
    
# Export non_standard_commits as a .pkl file
with open('relabeled_commit_ids.pkl', 'wb') as file:
    pickle.dump(relabeled_commits, file)
