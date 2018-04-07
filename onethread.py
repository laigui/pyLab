#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    nloops = range(len(loops))

    for i in nloops:
        loop(i, loops[i])
    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()