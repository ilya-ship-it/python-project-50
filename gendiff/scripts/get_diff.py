def get_diff(fisrt_file, second_file):
    keys = sorted(set(fisrt_file.keys()).union(second_file.keys()))
    diff = {}

    for key in keys:
        if key in fisrt_file and key not in second_file:
            diff[key] = ('removed', fisrt_file[key])
        elif key not in fisrt_file and key in second_file:
            diff[key] = ('added', second_file[key])
        elif fisrt_file[key] == second_file[key]:
            diff[key] = ('unchanged', fisrt_file[key])
        elif isinstance(fisrt_file[key], dict) and isinstance(second_file[key], dict):
            diff[key] = ('nested', get_diff(fisrt_file[key], second_file[key]))
        else:
            diff[key] = ('changed', (fisrt_file[key], second_file[key]))
    return diff