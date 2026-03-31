# 汇川InoproShop-FB库使用说明（AM401）

---
## 1. 接线说明

### 1.1 舵机接线说明

{{ fig_indent_adjustable("../images/汇川舵机接线说明.png","舵机接线说明", "100%", "3.5em") }}

### 1.2 RS485舵机接线说明

{{ fig_indent_adjustable("../images/汇川RS485舵机接线说明.png","RS485舵机接线说明", "100%", "3.5em") }}

### 1.3 UC04接线说明

{{ fig_indent_adjustable("../images/汇川UC04接线说明.png","UC04接线说明", "100%", "3.5em") }}

 

## 2. 程序说明

### 2.1 PLC串口与串口自由协议的配置

（1）、串口配置，默认为：

​	1. 波特率：115200

​	2. 奇偶校验：无

​	3. 数据位：8

​	4. 停止位：1&nbsp;

（2）、自由协议（例）：&nbsp;

​	1. 接收字节数寄存器：%MW0/%MB0

​	2. 接收数据起始地址：%MW1/%MB2

​	3. 最大接收长度：256

​	4. 发送字节数寄存器：%MW300/%MB600

​	5. 发送数据起始地址：%MW301/%MB602

​	6. 最大发送长度：256

{{ fig_indent_adjustable("../images/汇川串口自由协议配置.png","串口自由协议配置", "100%", "3.5em") }}

### 2.2 串口数据写入（通过库函数进行操作）：

  1. 0 ------- 舵机ID号

  2. 3600 -- 舵机目标角度360.0度

  3. 3000 -- 在3000ms(3S)转到目标角度

  4. 100 ---- 加速时间100ms

  5. 100 ---- 减速时间100ms

通过库函数将数据转换并封装进数据发送数组(自定义)

然后将SendBuf中的数据按顺序赋值给串口数据发送起始地址。

{{ fig_indent_adjustable("../images/汇川串口写入_1.jpg","串口写入_1", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/汇川串口写入_2.png","串口写入_2", "100%", "3.5em") }}



### 2.3 串口数据发送

将协议数据包写入到串口发送寄存器完毕后，将发送字节数寄存器写入要发送的字节长度（即非零）即可发送成功，操作成功后该寄存器自动归零。

{{ fig_indent_adjustable("../images/汇川串口发送.png","串口发送", "100%", "3.5em") }}

说明：串口配置可参考下面文档

`https://newweb.inovance.com/owfile/ProdDoc/SC/PS00003145_PDF_CN/C02/中型PLC编程手册（软件使用篇）-CN-C02.PDF?response-content-disposition=inline;filename=`



### 2.4 库函数与通信协议的说明

说明：Fashionstar 伺服总线舵机通讯协参考：

*https://wiki.fashionstar.com.hk/uartbasic/uart_rs485_protocols/*

{{ fig_indent_adjustable("../images/汇川库函数与通讯协议的说明.png","库函数与通讯协议的说明", "100%", "3.5em") }}



## 3. 库文件的导入

1. 在”Inoproshop”工具中找到工程标签并且点击导入PLCCopenXML将所有的FB库导入到工程文件中。

    {{ fig_indent_adjustable("../images/汇川库文件导入_1.png","库文件导入_1", "100%", "3.5em") }}



2. 导入成功后，我们通过拖拽工具箱中的功能块来进行我们的库文件调用并且填入我们实际所需的参数。

    {{ fig_indent_adjustable("../images/汇川库文件导入_2.png","库文件导入_2", "100%", "3.5em") }}

## 4. 库函数说明

### 4.1 角度控制

  1. ID：舵机ID编号

  2. Angle：舵机目标角度（3600）

  3. Interval：舵机到达目标角度时间

  4. AccInterval：加速时间

  5. DecInterval：减速时间

  6. Power：执行功率

**说明：在将SendBuf数据写入到串口发送寄存器的时候需要按顺序且连续发送，而且发送的时候字节数大小也要更改为需要发送的字节数！**

{{ fig_indent_adjustable("../images/汇川库文件导入_2.png","库文件导入_2", "100%", "3.5em") }}

&nbsp;

### 4.2 角度读取

  1. ID：舵机ID编号

{{ fig_indent_adjustable("../images/汇川库函数--角度读取.jpg","库函数--角度读取", "100%", "3.5em") }}

&nbsp;

### 4.3 重置圈数

  1. ID：舵机ID编号

{{ fig_indent_adjustable("../images/汇川库函数--重置圈数.jpg","库函数--重置圈数", "100%", "3.5em") }}

&nbsp;

### 4.4 原点设置

  1. ID：舵机ID编号

{{ fig_indent_adjustable("../images/汇川库函数--原点设置.jpg","库函数--原点设置", "100%", "3.5em") }}

&nbsp;

### 4.5 阻尼模式

  1. ID：舵机ID编号

  2. Power：阻尼执行功率(mv)

{{ fig_indent_adjustable("../images/汇川库函数--阻尼模式.jpg","库函数--阻尼模式", "100%", "3.5em") }}

### 4.6 通讯检测

  1. ID：舵机ID编号

{{ fig_indent_adjustable("../images/汇川库函数--通讯检测.jpg","库函数--通讯检测", "100%", "3.5em") }}

### 4.7 异步指令

- 开始异步：固定指令，直接使用。

- 结束异步：

​       State：0 -- 异步结束立即执行，1 -- 异步结束取消执行

{{ fig_indent_adjustable("../images/汇川库函数--异步指令开始.jpg","库函数--异步指令开始", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/汇川库函数--异步指令结束.jpg","库函数--异步指令结束", "100%", "3.5em") }}

### 4.8 数据监控

  1. ID：舵机ID编号

{{ fig_indent_adjustable("../images/汇川库函数--数据监控.jpg","库函数--数据监控", "100%", "3.5em") }}

### 4.9 停止转动（三种：卸力、锁力、阻尼）

  1. ID：舵机ID编号

  2. Power：执行功率(mv)

{{ fig_indent_adjustable("../images/汇川库函数--停止转动--卸力.jpg","库函数--停止转动--卸力", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/汇川库函数--停止转动--锁力.jpg","库函数--停止转动--锁力", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/汇川库函数--停止转动--阻尼.jpg","库函数--停止转动--阻尼", "100%", "3.5em") }}



