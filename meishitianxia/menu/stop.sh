#!/usr/bin

#
PIDS=`ps aux | grep 'producer.py' | grep -v "grep" | awk '{print $2}'`
kill -9 ${PIDS}
#
PIDS=`ps aux | grep 'consumer.py' | grep -v "grep" | awk '{print $2}'`
kill -9 ${PIDS}
