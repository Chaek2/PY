import Main, BD
import pyotp
import qrcode
k = pyotp.random_base32() # для надёжности есле надо

def reg(log):
    totp_auth = pyotp.totp.TOTP(
    key(log)).provisioning_uri(
    name='Player '+log,
    issuer_name='Wallet')
    qrcode.make(totp_auth).save("qr_auth.png")
    

def auto(log,sum):
    totp = pyotp.TOTP(key(log))
    while True:
        if totp.verify(input(("Enter the Code : "))):
            for i in BD.Row("Player",(log),"S"):
                BD.Row("Player",(i[1],i[2],i[3],i[4]+sum,i[0]),"U")
            Main.menu(log)

def key(log):
    for i in BD.Row("Player",(log),"S"):
        key=i[2]
    return key