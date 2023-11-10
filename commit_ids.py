import pickle
from icecream import ic
from tqdm import tqdm

bug_file_name = 'bug_commit_ids.pkl'
fix_file_name = 'fix_commit_ids.pkl'
# data_dir = '/data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/fixed'
data_dir = '/home/manh/Documents/Data/naturalness/context_5/bug_fix'
preprocessed_file_name = f'{data_dir}/linux_bug_fix.pkl'

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

for index, commit_hash in enumerate(tqdm(ids)):
    if (commit_hash in bug_commit_ids) and (commit_hash in fix_commit_ids):
        relabels.append('fix-bug')
    elif commit_hash in bug_commit_ids:
        relabels.append('bug')
    elif commit_hash in fix_commit_ids:
        relabels.append('fix')

ic(relabels.count('bug'))
ic(relabels.count('fix'))
ic(relabels.count('fix-bug'))
ic(relabels.count('normal'))

relabeled_commits = [ids, relabels, messages, codes]

# # Split 'relabeled_commits' into three parts (e.g., first 0-10k, 10k-20k, 20k-end)
# relabeled_commits_part1 = [ids[:25000], relabels[:25000], messages[:25000], codes[:25000]]
# relabeled_commits_part2 = [ids[25001:50000], relabels[25001:50000], messages[25001:50000], codes[25001:50000]]
# relabeled_commits_part3 = [ids[500001:], relabels[500001:], messages[500001:], codes[500001:]]

# # Export each part as a .pkl file
# with open('relabeled_commits_part1.pkl', 'wb') as file:
#     pickle.dump(relabeled_commits_part1, file)

# with open('relabeled_commits_part2.pkl', 'wb') as file:
#     pickle.dump(relabeled_commits_part2, file)

# with open('relabeled_commits_part3.pkl', 'wb') as file:
#     pickle.dump(relabeled_commits_part3, file)

# Export non_standard_commits as a .pkl file
with open(f'{data_dir}/linux_bug_fix_relabeled.pkl', 'wb') as file:
    pickle.dump(relabeled_commits, file)
