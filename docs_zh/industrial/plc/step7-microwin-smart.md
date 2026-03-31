# 西门子STEP 7-FB库使用说明（S7-200 SMART）

---
## 1. 接线说明

### 1.1 机柜接线说明

{{ fig_indent_adjustable("../images/200-1.png","机柜接线说明", "100%", "3.5em") }}

### 1.2 UC04接线说明

{{ fig_indent_adjustable("../images/200-2.png","机柜接线说明", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/200-3.png","200-3", "100%", "3.5em") }}

### 1.3 RS485舵机接线说明

| **PLC-A**                  | **RS485舵机-A** |
| -------------------------- | --------------- |
| PLC-B                  | RS485舵机-B |
| 电源+                  | RS485舵机+  |
| 电源-（需要和PLC共地） | RS485舵机-  |

{{ fig_indent_adjustable("../images/200-11.png","200-11", "100%", "3.5em") }}

## 2. 程序说明

### 2.1 库函数封包

 西门子S7-200SMART结合FashionStar总线伺服舵机通讯协议库（通讯协议可参考官网：https://fashionstar.com.hk/）

    {{ fig_indent_adjustable("../images/200-4.png","200-4", "100%", "3.5em") }}

 以“角度控制库”为例，TX_0~TX_CS为实际发送的协议寄存器，BYTE占一个字节，WORD占两个字节（可以看下图“角度的控制库寄存器说明”）；**需要注意的是在“角度控制库”中ANGLE和TIME这里要占四个寄存器，其他以“角度的控制库寄存器说明”的数据类型为准**，TX_V为寄存器头，例如VB100、VB200、VB300......（具体可以看下文例程）

    - ID ：需要设置舵机ID
    - ANGLE ：舵机角度（单位为0.1度，例如需要设置90度，输入应为900）
    - TIME ：舵机运动时间（单位ms）
    - POWER ：运行功率（单位mw）
    - ACC ：舵机运行加速时间（单位ms）
    - DEC： 舵机运行减速时间（单位ms）

    {{ fig_indent_adjustable("../images/200-5.png","200-5", "100%", "3.5em") }}


    {{ fig_indent_adjustable("../images/200-6.jpg","200-6", "100%", "3.5em") }}


### 2.2 库函数封包版程序解析说明

 端口0输出：SMB30 = 2#10011001:自由口通讯，波特率115200，8位数据位，无校验

    {{ fig_indent_adjustable("../images/200-7.png","200-7", "100%", "3.5em") }}

    {{ fig_indent_adjustable("../images/200-8.png","200-8", "100%", "3.5em") }}


 库解析说明

    - ID = 0：控制0号舵机
    - ANGLE = 900：设置角度为90度（单位为0.1度，90度应设为900）
    - TIME = 100：舵机100ms运行到90度（单位为ms）
    - POWER = 0 ：运行功率为0mw（单位为mw
    - ACC = 20：舵机运行加速时间为20ms（单位为ms）
    - DEC = 20： 舵机运行减速时间为20ms（单位为ms）
    - TX_0 = VB101
    - TX_1 = VB102
    - TX_CID = VB103
    - TX_LONG = VB104
    - TX_ID = VB105
    - TX_ANGLE = VW106 
    - TX_TIME = VW110
    - TX_ACC = VW114
    - TX_DEC = VW116
    - TX_POWER = VW118
    - TX_CS = VW120
    - TX_V = VB100

    {{ fig_indent_adjustable("../images/200-9.png","200-9", "100%", "3.5em") }}

 程序发送用XMT指令，接收用RCV指令，TBL为发送的寄存器；PORT为发送端口，这里用端口0输出；程序通过T32定时器做定时发送，加入|N|指令下降沿发送一次，避免多次发送指令造成冗余

    {{ fig_indent_adjustable("../images/200-10.png","200-10", "100%", "3.5em") }}



