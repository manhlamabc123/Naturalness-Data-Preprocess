#!/bin/bash

clear

for i in {0..7}
do
  python main.py \
    -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/save/bonus_linux \
    -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_0/bonus \
    -project linux \
    -context 0 \
    -file_name "repo_commits_$i.pkl"
done

clear

for i in {0..7}
do
  python main.py \
    -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/save/normal_linux \
    -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_0/normal \
    -project linux \
    -context 0 \
    -file_name "repo_commits_$i.pkl"
done

clear

for i in {0..14}
do
  python main.py \
    -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/save/bug_fix_linux \
    -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_0/bug_fix \
    -project linux \
    -context 0 \
    -file_name "repo_commits_$i.pkl"
done