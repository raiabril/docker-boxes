#!/usr/bin/env python3


import requests

print(requests.get("https://www.google.com").status_code)