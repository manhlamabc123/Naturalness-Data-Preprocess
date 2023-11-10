#!/bin/bash

python combine.py \
    -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/data \
    -project naturalness/context_0/bug_fix \
    -output_file_name linux_bug_fix \
    -file_names "repo_commits_0_preprocessed" "repo_commits_1_preprocessed" "repo_commits_2_preprocessed" "repo_commits_3_preprocessed" "repo_commits_4_preprocessed" "repo_commits_5_preprocessed" "repo_commits_6_preprocessed" "repo_commits_7_preprocessed" "repo_commits_8_preprocessed" "repo_commits_9_preprocessed" "repo_commits_10_preprocessed" "repo_commits_11_preprocessed" "repo_commits_12_preprocessed" "repo_commits_13_preprocessed" "repo_commits_14_preprocessed"

python combine.py \
    -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/data \
    -project naturalness/context_0/normal \
    -output_file_name linux_normal \
    -file_names "repo_commits_0_preprocessed" "repo_commits_1_preprocessed" "repo_commits_2_preprocessed" "repo_commits_3_preprocessed" "repo_commits_4_preprocessed" "repo_commits_5_preprocessed" "repo_commits_6_preprocessed" "repo_commits_7_preprocessed"

python combine.py \
    -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/data \
    -project naturalness/context_0/bonus \
    -output_file_name linux_bonus \
    -file_names "repo_commits_0_preprocessed" "repo_commits_1_preprocessed" "repo_commits_2_preprocessed" "repo_commits_3_preprocessed" "repo_commits_4_preprocessed" "repo_commits_5_preprocessed" "repo_commits_6_preprocessed" "repo_commits_7_preprocessed"