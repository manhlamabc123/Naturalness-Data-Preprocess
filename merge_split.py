import pickle
from icecream import ic
import pandas as pd

# data_dir = '/data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_3'
data_dir = '/home/manh/Documents/Data/naturalness'

# Load data from the .pkl file
with open(f'{data_dir}/linux_bonus.pkl', 'rb') as file:
    bonus = pickle.load(file)

with open(f'{data_dir}/linux_bug_fix_relabeled.pkl', 'rb') as file:
    bug_fix = pickle.load(file)

with open(f'{data_dir}/linux_normal.pkl', 'rb') as file:
    normal = pickle.load(file)

bonus_ids, bonus_labels, bonus_messages, bonus_commits = bonus
bug_fix_ids, bug_fix_labels, bug_fix_messages, bug_fix_commits = bug_fix
normal_ids, normal_labels, normal_messages, normal_commits = normal

ic(len(bonus_ids))
ic(len(bug_fix_ids))
ic(len(normal_ids))

bonus_df = pd.DataFrame({
    'commit_hash': bonus_ids,
    # 'message': bonus_messages,
    'commit': bonus_commits,
    'label': bonus_labels
})

ic(len(bug_fix_ids))
ic(len(bug_fix_messages))
ic(len(bug_fix_commits))
ic(len(bug_fix_labels))

bug_fix_df = pd.DataFrame({
    'commit_hash': bug_fix_ids,
    # 'message': bug_fix_messages,
    'commit': bug_fix_commits,
    'label': bug_fix_labels
})

normal_df = pd.DataFrame({
    'commit_hash': normal_ids,
    # 'message': normal_messages,
    'commit': normal_commits,
    'label': normal_labels
})

ic()
ic(bonus_df.shape)
ic(bug_fix_df.shape)
ic(normal_df.shape)

# Create a boolean mask to identify rows with 'label' equal to 'fix_bug'
mask = bug_fix_df['label'] != 'fix_bug'

# Use the mask to filter the DataFrame and keep only the rows where the condition is True
bug_fix_df = bug_fix_df[mask]

ic()
ic(bonus_df.shape)
ic(bug_fix_df.shape)
ic(normal_df.shape)

# Concatenate the DataFrames vertically
combined_df = pd.concat([bonus_df, bug_fix_df, normal_df], ignore_index=True)

ic()
ic(combined_df.shape)

# Use boolean indexing to update 'label' column
ic(combined_df['label'])

combined_df.loc[combined_df['label'] == 'bug', 'label'] = 1
combined_df.loc[combined_df['label'] != 1, 'label'] = 0

ic(combined_df['label'])

# Shuffle the DataFrame
ic(combined_df['commit_hash'])

shuffled_df = combined_df.sample(frac=1.0, random_state=42)  # Set a random_state for reproducibility

# Reset the index of the shuffled DataFrame
shuffled_df.reset_index(drop=True, inplace=True)

ic(shuffled_df['commit_hash'])

# Create a DataFrame with 'label' equal to 1
label_1_df = shuffled_df[shuffled_df['label'] == 1]

# Create a DataFrame with 'label' equal to 0
label_0_df = shuffled_df[shuffled_df['label'] == 0]

def split_dataframe(df, part1_ratio=0.75, part2_ratio=0.05, part3_ratio=0.20):
    """
    Split a DataFrame into three parts based on the specified ratios.

    Args:
    df (pd.DataFrame): The input DataFrame.
    part1_ratio (float): The proportion of rows for the first part (default is 0.75).
    part2_ratio (float): The proportion of rows for the second part (default is 0.05).
    part3_ratio (float): The proportion of rows for the third part (default is 0.20).

    Returns:
    pd.DataFrame, pd.DataFrame, pd.DataFrame: Three DataFrames representing the three parts.
    """
    total_rows = len(df)

    part1_rows = int(total_rows * part1_ratio)
    part2_rows = int(total_rows * part2_ratio)
    part3_rows = int(total_rows * part3_ratio)

    part1 = df.iloc[:part1_rows]
    part2 = df.iloc[part1_rows:part1_rows + part2_rows]
    part3 = df.iloc[part1_rows + part2_rows:]

    return part1, part2, part3

part1_1, part2_1, part3_1 = split_dataframe(label_1_df)
part1_0, part2_0, part3_0 = split_dataframe(label_0_df)

# Concatenate the corresponding parts from label_1_df and label_0_df
concatenated_part1 = pd.concat([part1_0, part1_1], ignore_index=True)
concatenated_part2 = pd.concat([part2_0, part2_1], ignore_index=True)
concatenated_part3 = pd.concat([part3_0, part3_1], ignore_index=True)

def calculate_label_ratio(df):
    """
    Calculate the ratio of 'label' equal to 1 to 'label' equal to 0 in a DataFrame.

    Args:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    float or str: The ratio of label 1 to label 0 if label 0 is not 0; otherwise, "Undefined."
    """
    # Count the number of 'label' equal to 1
    count_label_1 = len(df[df['label'] == 1])

    # Count the number of 'label' equal to 0
    count_label_0 = len(df[df['label'] == 0])

    # Calculate the ratio
    label_1_ratio = count_label_1 / count_label_0 if count_label_0 != 0 else "Undefined"

    return label_1_ratio

ic()
ic(concatenated_part1.shape)
ic(calculate_label_ratio(concatenated_part1))
ic(concatenated_part2.shape)
ic(calculate_label_ratio(concatenated_part2))
ic(concatenated_part3.shape)
ic(calculate_label_ratio(concatenated_part3))

# Shuffle the concatenated DataFrames
shuffled_part1 = concatenated_part1.sample(frac=1, random_state=42).reset_index(drop=True)
shuffled_part2 = concatenated_part2.sample(frac=1, random_state=42).reset_index(drop=True)
shuffled_part3 = concatenated_part3.sample(frac=1, random_state=42).reset_index(drop=True)

ic()
ic(shuffled_part1.shape)
ic(calculate_label_ratio(shuffled_part1))
ic(shuffled_part2.shape)
ic(calculate_label_ratio(shuffled_part2))
ic(shuffled_part3.shape)
ic(calculate_label_ratio(shuffled_part3))

train_ids, train_labels, train_messages, train_commits = shuffled_part1['commit_hash'].tolist(), shuffled_part1['label'].tolist(), [], shuffled_part1['commit'].tolist()
validate_ids, validate_labels, validate_messages, validate_commits = shuffled_part2['commit_hash'].tolist(), shuffled_part2['label'].tolist(), [], shuffled_part2['commit'].tolist()
test_ids, test_labels, test_messages, test_commits = shuffled_part3['commit_hash'].tolist(), shuffled_part3['label'].tolist(), [], shuffled_part3['commit'].tolist()

ic()
ic(len(train_ids))
ic(len(train_labels))
ic(len(train_messages))
ic(len(train_commits))

train = [train_ids, train_labels, train_messages, train_commits]
validate = [validate_ids, validate_labels, validate_messages, validate_commits]
test = [test_ids, test_labels, test_messages, test_commits]

pickle.dump(train, open(f"{data_dir}/linux_train.pkl", 'wb'))
pickle.dump(validate, open(f"{data_dir}/linux_val.pkl", 'wb'))
pickle.dump(test, open(f"{data_dir}/linux_test.pkl", 'wb'))