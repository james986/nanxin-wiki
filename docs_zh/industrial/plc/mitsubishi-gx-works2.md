# 三菱GX-WORK2-FB库使用说明（FX3U）

---
## 1. 接线说明

### 1.1 设备接线架构

{{ fig_indent_adjustable("../images/GX2设备接线架构.png","设备接线架构", "100%", "3.5em") }}

### 1.2 UC04接线说明

{{ fig_indent_adjustable("../images/GX2UC04接线说明_1.png","UC04接线说明_1", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/GX2UC04接线说明_2.png","UC04接线说明_2", "100%", "3.5em") }}

## 2. 程序说明

### 2.1 PLC 串囗参数设置：

  1. 数据位：8

  2. 奇偶性：无

  3. 停止位：1

  4. 波特率：9600

  (因为这款 PLC无115200 波特率，所以需要在上位机设置舵机波特率为 9600)

{{ fig_indent_adjustable("../images/GX2串口参数设置_2.jpg","串口参数设置_2", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/GX2串口参数设置.png","串口参数设置", "100%", "3.5em") }}

### 2.2 串口数据写入（通过库函数进行操作）：

  1. K0 ------ 舵机ID号

  2. K3600 -- 舵机目标角度360.0度

  3. K3000 -- 在3000ms(3s)转到目标角度

  4. K100 --- 加速时间100ms

  5. K100 --- 减速时间100ms

通过库函数将以上数据转换并存入一个连续的寄存器内如下图所示，存入D410、D411以此类推

{{ fig_indent_adjustable("../images/GX2串口数据写入.png","串口数据写入", "100%", "3.5em") }}

### 2.3 串口通讯指令

  1. 发送的数据存在D410

  2. 发送的数据个数为20个

  3. 返回的数据存在D200

  4. 返回的数据个数最大为7个

{{ fig_indent_adjustable("../images/GX2串口通讯指令.jpg","串口通讯指令", "100%", "3.5em") }}

### 2.4 串口数据发送请求

{{ fig_indent_adjustable("../images/GX2串口发送请求.jpg","串口发送请求", "100%", "3.5em") }}

### 2.5 串口复位

{{ fig_indent_adjustable("../images/GX2串口复位.jpg","串口复位", "100%", "3.5em") }}

**说明：串口配置学习可参考：**

[(018)三菱FX3U PLC和串口助手通讯的方法_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1d84y1a7su/?spm_id_from=333.337.search-card.all.click&vd_source=1f8eb3ac14fcef7ab654bb2f9fbaab75)

### 2.6 库函数与通信协议的说明：

**说明：Fashionstar伺服总线舵机通讯协参考：**

<https://wiki.fashionstar.com.hk/uartbasic/uart_rs485_protocols/>

1. 以上面设置0号舵机3000ms旋转到360度为例子，用MOV指令分别将第二和第一位两两分别存入寄存器D410中，其他以此类推

{{ fig_indent_adjustable("../images/GX2库函数与通信协议的说明.png","库函数与通信协议的说明", "100%", "3.5em") }}




## 3. 库文件导入

1. 在“GX WORK2”工具中，找到工程--\>库操作--\>在工程中获取库。然后打开“在工程中获取库”。

    {{ fig_indent_adjustable("../images/GX2库文件导入_1.jpg","库文件导入_1", "100%", "3.5em") }}

2. 将自己所需的库文件导入到工程中即可

    {{ fig_indent_adjustable("../images/GX2库文件导入_2.jpg","库文件导入_2", "100%", "3.5em") }}

    {{ fig_indent_adjustable("../images/GX2库文件导入_2.jpg","库文件导入_2", "100%", "3.5em") }}

3. 通过拖拽FB管理者的FB库文件即可调用，然后写入自己实际所需的控制参数即可。

    {{ fig_indent_adjustable("../images/GX2库文件导入_4.png","库文件导入_4", "100%", "3.5em") }}



## 4. 库函数说明

### 4.1 角度控制

- ID:舵机ID号

- Angle:目标角度（K3600则是360.0度为目标角度）

- IntervalTime:转到目标角度的时间间隔（K3000为3000ms）

- AccInterval:加速时间（K100为100ms）

- DecInterval:减速时间（K100为100ms）

- Power:执行功率

  **说明：从D410开始需要到结束需要连续的寄存器写入，不可断层!**

  **（不一定是以D410作为数据起点，自定，以下同理）**

  {{ fig_indent_adjustable("../images/GX2库函数--角度控制.jpg","库函数--角度控制", "100%", "3.5em") }}

### 4.2 角度读取

- ID:舵机ID号

  {{ fig_indent_adjustable("../images/GX2库函数--角度读取.jpg","库函数--角度读取", "100%", "3.5em") }}

### 4.3 零点设置

- ID:舵机ID号

  {{ fig_indent_adjustable("../images/GX2库函数--零点设置.jpg","库函数--零点设置", "100%", "3.5em") }}

### 4.4 数据监控

- ID:舵机ID号

  {{ fig_indent_adjustable("../images/GX2库函数--数据监控.jpg","库函数--数据监控", "100%", "3.5em") }}

### 4.5 停止转动--三种模式

- ID:舵机ID号

- Power:执行功率

  {{ fig_indent_adjustable("../images/GX2库函数--停止转动--卸力.jpg","库函数--停止转动--卸力", "100%", "3.5em") }}

  {{ fig_indent_adjustable("../images/GX2库函数--停止转动--锁力.jpg","库函数--停止转动--锁力", "100%", "3.5em") }}
  
  {{ fig_indent_adjustable("../images/GX2库函数--停止转动--阻尼.jpg","库函数--停止转动--阻尼", "100%", "3.5em") }}

### 4.6 通讯检测

- ID:舵机ID号

  {{ fig_indent_adjustable("../images/GX2库函数--通讯检测.jpg","库函数--通讯检测", "100%", "3.5em") }}

### 4.7 异步指令

- 开始异步指令--固定指令，所以STATE不起作用的，给K0即可

- 结束异步指令

1.  K0，结束后立即执行

2.  K1，结束后取消执行

    {{ fig_indent_adjustable("../images/GX2库函数--异步指令.jpg","库函数--异步指令", "100%", "3.5em") }}

### 4.8 重置多圈

- ID:舵机ID号

  {{ fig_indent_adjustable("../images/GX2库函数--重置多圈.jpg","库函数--重置多圈", "100%", "3.5em") }}

### 4.9 阻尼模式

- ID:舵机ID号

- POWER：阻尼功率

  {{ fig_indent_adjustable("../images/GX2库函数--阻尼模式.jpg","库函数--阻尼模式", "100%", "3.5em") }}



