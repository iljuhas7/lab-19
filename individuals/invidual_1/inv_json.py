import json
import pathlib
import inv_jsonschema


def load(file_path: str) -> list:
    path = pathlib.Path(file_path)
    
    if not path.exists():
        return []

    with open(path.absolute(), "r", encoding="utf-8") as f:
        json_data = json.load(f)
        list_item = []

        for cur_json_data in json_data:
            msg = inv_jsonschema.test_msg(cur_json_data)

            if not (msg == 'ok'):
                print("[Error][Json]:", msg)
                return []

        for cur_json_data in json_data:
            list_item.append({
                'name': cur_json_data["name"],
                'group': cur_json_data["group"],
                'z': cur_json_data["z"],
            })

        return list_item


def save(file_path: str, obj: list) -> bool:
    path = pathlib.Path(file_path)
    
    if not (type(obj) == list):
        return False

    for cur_obj in obj:
        msg = inv_jsonschema.test_msg(cur_obj)

        if not (msg == 'ok'):
            print("[Error][Json]:", msg)
            return False

    print(obj)

    with open(path.absolute(), "w", encoding="utf-8") as f:
        list_item = []

        for item in obj:
            list_item.append(
                {
                    'name': item["name"],
                    'group': item.get("group", 0),
                    'z': item["z"]
                }
            )

        json.dump(list_item, f, ensure_ascii=False, indent=4)
    return True
