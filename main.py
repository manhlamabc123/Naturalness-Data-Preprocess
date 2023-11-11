import argparse, pickle
from icecream import ic
from process_diff import *
from tqdm import tqdm


def read_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-data_dir', type=str, default='', help='')
    parser.add_argument('-save_dir', type=str, default='', help='')
    parser.add_argument('-project', type=str, default='', help='')
    parser.add_argument('-file_name', type=str, default='', help='')
    parser.add_argument('-context', type=int, default=3, help='')
    parser.add_argument('-debug', action='store_true', help='')

    return parser

def main():
    params = read_args().parse_args()
    data_dir = params.data_dir
    save_dir = params.save_dir
    project = params.project
    file_name = params.file_name
    num_context = params.context
    debug = params.debug

    ic(data_dir)
    ic(project)
    ic(file_name)
    ic(num_context)

    # Load data from the .pkl file
    with open('bug_commit_ids.pkl', 'rb') as file:
        bug_commit_ids = pickle.load(file)

    with open('fix_commit_ids.pkl', 'rb') as file:
        fix_commit_ids = pickle.load(file)

    with open('fix_bug_commit_ids.pkl', 'rb') as file:
        fix_bug_commit_ids = pickle.load(file)

    ids = []
    labels = []
    messages = []
    commits = []

    if debug:
        ic.enable()
    else:
        ic.disable()

    try:
        with open(f'{data_dir}/{file_name}', 'rb') as file:
            loaded_data = pickle.load(file)

        for commit_hash in tqdm(loaded_data.keys()):
            ic(commit_hash)
            ids.append(commit_hash)
            hunks = []

            ic(loaded_data[commit_hash].keys())

            message = loaded_data[commit_hash]['msg']
            message = message.strip()
            message = split_sentence(message)
            message = ' '.join(message.split(' ')).lower()

            for file in loaded_data[commit_hash]['diff'].keys():
                ic(file)
                hunk = {}
                hunk['file_name'] = file
                hunk['code_changes'] = []

                processed_diff = process_content(loaded_data[commit_hash]['diff'][file]['content'], surrounding_lines=num_context)

                for file_code in processed_diff:
                    ic(file_code)
                    code_changes = {}
                    after, before = [], []

                    for code in file_code:
                        # ic(code)
                        if 'a' in code or 'b' in code or 'ab' in code:
                            code_key = str(list(code.keys())[0])
                        else:
                            ic('Empty dict')
                            continue
                        # ic(code_key)
                        
                        if code_key == 'a':
                            after += code[code_key]
                        elif code_key == 'b':
                            before += code[code_key]
                        else:
                            after += code[code_key]
                            before += code[code_key]

                    ic(after)
                    ic(before)
                    
                    processed_after, processed_before = [], []
                    for a_line, b_line in zip(after, before):
                        # ic(a_line)
                        # ic(b_line)
                        # ic(type(a_line))
                        # ic(type(b_line))
                        a_line, b_line = a_line.strip(), b_line.strip()
                        # ic(a_line)
                        # ic(b_line)
                        a_line, b_line = ' '.join(split_sentence(a_line).split()), ' '.join(split_sentence(b_line).split())
                        # ic(a_line)
                        # ic(b_line)
                        a_line, b_line = ' '.join(a_line.split(' ')), ' '.join(b_line.split(' '))
                        # ic(a_line)
                        # ic(b_line)
                        processed_after.append(a_line)
                        processed_before.append(b_line)
                    
                    ic(processed_after)
                    ic(processed_before)
                    
                    code_changes['before'] = processed_before
                    code_changes['after'] = processed_after

                    hunk['code_changes'].append(code_changes)

                hunks.append(hunk)

            ic(hunks)
            if project == 'linux':
                if commit_hash in fix_bug_commit_ids:
                    labels.append('fix-bug')
                elif commit_hash in bug_commit_ids:
                    labels.append('bug')
                elif commit_hash in fix_commit_ids:
                    labels.append('fix')
                else:
                    labels.append('normal')
            messages.append(message)
            commits.append(hunks)

            if debug:
                break

        ic(commits)
    except FileNotFoundError:
        ic.enable()
        ic(f"File {file_name} not found.")
    except Exception as e:
        ic.enable()
        ic(commit_hash)
        ic(e)

    preprocessed_train = [ids, labels, messages, commits]

    if not os.path.exists(f"{save_dir}"):
        os.makedirs(f"{save_dir}")

    pickle.dump(preprocessed_train, open(f"{save_dir}/{file_name.split('.')[0]}_preprocessed.pkl", 'wb'))

if __name__ == "__main__":
    main()