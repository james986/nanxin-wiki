# 西门子TIA Portal v19-FB库使用说明（S7-1200）

---
## 1. 接线说明

### 1.1 机柜接线说明
{{ fig_indent("../images/1.png","1","3.2em")}}

### 1.2 PLC-UC04-UART舵机接线说明

| **CB 1241_TA**   | **CB 1241_T/RA** |
| ---------------- | ---------------- |
| CB 1241_TB   | CB 1241_T/RB |
| CB 1241_T/RA | UC04_A       |
| CB 1241_T/RB | UC04_B       |

{{ fig_indent("../images/2.png","2","3.2em")}}

### 1.3 RS485舵机接线说明

| **PLC-A**                  | **RS485舵机-A** |
| -------------------------- | --------------- |
| PLC-B                  | RS485舵机-B |
| 电源+                  | RS485舵机+  |
| 电源-（需要和PLC共地） | RS485舵机-  |

{{ fig_indent("../images/12.png","12","3.2em")}}

## 2. 程序说明

### 2.1 组态配置（软件为：博途V19）

- **1.** 在设备组态中添加PLC型号，将CB 1241(RS485)通信板加入组态中

    {{ fig_indent_adjustable("../images/3.png","3", "100%", "3.5em") }}

- **2.** 鼠标左键双击PLC设备，选择''系统和时钟存储器''，勾选''启用系统存储器字节''和''启用时钟存储器字节''

    {{ fig_indent_adjustable("../images/4.png","4", "100%", "3.5em") }}

### 2.2 库函数调用及使用

- **1.** 点击软件右侧“库”，打开‘’全局库‘’，选择.al19尾缀的文件打开

    {{ fig_indent_adjustable("../images/5.png","5", "100%", "3.5em") }}

    {{ fig_indent_adjustable("../images/6.png","6", "100%", "3.5em") }}

- **2.** 打开后可以看到已经添加入其中，在模板副本中拖动FB函数（库函数）到程序中并填写好参数，将数据块拖动到最左侧程序块中

    {{ fig_indent_adjustable("../images/7.png","7", "100%", "3.5em") }}

    {{ fig_indent_adjustable("../images/8.png","8", "100%", "3.5em") }}

    {{ fig_indent_adjustable("../images/9-17605849095322.png","9-17605849095322", "100%", "3.5em") }}

- **3.** 单击数据块，将数据块中的发送数据拖动到发送指令Send_P2P中的BUFFER中

    {{ fig_indent_adjustable("../images/10.png","10", "100%", "3.5em") }}

- **4.** 单击数据块，将数据块中的接收数据拖动到接收指令Receive_P2P中的BUFFER中

    {{ fig_indent_adjustable("../images/11.png","11", "100%", "3.5em") }}

### 2.3 参数说明（库函数通用）

- angle：舵机目标角度，单位为0.1度
- ID：舵机ID号
- interval：舵机到达目标角度时间，单位ms
- accInterval：加速时间，单位ms（需要大于20ms）
- decInterval：减速时间，单位ms（需要大于20ms）
- power：执行功率，单位mw


