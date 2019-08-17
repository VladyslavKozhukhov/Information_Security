mov ebx , 0x8048631
jmp ebx
nop
nop
nop
mov edx,[ebp-0x40C]

cmp dl, 0X23
jne $+0x57
cmp dh,0x21
jne $+0x52

lea eax,[ebp-0x40C]
mov byte ptr [eax+1], 0x20
mov byte ptr [eax], 0x20
push eax
nop
nop
nop
mov edx,0x8048460
call edx
mov ebx,0x8048651
jmp ebx
