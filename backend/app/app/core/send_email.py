import random
import os


def send_secruity_code_mail(email: str) -> None:
    subject = "[Looty] 이메일 인증 코드"
    secruity_code = generate_security_code()
    data = {
        "code" : secruity_code
    }
    send_email_template(email = email, subject = subject, template = "security_code_mail.html", data = data)


def generate_security_code() -> str:
    return str(random.randint(100000, 999999))


def send_email_template(email: str, subject: str, template: str, data: dict) -> None:
    pass
    # with open(os.path.join(os.path.dirname(__file__), f"templates/{template}"), "r") as f:
    #     template_str = f.read()
    # template = Template(template_str)
    # html = template.render(**data)
    # send_email(email = email, subject = subject, html = html)


