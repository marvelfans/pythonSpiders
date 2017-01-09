#!/usr/bin

# 如果之前有，就杀死
PIDS=`ps aux | grep 'main.py' | grep -v "grep" | awk '{print $2}'`
kill -9 ${PIDS}
