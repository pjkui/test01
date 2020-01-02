#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import time
import gzip
from hashlib import md5
import sys
import io


def Decrypt(key:str, text:str) -> str:
	if len(key) < 32: key += ' ' * (32 - len(key))
	elif len(key) > 32: key = key[0:32]
	cipher = AES.new(bytes(key,encoding='utf-8'), AES.MODE_CBC, bytes(AES.block_size))
	dec = cipher.decrypt(base64.b64decode(text))
	# print(dec)
	s1 = str(gzip.decompress(bytes.strip(dec)), encoding='utf-8') 
	print(s1)
	return s1


def Pass(id, priv_key):
	prefix = str(id) + str(int(time.time()))
	pub_key = prefix + md5(bytes(prefix + priv_key, 'utf8')).hexdigest()
	print('恭喜通过第%d关,通关公钥:%s' % (id, pub_key))

stack = []
ins_len = [1] * 5 + [2] * 9 + [9, 1]
print("ins_len")
print(ins_len)
reg = [0] * 16
code = base64.b64decode('zyLpMs8CL9Oy/3QDdRlURZRGFHQHdRhURZFGIL/lv+MiNi+70AXRBtMD1wfYCNkJ5v3/iV14RWMB0n+/xgk=')
print(code)
while True:
	ins, r0 = code[reg[15]] >> 4, code[reg[15]] & 15
	length = ins_len[ins]
	if length > 1:
		arg = code[reg[15] + 1 : reg[15] + length]
		if length == 2: r1 = arg[0] >> 4; r2 = arg[0] & 15
	reg[15] += length
    
	if 0 == ins : break
	elif 1 == ins : stack.append(reg[r0])
	elif 2 == ins : reg[r0] = stack.pop()
	elif 3 == ins : 
		if not reg[r0] : reg[15] += ins_len[code[reg[15]] >> 4]
	elif 4 == ins : reg[r0] = 0 if reg[r0] else 1
	elif 5 == ins : reg[r0] = reg[r1] + reg[r2]
	elif 6 == ins : reg[r0] = reg[r1] - reg[r2]
	elif 7 == ins : reg[r0] = reg[r1] * reg[r2]
	elif 8 == ins : reg[r0] = reg[r1] / reg[r2]
	elif 9 == ins : reg[r0] = reg[r1] % reg[r2]
	elif 10 == ins : reg[r0] = 1 if reg[r1] < reg[r2] else 0
	elif 11 == ins : stack.append(reg[r0]); reg[r0] += int.from_bytes(arg, byteorder='little', signed=True)
	elif 12 == ins : reg[r0] += int.from_bytes(arg, byteorder='little', signed=True)
	elif ins in (13, 14) : reg[r0] = int.from_bytes(arg, byteorder='little', signed=True)

key = str(reg[0])+str(reg[1])
exec(Decrypt(key,'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'))