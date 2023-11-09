#!/bin/bash

clear

for i in {0..14}
do
  python main.py \
    -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/save/bug_fix_linux \
    -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_5/ \
    -project bug_fix_linux \
    -context 5 \
    -file_name "repo_commits_$i.pkl"
done
