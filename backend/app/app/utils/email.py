import logging
import random
import os

from redis.asyncio import Redis

from app.api import deps
from app.utils.uuid6 import uuid7


async def send_secruity_code_mail(redis_client : Redis, email: str) -> str:

    
    key = f"security_code:{email}"

    if await redis_client.exists(key):
        await redis_client.delete(key)

    secruity_code = generate_security_code()
    await redis_client.set(key, secruity_code, ex = 60 * 30) # 30분 동안 유효

    subject = "[Looty] 이메일 인증 코드"
    
    data = {
        "code" : secruity_code
    }

    logging.info(key, secruity_code)

    send_email_template(email = email, subject = subject, template = "security_code_mail.html", data = data)

    return secruity_code


def generate_security_code() -> str:
    return str(random.randint(100000, 999999))


def generate_random_string():
    return uuid7()



async def verify_security_code(redis_client : Redis, email: str, secruity_code: str) -> bool:

    # TODO - 인증 횟수 제한 구현

    key = f"security_code:{email}"
    value = await redis_client.get(key)

    if value == secruity_code:

        return True
    else:
        return False


def send_email_template(email: str, subject: str, template: str, data: dict) -> None:
    print(data)
    pass
    # with open(os.path.join(os.path.dirname(__file__), f"templates/{template}"), "r") as f:
    #     template_str = f.read()
    # template = Template(template_str)
    # html = template.render(**data)
    # send_email(email = email, subject = subject, html = html)


