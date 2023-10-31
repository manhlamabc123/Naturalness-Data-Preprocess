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

ic(len(bug_commit_ids))
ic(bug_commit_ids[:5])
ic(len(fix_commit_ids))
ic(fix_commit_ids[:5])

ids, labels, messages, codes = preprocessed_commits

ic(len(ids))

ic(labels[:10])

# Convert the lists to sets
set1 = set(bug_commit_ids)
set2 = set(fix_commit_ids)
set3 = set(ids)

# Find the common elements
common_elements = set3.intersection(set1)

# Get the count of common elements
count_common_elements = len(common_elements)

ic(count_common_elements)

# Find the common elements
common_elements = set3.intersection(set2)

# Get the count of common elements
count_common_elements = len(common_elements)

ic(count_common_elements)

# relabels = []

# for index, commit_hash in enumerate(ids):
    
#     if commit_hash in bug_commit_ids:
#         relabels.append('bug')
#     if commit_hash in fix_commit_ids:
#         relabels.append('fix')

# ic('bug' in relabels)
# ic('fix' in relabels)

# relabeled_commits = [ids, relabels, messages, codes]

# ic(relabels[:10])
    
# # Export non_standard_commits as a .pkl file
# with open('relabeled_commit_ids.pkl', 'wb') as file:
#     pickle.dump(relabeled_commits, file)
