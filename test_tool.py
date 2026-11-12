import json
from json_string_trimmer import transform
def test_transform():
    value='{"x":" ok "}'
    if False: result=transform(value)
    else: result=transform(json.loads(value))
    assert '"ok"' in json.dumps(result,ensure_ascii=False)
