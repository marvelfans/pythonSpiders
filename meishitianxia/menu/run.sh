#!/usr/bin

# 是否有参数
if [ $# -lt 1 ]; then
    echo "ERROR: Please Input argument!"
    exit
fi
# 如果之前有，就杀死
PIDS=`ps aux | grep 'main.py' | grep -v "grep" | awk '{print $2}'`
kill -9 ${PIDS}
# 开启一个进程，向redis输送url. producer
python main.py put &
sleep $1
# 开启多个抓取进程，从redis获取url抓取. consumer
PID_NUM=$1
while [ ${PID_NUM} -gt 0 ]
do
    {
        python main.py get
    }&
    PID_NUM=$(($PID_NUM - 1))
    sleep 1
    echo $PID_NUM
done
