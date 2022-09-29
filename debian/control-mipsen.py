#!/usr/bin/env python3
import sys

all_mips_archs = "mips mipsel mipsn32 mipsn32el mips64 mips64el mipsr6 mipsr6el mipsn32r6 mipsn32r6el mips64r6 mips64r6el"

def convert_section(s):
    res = []
    for l in s.split('\n'):
        if l.startswith('Architecture: '):
            l = convert_arch(l)
            if not l:
                return
        res.append(l)
    return '\n'.join(res)

def convert_arch(l):
    astr = []
    for a in l.rstrip().split():
        if a == "any" or a == "linux-any":
            return 'Architecture: ' + all_mips_archs
        if a.startswith("mips"):
            astr.append(a)
    return "Architecture: " + ' '.join(astr) if astr else None


with open("debian/control.tmp") as f:
    sections = [s.strip() for s in f.read().split('\n\n')]
    sections = [convert_section(s) for s in sections if s.startswith("Package: ") or s.startswith("Source: ")]
    sections = [s for s in sections if s]
    print(*sections, sep='\n\n')
