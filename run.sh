# #!/bin/bash

# clear

# for i in {0..7}
# do
#   python main.py \
#     -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/save/bonus_linux \
#     -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_$1/bonus \
#     -project linux \
#     -context $1 \
#     -file_name "repo_commits_$i.pkl"
# done

# clear

# for i in {0..7}
# do
#   python main.py \
#     -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/save/normal_linux \
#     -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_$1/normal \
#     -project linux \
#     -context $1 \
#     -file_name "repo_commits_$i.pkl"
# done

# clear

# for i in {0..14}
# do
#   python main.py \
#     -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/JIT-DP-DataCrawling/save/bug_fix_linux \
#     -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_$1/bug_fix \
#     -project linux \
#     -context $1 \
#     -file_name "repo_commits_$i.pkl"
# done

#!/bin/bash

projects=("gerrit" "go" "jdt" "platform" "openstack" "qt" "linux")
selected_values=(1 3 5 10)

for project in "${projects[@]}"
do
  for i in "${selected_values[@]}"
  do
    python main.py \
      -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/raw \
      -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_$i \
      -project $project \
      -context $i \
      -csv_file /data/gpfs/projects/punim1928/RISE/JITDP/data/lapredict-paper/$project/$project_k_feature.csv \
      -file_name "${project}.pkl"
  done
done

python main.py \
  -data_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/raw \
  -save_dir /data/gpfs/projects/punim1928/RISE/JITDP/data/naturalness/context_1 \
  -project gerrit \
  -context 1 \
  -file_name "gerrit.pkl" \
  -debug