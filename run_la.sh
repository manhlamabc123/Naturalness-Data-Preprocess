#!/bin/bash

clear

python main.py \
  -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/git_datasets/jdt \
  -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/lapredict_dataset \
  -project jdt \
  -context 3 \
  -file_name jdt.pkl