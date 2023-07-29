from secrets import choice
from sys import argv

def genpass():
    charlimit=
    while not isinstance(charlimit, int):
        charlimit = input("How much charactor would you like: ")
    print(charlimit)
        

def main():
    content = input("Do you want to generate:\n\t1> A password\n\t2> A hash\n\t3> A ssl public/private key\n")
    if content == "1" or content == "pass" or 1 in argv or "pass" in argv:
        genpass()
    elif content == 2 or content == "hash" or 2 in argv or "hash" in argv:
        genhash()
    elif content == 3 or content == "key" or content == "ssl" or 3 in argv or "key" in argv:
        getsslkey()

if __name__ == '__main__':
    main()
    
