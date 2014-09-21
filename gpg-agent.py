#!/usr/bin/env python

# simple program to convert gpg-agent's output to fish-friendly syntax
import subprocess
import re

# execute gpg-agent and read in environmental variables
proc = subprocess.Popen(["gpg-agent", "-s", "--enable-ssh-support", "--daemon"], stdout=subprocess.PIPE, universal_newlines=True)

# loop over input lines, removing export commands
# remove unneeded semicolons and convert '=' to ' '
# execute fish and set gpg-agent's needed env variables
for line in proc.stdout:
    linelist = line.split("export")
    fixedstr = re.sub(r'; ', "", linelist[0])
    fixedstr = re.sub(r'=', " ", fixedstr)
    fixedstr = "set " + fixedstr
    subprocess.call(["/usr/bin/fish", "-c", fixedstr])
