import os
import math
import random




digits="0123456789"
OTP=""

# 8 digit random password generator

for i in range(8):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + ": is your random generated OTP to use !! Don't share with others"

msg = otp 

print (msg)
