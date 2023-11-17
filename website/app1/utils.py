import json

def convert_request_body_into_json(reqBody):
    if reqBody:
        body_unicode = reqBody.decode('utf-8')
        json_body = json.loads(body_unicode)
        return json_body