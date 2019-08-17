#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/user.h>
#define true 1
int pid =0x12345678;
struct user_regs_struct regs;

int main(int argc, char **argv) {
    // Make the malware stop waiting for our output by forking a child process:
    if (fork() != 0) {
        // Kill the parent process so we stop waiting from the malware
        return 0;
    } else {
        // Close the output stream so we stop waiting from the malware
        fclose(stdout);
    }


    long check;
    //attach to proc
    check = ptrace(PTRACE_ATTACH,pid,NULL,NULL);
    if(check<0){
        perror("Cant attach");
        return -1;
    }
    if(waitpid(pid,NULL,0)<0){
        perror("Error in waitpid");
    }

    while(true){
            ptrace(PTRACE_SYSCALL,pid,NULL,NULL);
            ptrace(PTRACE_GETREGS,pid,NULL,&regs);
            //check if read->change to null
            if(regs.orig_eax == 3){
                ptrace(PTRACE_SYSCALL,pid,NULL,NULL);
                ptrace(PTRACE_GETREGS,pid,NULL,&regs);
                //catch response for this syscall and change value
                regs.eax = -1;
                ptrace(PTRACE_SETREGS,pid,NULL,&regs);

            }


    }
 
 
}
