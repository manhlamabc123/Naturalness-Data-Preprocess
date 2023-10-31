import pickle, argparse
from icecream import ic
from tqdm import tqdm

def read_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-data_dir', type=str, default='/home/manh/Documents/Data/splited-tan-dataset')
    parser.add_argument('-project', type=str, default='bootstrap')
    parser.add_argument('-file_names', type=str, default=[], nargs='+')

    return parser

def main():
    params = read_args().parse_args()

    data_dir = params.data_dir
    project = params.project
    file_names = params.file_names

    ic(data_dir)
    ic(project)
    ic(file_names)

    ids, labels, messages, commits = [], [], [], []

    for file_name in file_names:
        file_path = f"{data_dir}/{project}/{file_name}.pkl"

        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)
                temp_ids, temp_labels, temp_messages, temp_commits = data
                
                ids += temp_ids
                labels += temp_labels
                messages += temp_messages
                commits += temp_commits
                
                # Process the project_data as needed
                ic(f"Loaded data for project: {file_path}")
        except FileNotFoundError:
            ic(f"File not found for project: {file_path}")

    concated_data = ids, labels, messages, commits

    ic(len(ids))
    ic(pickle.dump(concated_data, open(f"{data_dir}/{project}/linux_normal.pkl", 'wb')))

if __name__ == "__main__":
    main()