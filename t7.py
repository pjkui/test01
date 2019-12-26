#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from Crypto.Cipher import AES
import base64
import time
import gzip
from hashlib import md5
import sys
import io

def Hash(context):
    result = md5(bytes(context, 'utf8'))
    for i in range(0, 10000000):
            result = md5(result.digest())
    return result.hexdigest()
def Do():
    for keyI in range(0,99999999):
        key = str(keyI)
        if len(key) < 8: key = '0' * (8 - len(key))+key
        if Hash(key) == '5f4654140971c47658de19d62ba472b6':
            print(key)
            print("done")
            return
        else:
            print(str(keyI/99999999)+'% '+key)
Do()