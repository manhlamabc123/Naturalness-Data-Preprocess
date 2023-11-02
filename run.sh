#!/bin/bash

clear

for i in {0..7}
do
  python main.py \
    -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/save/linux \
    -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/bonus \
    -project linux \
    -file_name "repo_commits_$i.pkl"
done
