#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int input, output;

    if (argc != 2) {
        printf("USAGE: %s <number>\n", argv[0]);
        return -1;
    }

    input = atoi(argv[1]);

    asm ("MOV EBX, %0"
        :
        : "r"(input));

    asm (
        /* Your code starts here. */
            //    "DEC EBX;"

        "MOV EDX,0;"//i=0
        "MOV EAX,0;"//result =1
        "MOV ECX,1;"//prev =1
        "MAINLOOP:"
        "CMP EDX,EBX;"//i>=n-1
        "JGE ENDMAINLOOP;"
        "MOV EDI,EAX;"//tmp=result
        "ADD EAX,ECX;"
        "MOV ECX,EDI;"
        "INC EDX;"
        "JMP MAINLOOP;"
        "ENDMAINLOOP:"
        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
