
#!/bin/bash
#这一句是约定的标记，表示这个脚本使用bash解释器执行
echo `date`
echo "hello world!"
# echo命令用于向窗口输出文本

#chmod +x ./tut.sh 使脚本有执行权限
# ./tut.sh在终端运行脚本

#--------
#使用变量

name="LPF"
echo ${name}
#花括号可选，加不加都行，加花括号为了帮助解释器识别变量

name="new_LPF"
echo ${name}
#变量可以被重新定义

#readonly name
#readonly 可以使变量定义为只读变量

unset name
#unset variable_name 删除变量，但不能删除只读变量

