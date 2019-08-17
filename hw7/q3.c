#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>



int pid =0x12345678;
int addr_got = 0xabcdefff;
int new_addr =0xabcdabcd;

int main() {
	long check;
	//attach to proc
	check = ptrace(PTRACE_ATTACH,pid,NULL,NULL);
	if(check<0){
		perror("Cant attach");
		return -1;
	}
	//switch code 
	check = ptrace(PTRACE_POKEDATA,pid,addr_got,new_addr);
	if(check<0){
		perror("Cant change code");
		return -1;
	}
	//detach
	check = ptrace(PTRACE_DETACH,pid,NULL,NULL);
	if(check<0){
		perror("Cant detach");
		return -1;
	}
    return 0;
}