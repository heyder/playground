#!/usr/bin/env python3

import random
import argparse
from scapy.all import srp, Ether
from scapy.layers.inet import IP, UDP


def get_args():
    parser = argparse.ArgumentParser(prog="traceroute.py",
                                     formatter_class=lambda prog: argparse.HelpFormatter(
                                         prog, max_help_position=50),
                                     epilog='''This is a traceroute implementation using scapy.''')

    parser.add_argument("target", help="Target Host")
    parser.add_argument("-m", "--maximum",  default=30,
                        required=False, help="use maximum <hops>")
    args = parser.parse_args()
    return args


def traceroute(dst, max_hops):
  try:
    #ans, unans = srp(Ether()/IP(ttl=1,dst="8.8.8.8")/UDP(dport=33434), iface="eth0")
    packet = Ether()/IP(dst=dst)/UDP(dport=random.randint(33434, 65535))
    #print(packet.show())
    i = 1
    while i <= max_hops:
      packet.ttl = i
      ans, unans = srp(packet, verbose=False, timeout=2)
      #print(ans.show())
      if not ans.res:
        print('{} no reply '.format(i))
        next
      else:
        icmp_resp_type = ans.res[0][1][2].type
        #print(icmp_resp_type)
        if icmp_resp_type == 11:  # 11 - TIME_EXCEEDED
          print('{} {} *'.format(i, ans.res[0][1][1].src))
        elif icmp_resp_type == 3:  # 3 - PORT_UNREACHABLE
          print('{} {} *'.format(i, ans.res[0][1][1].src))
          break
        else:
          raise Exception("Unexpected ICMP type {}".format(icmp_resp_type))
      i += 1
  except KeyboardInterrupt:
    print("\n\n[*] User requested shutdown.")
    exit(0)


def main():
  args = get_args()
  traceroute(args.target.strip(), int(args.maximum))


if __name__ == '__main__':
  main()
