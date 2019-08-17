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
        "XOR EDI,EDI;"          //max=0 EDI
        "PUSH EBX;"          //ECX=EBX=num
        "MOV EAX, EBX;"         //EAX=EBX=num
        "MOV EBX,EDI;"          //EBX=0
        "INC EBX;"              //EBX=d=1
        "INC EBX;"              //EBX=d=2

        "MAINLOOP:"
        "XOR ECX,ECX;"      //ESI=0
        "INC ECX;"          //ESI=n=1    
        "CMP EAX,ECX;"      //Num cmp 1 
        "JLE ENDMAINLOOP;"  //if num<=1 leave main loop        

        "SECONDLOOP:"
        "XOR EDX, EDX;"
        "DIV EBX;"          //EAX/EBX ---> EDX=num%d, EAX = num/d
        "XOR ECX,ECX;"      //ESI = 0
        "CMP ECX,EDX;"      //num%d == 0
        "JNE ENDSECONDLOOP;"//if num%d!=0 jump to end
        "CMP EDI,EBX;"      //max<=d
        "JLE UPDATEMAX;"
        "JMP SECONDLOOP;"   //if max >d continue
        "UPDATEMAX:"
        "MOV EDI,EBX;"      //max=d;
        "POP ECX;"
        "PUSH EAX;"
        "JMP SECONDLOOP;"   //back to while n%d == 0

        "ENDSECONDLOOP:"
        "POP EAX;"
        "PUSH EAX;"         //Eax back
        "INC EBX;"          //d++
        "JMP MAINLOOP;"     //Back to While n>1     

        "ENDMAINLOOP:"
        "MOV EAX,EDI;"//EDI;"          //move max to EAX
        
        //add check if 1 so 0
        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
