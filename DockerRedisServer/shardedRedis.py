#!/usr/bin/python3

import os, sys, getopt
import subprocess

argv=sys.argv[1:]
numShards=8
basePort=6381

try:
    opts, args = getopt.getopt(argv, "n:p:", ["numshards=", "port="])
except getopt.GetoptError:
    print
    'shardedRedis -n <number of shards> -p <port number>'
    sys.exit(2)
for opt, arg in opts:
    if opt in ('-p', "--port"):
        basePort=int(arg)
    elif opt in ("-n", "--numshards"):
        numShards = int(arg)

listProcess = []

for i in range(0,numShards):
    portNum=str(basePort+i)
    if not os.path.exists(portNum):
        os.mkdir(portNum)
    os.chdir(portNum)
#    command = "redis-server /data/BGPGeoPo1/redis.conf --port "+portNum
    command = "redis-server /src/DockerRedisServer/redis.conf --port "+portNum
    p=subprocess.Popen(command, shell=True)
    listProcess.append(p)
    #print(p.returncode)
    os.chdir('..')

finish = False

while not finish:
    finish = False
    #for iProcess in range(numShards):
    #    if listProcess[iProcess].poll() is not None:
    #   	    print("Server", i + 1, "has stopped")
    #   	    finish = True

#print('done')

