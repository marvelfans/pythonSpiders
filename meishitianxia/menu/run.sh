#!/usr/bin

PYTHON='/data/zhaojingzhen/bin/python2.7/bin/python2.7'

# 是否有参数
# if [ $# -lt 1 ]; then
#     echo "ERROR: Please Input argument!"
#     exit
# fi
# 如果之前有，就杀死
PIDS=`ps aux | grep 'producer.py' | grep -v "grep" | awk '{print $2}'`
kill -9 ${PIDS}
#
PIDS=`ps aux | grep 'consumer.py' | grep -v "grep" | awk '{print $2}'`
kill -9 ${PIDS}
# # 启动程序，抓取url
# for ((i=1; i<=10; i++))
# do
#     {
#         ${PYTHON} producer.py $i
#     }
#     sleep 2
# done

# 开启多个抓取进程，从redis获取url抓取. consumer
# 设置抓取进程数目
PID_NUM=5
while [ ${PID_NUM} -gt 0 ]
do
    {
        ${PYTHON} consumer.py get
    }&
    PID_NUM=$(($PID_NUM - 1))
    sleep 1
    echo $PID_NUM
done
