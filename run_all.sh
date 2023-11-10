#!/bin/bash

bash run.sh $1

bash merge.sh $1

python commit_ids.py -c $1

python merge_split.py -c $1