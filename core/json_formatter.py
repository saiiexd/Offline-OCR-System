import json


def text_to_json(raw_text):
    lines = [line.strip() for line in raw_text.split("\n") if line.strip()]

    data = {
        "lines": lines
    }

    return json.dumps(data, indent=4)
