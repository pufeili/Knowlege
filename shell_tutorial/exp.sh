#!/bin/bash
#这一句是约定的标记，表示这个脚本使用bash解释器执行


#start_time=$(date +%s)
echo `date`
start_time=$(date +%s)   #记录开始时间

python3 main.py -lr 0.2

python3 main.py -e 40 -lr 0.001 -m cat -fm 2
python3 main.py -e 41 -lr 0.0001 -m add -fm 3
python3 main.py -e 42 -lr 0.002 -m asa -fm 4
python3 main.py -e 43 -lr 0.003 -m bcb -fm 1

end_time=$(date +%s)
cost_time=$[ $end_time-$start_time ]
echo "build kernel time is $(($cost_time/60))min $(($cost_time%60))s"

#echo $cost_time
