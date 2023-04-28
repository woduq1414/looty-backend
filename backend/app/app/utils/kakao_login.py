import json
import requests


def verify_kakao_access_token(
        kakao_access_token : str
) -> str | None:
    res = requests.get("https://kapi.kakao.com/v1/user/access_token_info", headers={
        "Authorization": "Bearer " + kakao_access_token
    })

    print(res.text)

    if res.status_code != 200:
        return None

    kakao_id = str(json.loads(res.text)["id"])
    return kakao_id

