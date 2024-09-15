def get_diff(file_1, file_2):
    keys = sorted(set(file_1.keys()).union(file_2.keys()))
    diff = {}
    for key in keys:
        if key in file_1 and key not in file_2:
            diff[key] = ('removed', file_1[key])
        elif key not in file_1 and key in file_2:
            diff[key] = ('added', file_2[key])
        elif file_1[key] == file_2[key]:
            diff[key] = ('unchanged', file_1[key])
        elif isinstance(file_1[key], dict) and isinstance(file_2[key], dict):
            diff[key] = ('nested', get_diff(file_1[key], file_2[key]))
        else:
            diff[key] = ('changed', (file_1[key], file_2[key]))
    return diff
