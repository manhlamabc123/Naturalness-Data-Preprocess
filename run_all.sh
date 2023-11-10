#!/bin/bash

bash run.sh

bash merge.sh

python commit_ids.py

python merge_split.py