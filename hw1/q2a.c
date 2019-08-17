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
        "FIBREC:"
        "CALL FIBFUNC;"
        "JMP OUT;"
        "FIBFUNC:"
        "XOR EAX,EAX;"
        "XOR ECX,ECX;"
        "INC EAX;"
            "MOV ECX,EAX;"//1
            "CMP ECX,EBX;"
            "JGE ENDOFLOOP;"//if greater >=
            "PUSH EBX;"//save value
            "SUB EBX,1;"
            "CALL FIBFUNC;"//F(n-1)
            "POP EBX;"//Get back value
            "MOV EDI,EAX;"
            "PUSH EDI;"//save again
            "SUB EBX,2;"
            "CALL FIBFUNC;"//F(n-2)
            "POP EDI;"
            "ADD EAX,EDI;"//+
            "RETURN:"
            "RET;"
            "ENDOFLOOP:"
            "XOR EDI,EDI;"
            "CMP EBX,EDI;"
            "JZ ENDRET;"
            "ADD EAX,1;"
            

            "ENDRET:"//low numbers,back
            "MOV EAX,EBX;"
            "RET;"
        "OUT:"//get out
        "NOP;"
        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
