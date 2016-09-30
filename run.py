from modex import modex
from Crypto.Util import number
import os


def gen_public():
    g_val = 5
    p_val = number.getPrime(512)
    s_val = int.from_bytes(os.urandom(int(512 / 8)), byteorder='big')
    public = modex(g_val, s_val, p_val)

    print('g_val: ', end='')
    print(g_val)
    print('p_val: ', end='')
    print(p_val)
    print('s_val: ', end='')
    print(s_val)
    print('publi: ', end='')
    print(public)


def find_private(gtp, s, p):
    result = modex(gtp, s, p)
    print('result: ', end='')
    print(result)


if __name__ == '__main__':
    find_private(
        2945166128725800256000955729328375301382052850666414119166643464430300294452268388009300704087876707467404623104125436114550913807034328143124586069785864,
        11553455138370287079234584895833422641861280994366615547014331141371142559160261207471744791035992733865675353735314772631012491551048454647318378576025649,
        11570030796084393485015596325980500115240964467836275977103555273985399177209114919338704479157106531784731416182305862495754749741439456293862894856466757
    )
