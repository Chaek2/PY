import smtpd, Main, os,QR
import smtplib
import time
from random import randint
def Add(log):
    os.system('cls')
    sum = int(input("Введите сумму (100-700)"))
    if sum>99 and sum<701:
        QR.reg(log)
        QR.auto(log,sum)
    else:
        Add(log)
    
