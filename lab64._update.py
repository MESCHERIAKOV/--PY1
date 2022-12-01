import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    lod = []
    lor = []
    with open(filename, 'r') as f:
        result = f.readlines()
        headers = result[0].rstrip().split(sep=',')
        for row in result[1:]:
            lor.append(row.rstrip().split(sep=','))
        for element in lor:
            a = {k:v for k, v in zip(headers, element)}
            lod.append(a)
         
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))