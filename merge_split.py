import pickle
from icecream import ic
from tqdm import tqdm
import pandas as pd

# Load data from the .pkl file
with open('/data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_3/linux_bonus.pkl', 'rb') as file:
    bonus = pickle.load(file)

with open('/data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_3/linux_bug_fix.pkl', 'rb') as file:
    bug_fix = pickle.load(file)

with open('/data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_3/linux_normal.pkl', 'rb') as file:
    normal = pickle.load(file)

bonus_ids, bonus_messages, bonus_commits, bonus_labels = bonus
bug_fix_ids, bug_fix_messages, bug_fix_commits, bug_fix_labels = bug_fix
normal_ids, normal_messages, normal_commits, normal_labels = normal

ic(len(bonus_ids))
ic(len(bug_fix_ids))
ic(len(normal_ids))