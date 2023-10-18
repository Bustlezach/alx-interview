#!/usr/bin/python3

def print_metrics(dic, total_size):
    """
    This function prints the metric stats
    """
    print(f'File size: {total_size}')
    for key in dic.keys():
        print(f'{key}: {dic[key]}')


dic = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_size = 0
count = 0

try:
    with open(0) as file:
        for line in file:
            arr = line.split()
            count += 1
            try:
                total_size += int(arr[-1])
            except:
                pass
            try:
                if arr[-2] in dic:
                    dic[arr[-2]] += 1
            except:
                pass
            try:
                if count % 10 == 0:
                    print_metrics(dic, total_size)
            except:
                print_metrics(dic, total_size)
except KeyboardInterrupt:
    print_metrics(dic, total_size)
    raise
