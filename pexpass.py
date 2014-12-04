#!/usr/bin/env python
import sys
import optparse
import pexpect
import struct, fcntl, os, sys, signal

def sigwinch_passthrough (sig, data):
    # Check for buggy platforms (see pexpect.setwinsize()).
    if 'TIOCGWINSZ' in dir(termios):
        TIOCGWINSZ = termios.TIOCGWINSZ
    else:
        TIOCGWINSZ = 1074295912 # assume
    s = struct.pack ("HHHH", 0, 0, 0, 0)
    a = struct.unpack ('HHHH', fcntl.ioctl(sys.stdout.fileno(), TIOCGWINSZ , s))
    global global_pexpect_instance
    global_pexpect_instance.setwinsize(a[0],a[1])

ssh_newkey = 'Are you sure you want to continue connecting'

parser = optparse.OptionParser()
#parser.add_option('-f', action="store", dest="filename")
parser.add_option('-p', action="store", dest="password")
#parser.add_option('-e', action="store_true", dest="envpass", default=False)

options, args = parser.parse_args(sys.argv)

args.pop(0) #remove script name

p=pexpect.spawn(args.pop(0), args)
i=p.expect([ssh_newkey,'assword:',pexpect.EOF,pexpect.TIMEOUT],1)
if i==0:
    p.sendline('yes')
    i=p.expect([ssh_newkey,'assword:',pexpect.EOF])
if i==1:
    p.sendline(options.password)
elif i==2:
    print "I either got key or connection timeout"
    pass
elif i==3: #timeout
    pass
p.sendline("\r")
global global_pexpect_instance
global_pexpect_instance = p
signal.signal(signal.SIGWINCH, sigwinch_passthrough)

try:
    p.interact()
    sys.exit(0)
except:
    sys.exit(1)
