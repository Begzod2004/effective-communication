from pprint import pprint

from eskiz.client import SMSClient


client = SMSClient(
    api_url="https://notify.eskiz.uz/api/",
    email="begzodmirzaqulov71@gmail.com",
    password="ajrkyssdbpxcgigs",
)

resp = client._send_sms(
    phone_number="998992291329",
    message="Hello from Python❤️"
)
pprint(resp)