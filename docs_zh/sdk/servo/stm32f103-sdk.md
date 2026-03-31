# UART / RS485 总线伺服舵机 SDK 开发手册（STM32F103）

<style>
.md-typeset .uart-ds-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 8px;
  width: 100%;
  box-sizing: border-box;
}

.md-typeset .uart-ds-grid .uart-ds-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--fs-divider);
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
  text-align: center;
}


.md-typeset .uart-ds-grid a.uart-ds-card {
  display: block;
  color: inherit;
  text-decoration: none;
  cursor: pointer;
}

.md-typeset .uart-ds-grid a.uart-ds-card:hover {
  border-color: var(--fs-accent);
}

.md-typeset .uart-ds-grid .uart-ds-card img {
  width: 100% !important;
  max-width: 100% !important;
  height: auto;
  display: block;
  margin: 0 auto !important;
  padding: 0 !important;
  cursor: pointer !important;
}

.md-typeset .uart-ds-grid a.uart-ds-card:hover img {
  cursor: pointer !important;
}

.uart-ds-label {
  display: inline-block;
  margin-top: 4px;
  font-size: 14px;
  font-weight: 600;
}

@media (max-width: 640px) {
  .md-typeset .uart-ds-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .md-typeset .uart-ds-grid .uart-ds-card img {
    max-width: 100% !important;
  }
}
</style>

<a id="sdk-resource-bundle"></a>
{{ github_download_table("", "v1.2026.0305", "https://github.com/servodevelop/servo-uart-rs485-sdk", "./data/stm32f103-sdk.zip", "28px") }}



本 SDK 基于[总线伺服舵机 UART / RS485 通信协议](../../../uart/protocols/uart-rs485-protocol/)封装底层 C 语言 API，帮助开发者在 STM32F103 平台上快速实现各型号总线伺服舵机的精准控制、状态回读与多轴同步控制。

## 快速开始

在基础开发环境与硬件连线已完成的前提下，可通过下列入口直接跳转到对应功能示例。

每个示例均提供完整代码，可直接复制并编译执行，用于快速验证与联调。

- [▶️ 检测舵机是否在线](#quick-ping)
- [▶️ 控制单个舵机进行复杂运动](#quick-single-complex)
- [▶️ 串行指令控制多舵机](#quick-multi-serial)
- [▶️ 死区评估与自主运动闭环](#quick-deadzone-loop)
- [▶️ 多圈大角度运动控制](#quick-mturn-control)
- [▶️ 舵机持续旋转](#quick-wheel-keep)
- [▶️ 舵机定时旋转](#quick-wheel-timed)
- [▶️ 舵机定圈旋转](#quick-wheel-circle)
- [▶️ 体验阻尼手感](#quick-damping-feel)
- [▶️ 阻尼模式与运动轨迹捕获](#quick-damping-track)
- [▶️ 动作执行成功自动切入阻尼](#quick-stop-to-damping)
- [▶️ 系统毫秒级同步协同](#quick-sync-ms)
- [▶️ 异步命令延时触发](#quick-async-delay)
- [▶️ 舵机传感器数据全监控](#quick-monitor-full)
- [▶️ 读取舵机参数](#quick-read-params)


<h3 align="center"><span style="color:#007ACC;">=== 第一篇：环境搭建 ===</span></h3>

---

## 1. 资源准备

在开始编写代码前，请确保您已准备好以下软硬件开发资源：

### 1.1 开发工具及驱动软件

-   **[STM32F103 SDK 示例代码](https://fashionrobo.com/downloadcenter/)**
    
    包含完整底层驱动库与测试例程，可直接用于工程导入与功能验证。

-   **[上位机调试软件](../../../software/servo/pc-config-software/)**
    
    用于图形化测试舵机参数与动作。

-   **[Keil MDK-ARM v5](https://fashionrobo.com/wp-content/uploads/download/keil5.zip)**
    
    STM32 官方推荐的 C/C++ 集成开发环境，用于编译与下载固件。

-   **[串口调试助手（XCOM V2.2）](https://www.amobbs.com/forum.php?mod=attachment&aid=NDQxNzc5fDE5NzMzYjQ1fDE1NzY2NTQ4NTN8MHw1NzAzODMz)**
    
    用于查看 MCU 打印日志与通信状态数据。

-   **[CH340 串口驱动](https://fashionrobo.com/wp-content/uploads/download/CH341SER.zip)**
    
    转接板及调试模块常用的 USB 转 TTL 驱动。
	
	[（验证驱动是否安装成功）](https://jingyan.baidu.com/article/00a07f3872a90982d028dcb9.html)。

-   **[ST-Link v2 下载器驱动](https://fashionrobo.com/wp-content/uploads/download/STLinkV2.zip)**
    
    用于 ST-Link 下载器识别与烧录调试支持。

> [!TIP]
> 点击本文顶部[**开发资源包**](#sdk-resource-bundle)，可一键下载以上全部资源。

### 1.2 硬件准备

#### 方案一（🔰 新手强烈推荐）

使用“STM32 多合一主控板(PTC-32) 。主控板在物理层面集成了 **STM32F103C8T6** 与 **舵机转接板 UC-01** 的功能。免去繁杂的连接，即插即用，大幅降低前期硬件排错的时间成本。

<div class="uart-ds-grid">
  <a class="uart-ds-card" href="./rx6-u12h-m">
	<img src="../images/1.3.png" alt="PTC-32">
	<span class="uart-ds-label">PTC-32</span>
  </a>
</div>



#### 方案二（🚀 进阶拓展）

核心板 + UC-01 转接板 组合**
  适合已有主控板，或需要将舵机集成到更复杂机器人系统中的开发者，具备极高的灵活度。

<div class="uart-ds-grid">
  <a class="uart-ds-card" href="./hp6-u15h-m">
	<img src="../images/1.4.png" alt="UC-01">
	<span class="uart-ds-label">UC-01</span>
  </a>
  <a class="uart-ds-card" href="./rp6-u15h-m">
	<img src="../images/1.5.png" alt="STM32F103C8T6 Core">
	<span class="uart-ds-label">STM32F103C8T6 Core</span>
  </a>
</div>


## 2. 硬件连线说明


### 2.1 串口资源分配约定

在提供的 SDK 例程中，我们将 STM32F103 的硬件串口（UART）进行了标准化分配：

* `UART1`：**控制通信通道**。接总线伺服舵机转接板，用于下发控制指令与接收舵机反馈。
* `UART2`：**日志输出通道**（可选）。接 USB 转 TTL 模块，用于向 PC 端打印 `printf` 调试信息。
* `UART3`：预留，暂未使用。

### 2.2 物理接线拓扑

#### 程序下载接线 (ST-Link v2 <-> STM32)
用于烧录编译好的固件程序。

| ST-Link V2 引脚 | STM32 核心板引脚 |
| :-------------- | :--------------- |
| **SWDIO**       | SWIO / IO        |
| **SWCLK**       | SWCLK / CLK      |
| **GND**         | GND              |
| **3.3V**        | 3V3              |

#### 控制通信接线 (STM32 UART1 <-> 舵机转接板)

> [!TIP]
> 如使用STM32 多合一主控板(PTC-32) 则无需此步骤，此步骤仅用于方案二：核心板 + UC-01 转接板 组合

| STM32F103 GPIO       | 总线伺服舵机转接板UC01 | 连线说明                         |
| :------------------- | :--------------------- | :------------------------------- |
| **PA_9** (UART1 Tx)  | **Rx**                 | MCU 发送控制指令                 |
| **PA_10** (UART1 Rx) | **Tx**                 | MCU 接收舵机回传数据             |
| **5V**               | **5V**                 | 逻辑电平参考（视转接板供电而定） |
| **GND**              | **GND**                | 共地（必须连接）                 |

{{ fig_center("../images/link2.png", "硬件连线示意图", "500px") }}

#### 日志调试接线 (STM32 UART2 <-> USB 转 TTL) - 可选

| STM32F103 GPIO      | USB转TTL模块(外购) | 连线说明                   |
| :------------------ | :----------------- | :------------------------- |
| **PA_2** (UART2 Tx) | **Rx**             | MCU 输出 `printf` 日志     |
| **PA_3** (UART2 Rx) | **Tx**             | 接收 PC 端调试指令（预留） |
| **GND**             | **GND**            | 共地（必须连接）           |

#### 整体拓扑图

{{ fig_center("../images/01.png", "程序下载接线图", "500px") }}



## 3. 工程配置与编译结构

### 3.1 工程导入与 Keil5 配置

解压下载的 SDK 源码包 `fashionstar-uart-servo-stm32f103-master` 后，进入对应的例程目录。以下操作以“通讯检测”例程为例：

- **1.** <strong>打开工程</strong>：双击运行 <code>/FashionStarUartServo/Project/FashionStarUartServo.uvprojx</code> 启动 Keil5。

    {{ fig_indent_adjustable("../images/5.png","Keil工程界面", "100%", "3.5em") }}
    {{ fig_indent_adjustable("../images/6.png","Keil工程配置界面", "100%", "3.5em") }}

- **2.** <strong>配置编译器</strong>：确保工程使用的是 <strong>Use default compiler version 5</strong>（ARM Compiler 5），以保障兼容性。

    {{ fig_indent_adjustable("../images/7.png","编译器配置界面", "100%", "3.5em") }}
    {{ fig_indent_adjustable("../images/8.png","编译器版本配置", "100%", "3.5em") }}

- **3.** <strong>配置下载器</strong>：在 <code>Options for Target</code> -> <code>Debug</code> 选项卡中，选择实际使用的 Debugger（本手册标准配置为 <strong>ST-Link Debugger</strong>）。

    {{ fig_indent_adjustable("../images/9.png","下载器配置界面", "100%", "3.5em") }}

### 3.2 编译与固件下载

- **1.** 点击 Keil 顶部的 <code>Build</code> 按钮编译工程。检查下方 <code>Build Output</code> 窗口，确保提示 <code>0 Error(s), 0 Warning(s)</code>。

    {{ fig_indent_adjustable("../images/10.png","编译输出窗口", "100%", "3.5em") }}
    {{ fig_indent_adjustable("../images/11.png","编译成功提示", "100%", "3.5em") }}

- **2.** 将 ST-Link 插入电脑 USB 口，点击 <code>Download</code> 按钮将固件烧录至 STM32 芯片。

    {{ fig_indent_adjustable("../images/12.png","固件烧录按钮", "100%", "3.5em") }}

- **3.** 烧录完成后，按下 STM32 核心板上的 <strong>Reset（复位）按键</strong>，程序即可开始运行。
### 3.3 SDK 工程目录树解析

为了方便后续进行二次开发，建议您了解 SDK `User` 文件夹下的模块划分逻辑：

```text
├── fashion_star_uart_servo    // 核心：FashionStar 舵机通信协议封装层 API
│   ├── fashion_star_uart_servo.c
│   └── fashion_star_uart_servo.h
├── main.c                     // 业务层：用户主程序入口
├── ring_buffer                // 底层组件：C语言实现的环形缓冲队列（处理串口字节流）
│   ├── README.md
│   ├── ring_buffer.c
│   └── ring_buffer.h
├── stm32f10x_conf.h
├── sys_tick                   // 底层组件：系统时间管理（封装延时与倒计时函数）
│   ├── sys_tick.c
│   └── sys_tick.h
└── usart                      // 底层组件：串口通信驱动（提供宏定义快捷开关 UART1/2/3）
    ├── README.md
    ├── usart.c
    └── usart.h
```



<h3 align="center"><span style="color:#007ACC;">=== 第二篇：舵机功能 API 与核心例程 ===</span></h3>

---


## 4. 通讯检测 (Ping)

在进行复杂的运动控制前，首先需要验证物理链路与通信协议是否畅通。发送 Ping 指令可检测总线上特定 ID 的舵机是否在线。若舵机在线，将立刻返回包含其基本状态的响应数据包。

**函数原型**

```C
FSUS_STATUS FSUS_Ping(
    Usart_DataTypeDef *usart,
    uint8_t servo_id
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象指针（例如 `&usart1`）。
* `servo_id`：需要检测的舵机 ID 号。

**返回值**

- 返回状态码 `FSUS_STATUS`。
- 若请求成功则返回 `0` (`FSUS_STATUS_SUCCESS`)，非 0 值意味着通讯失败。
- 完整错误码请查阅 `fashion_star_uart_servo.h`。

**函数调用示例**

```c
statusCode = FSUS_Ping(servoUsart, servoId);
```

<a id="quick-ping"></a>
### ▶️ 检测舵机是否在线

**逻辑说明：**

- 持续向 0 号舵机发送通信检测指令，
- 根据应答状态码，在 UART2 日志串口中打印舵机的在线状态。

**完整示例代码**

```c
/********************************************************
 * 测试通信检测指令，测试舵机是否在线
 ********************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)  <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) <----> 总线伺服舵机转接板 Tx
// STM32F103 GND 	  <----> 总线伺服舵机转接板 GND
// STM32F103 V5 	  <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND 	 <----> USB转TTL GND
// STM32F103 V5 	 <----> USB转TTL 5V (可选)
// <注意事项>
// 使用前确保已设置usart.h里面的USART2_ENABLE为1
Usart_DataTypeDef* loggingUsart = &usart2;

// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
	while((loggingUsart->pUSARTx->SR&0X40)==0){}
	/* 发送一个字节数据到串口 */
	USART_SendData(loggingUsart->pUSARTx, (uint8_t) ch);
	/* 等待发送完毕 */
	// while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);		
	return (ch);
}

// 连接在转接板上的总线伺服舵机ID号
uint8_t servoId = 0; 
// 发送Ping请求的状态码
FSUS_STATUS statusCode; 

int main (void)
{
	// 嘀嗒定时器初始化
	SysTick_Init();
	// 串口初始化
	Usart_Init();
	
	while (1)
    {	
		printf("\r\n");
		// Ping一下舵机
		printf("[INFO]ping servo %d \r\n", servoId);
		statusCode = FSUS_Ping(servoUsart, servoId);
		printf("[INFO]status code %d \r\n", statusCode);
		
		// 根据状态码做不同的处理
		if (statusCode == FSUS_STATUS_SUCCESS){
			printf("[INFO]ping success, servo %d echo \r\n", servoId);
		}else{
			printf("[ERROR]ping fail, servo %d not online \r\n", servoId);
		}
		// 等待1000ms
		SysTick_DelayMs(1000);
    }
}
```

## 5. 单圈角度控制

> [!NOTE]
> * **指令覆盖**：舵机采取“最新指令优先”原则。连续下发角度控制命令时，新指令会立即覆盖前序指令。建议在连续动作间加入延时，或轮询读取当前角度判断动作是否完成。
> * **总线保护**：向同一舵机连续发送指令时，建议指令间隔保持在 10ms 以上。
> * **功率保持**：若 `power = 0` 或设置值大于系统功率保持值，舵机将默认按照设定的功率保持值执行（可通过上位机修改配置）。
> * **物理限制**：实际到达目标位置的时间受制于舵机型号的最大物理转速及当前外加负载。

### 简易单圈角度控制

最基础的点到点控制方式，要求舵机在指定的周期时间内运行到指定角度。
{{ fig_center("../images/5_1.png", "基础控制模式示意图", "500px") }}

**函数原型**

```c
FSUS_STATUS FSUS_SetServoAngle(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    float angle,
    uint16_t interval,
    uint16_t power,
    uint8_t wait
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。
* `servo_id`：目标舵机 ID。
* `angle`：目标绝对角度。最小单位 0.1°，取值范围 `[-180.0, 180.0]`。
* `interval`：期望的动作运行时间 (ms)。
* `power`：执行此动作时的最大功率限制 (mV)，默认为 `0`。
* `wait`：API 阻塞模式。`0` 表示非阻塞（指令下发即返回），`1` 表示阻塞等待（挂起直到舵机旋转到位）。

**函数调用示例**

```c
// 舵机控制相关的参数
uint8_t servoId = 0;  // 舵机的ID号
float angle = 0;// 舵机的目标角度  舵机角度在-180度到180度之间, 最小单位0.1°
uint16_t interval = 2000; // 运行时间ms  可以尝试修改设置更小的运行时间，例如500ms
uint16_t power = 0; // 舵机执行功率 单位mV 默认为0   
uint8_t wait = 0; //  API是否为阻塞式，0:不等待 1:等待舵机旋转到特定的位置; 

FSUS_SetServoAngle(servoUsart, servoId, angle, interval, power, wait);
```

### 高级单圈角度控制 (基于时间)

在基础控制上引入梯形速度规划。通过指定加速段时间与减速段时间，有效抑制启停瞬间的机械抖动与电流冲击。
{{ fig_center("../images/5_2.png", "梯形速度规划示意图", "500px") }}

**函数原型**

```c
FSUS_STATUS FSUS_SetServoAngleByInterval(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    float angle,
    uint16_t interval,
    uint16_t t_acc,
    uint16_t t_dec,
    uint16_t power,
    uint8_t wait
);
```

**参数说明**

* `interval`：总运行时间 (ms)，须满足 `interval > t_acc + t_dec`。
* `t_acc`：从静止加速到匀速阶段的耗时 (ms)，最小值 `> 20`。
* `t_dec`：从匀速状态减速到停止的耗时 (ms)，最小值 `> 20`。
*(其他参数同上)*


**函数调用示例**

```c
//// 舵机控制相关的参数
// 舵机的ID号
uint8_t servoId = 0;  
// 舵机的目标角度
// 舵机角度在-180度到180度之间, 最小单位0.1°
float angle = 0; 
// 运行时间ms  
// 可以尝试修改设置更小的运行时间，例如500ms
uint16_t interval = 2000; 
// 加速时间
uint16_t t_acc = 100;
// 减速时间
uint16_t t_dec = 150;
// 舵机执行功率 单位mV 默认为0   
uint16_t power = 0;
 //  API是否为阻塞式，0:不等待 1:等待舵机旋转到特定的位置; 
uint8_t wait = 0; 

FSUS_SetServoAngleByInterval(servo_usart, servo_id, angle, interval, t_acc, t_dec, power, wait);
```

### 高级单圈角度控制 (基于速度)

适用于需要舵机以特定“恒定物理速度”前往目标点的应用场景。
{{ fig_center("../images/5_3.png", "恒定速度控制示意图", "500px") }}

**函数原型**

```c
FSUS_STATUS FSUS_SetServoAngleByVelocity(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    float angle,
    float velocity,
    uint16_t t_acc,
    uint16_t t_dec,
    uint16_t power,
    uint8_t wait
);
```

**参数说明**

* `velocity`：目标巡航速度，单位 °/s。有效范围 `[1, 750]`。
*(其他参数同上)*


**函数调用示例**

```c
//// 舵机控制相关的参数
// 舵机的ID号
uint8_t servoId = 0;  
// 舵机的目标角度
// 舵机角度在-180度到180度之间, 最小单位0.1°
float angle = 0; 
// 目标转速
float velocity;
// 加速时间
uint16_t t_acc = 100;
// 减速时间
uint16_t t_dec = 150;
// 舵机执行功率 单位mV 默认为0   
uint16_t power = 0;
 //  API是否为阻塞式，0:不等待 1:等待舵机旋转到特定的位置; 
uint8_t wait = 0; 

FSUS_SetServoAngleByVelocity(servo_usart, servo_id, angle, velocity, t_acc, t_dec, power, wait);
```

### 单圈当前角度读取

读取舵机当前所在物理位置的绝对角度。

**函数原型**

```c
// 查询单个舵机的角度信息 angle 单位度
FSUS_STATUS FSUS_QueryServoAngle(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    float *angle
);
```

**函数调用示例**

```c
uint8_t servoId = 0;    // 舵机的ID号
float curAngle = 0;     // 舵机当前所在的角度
FSUS_QueryServoAngle(servoUsart, servoId, &curAngle); // 读取一下舵机的角度
//curAngle = 当前单圈角度
```

<a id="quick-single-complex"></a>
### ▶️ 控制单个舵机进行复杂运动

**逻辑说明：** 

- 演示上述三种单圈控制 API。
- 舵机将在不同控制模式下循环往复动作，并在每个动作完成后，通过回调查询 API 实时打印到达角度，方便开发者对比不同速度规划模式的运行特征。

**完整示例代码：**

```c
/********************************************************
 * 测试控制舵机的角度, 让舵机在两个角度之间做周期性旋转
 ********************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)    <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) 	<----> 总线伺服舵机转接板 Tx
// STM32F103 GND        <----> 总线伺服舵机转接板 GND
// STM32F103 V5         <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
Usart_DataTypeDef* servo_usart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
Usart_DataTypeDef* logging_usart = &usart2;



// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
    while((logging_usart->pUSARTx->SR&0X40)==0){}
    /* 发送一个字节数据到串口 */
    USART_SendData(logging_usart->pUSARTx, (uint8_t) ch);
    /* 等待发送完毕 */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}



//// 舵机控制相关的参数
// 舵机的ID号
uint8_t servo_id = 0;  
// 舵机的目标角度
// 舵机角度在-180度到180度之间, 最小单位0.1°
float angle = 0; 
// 运行时间ms  
// 可以尝试修改设置更小的运行时间，例如500ms
uint16_t interval;
// 目标转速
float velocity;
// 加速时间
uint16_t t_acc;
// 减速时间
uint16_t t_dec;
// 舵机执行功率 单位mV 默认为0   
uint16_t power = 0;
// 设置舵机角度的时候, 是否为阻塞式 
// 0:不等待 1:等待舵机旋转到特定的位置; 
uint8_t wait = 1; 
// 读取的角度
float angle_read;

int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();
    
    while (1){
        printf("GOTO: 135.0f\r\n");
        // 简易角度控制 + 当前角度查询
        angle = 135.0;
        interval = 2000;
        FSUS_SetServoAngle(servo_usart, servo_id, angle, interval, power, wait);
        FSUS_QueryServoAngle(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);
        
        // 等待2s
        SysTick_DelayMs(2000);
        
        // 带加减速的角度控制(指定周期) + 当前角度查询
        printf("GOTO+Interval: 0.0f\r\n");
        angle = 0.0f;
        interval = 1000;
        t_acc = 100;
        t_dec = 150;
        FSUS_SetServoAngleByInterval(servo_usart, servo_id, angle, interval, t_acc, t_dec, power, wait);
        FSUS_QueryServoAngle(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);
        
        // 等待2s
        SysTick_DelayMs(2000);
        
        // 带加减速的角度控制(指定转速) + 当前角度查询
        printf("GOTO+Velocity: -135.0f\r\n");
        angle = -135.0f;
        velocity = 200.0f;
        t_acc = 100;
        t_dec = 150;
        FSUS_SetServoAngleByVelocity(servo_usart, servo_id, angle, velocity, t_acc, t_dec, power, wait);
        FSUS_QueryServoAngle(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);
  }
}

```

**终端输出参考日志：可以观察到实际到达角度存在微小稳态误差**

```text
GOTO: 135.0f
Cur Angle: 134.7
GOTO+Interval: 0.0f
Cur Angle: 0.3
GOTO+Velocity: -135.0f
Cur Angle: -134.6
```

<a id="quick-multi-serial"></a>
### ▶️ 串行指令控制多舵机

**逻辑说明：**

- 采用非阻塞模式（`wait=0`）连续向总线抛出控制指令，
- 配合 MCU 主循环延时实现 0 号与 1 号舵机的基本协同工作。

> [!TIP]
> 若对多颗舵机联动同步性有极高要求，建议采用[同步指令](#9)。

**完整示例代码：**

```c
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)    <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) 	<----> 总线伺服舵机转接板 Tx
// STM32F103 GND        <----> 总线伺服舵机转接板 GND
// STM32F103 V5         <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 

//// 舵机控制相关的参数
// 运行时间ms  
// 可以尝试修改设置更小的运行时间，例如500ms
uint16_t interval = 2000; 
// 舵机执行功率 单位mV 默认为0   
uint16_t power = 0;
// 设置舵机角度的时候, 是否为阻塞式 
// 0:不等待 1:等待舵机旋转到特定的位置; 
uint8_t wait = 0; 

int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();
    
    while (1)
    {   
        // 简易角度控制指令，控制0和1号舵机
        FSUS_SetServoAngle(servoUsart, 0, 135.0, interval, power, wait);
        FSUS_SetServoAngle(servoUsart, 1, 45.0, interval, power, wait);
        // 等待动作完成
        SysTick_DelayMs(interval);
        
        // 等待2s
        SysTick_DelayMs(2000);
        
        // 简易角度控制指令，控制0和1号舵机
        FSUS_SetServoAngle(servoUsart, 0, -135.0, interval, power, wait);
        FSUS_SetServoAngle(servoUsart, 1, -45.0, interval, power, wait);
        // 等待动作完成
        SysTick_DelayMs(interval);
        
        // 等待2s
        SysTick_DelayMs(2000);
    }
}
```

<a id="quick-deadzone-loop"></a>
### ▶️ 死区评估与自主运动闭环

**逻辑说明：** 

- 在机器人运动学开发中，MCU 常需精准获知关节是否真正物理"到位"。
- 本例程演示了如何根据目标偏差自动计算预估执行时间，并通过高频轮询当前角度（引入 `servoDeadBlock` 死区容差），实现高强度的软件级位置闭环验证。

**完整示例代码：**

```c
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)    <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx)   <----> 总线伺服舵机转接板 Tx
// STM32F103 GND        <----> 总线伺服舵机转接板 GND
// STM32F103 V5         <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
// <注意事项>
// 使用前确保已设置usart.h里面的USART2_ENABLE为1
Usart_DataTypeDef* loggingUsart = &usart2;

// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
    while((loggingUsart->pUSARTx->SR&0X40)==0){}
    /* 发送一个字节数据到串口 */
    USART_SendData(loggingUsart->pUSARTx, (uint8_t) ch);
    /* 等待发送完毕 */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}

// 舵机控制相关的参数
uint8_t servoId = 0;    // 舵机的ID
float curAngle = 0;     // 舵机当前所在的角度
float nextAngle = 0;    // 舵机的目标角度
uint16_t speed = 200;   // 舵机的转速 单位 °/s
uint16_t interval = 0;  // 舵机旋转的周期
uint16_t power = 0;     // 舵机执行功率 单位mV 默认为0
uint8_t wait = 0;       // 0:不等待 1:等待舵机旋转到特定的位置;
// 舵机角度死区, 如果舵机当前角度跟
// 目标角度相差小于死区则代表舵机到达目标角度, 舵机不再旋转
// <注意事项>
//      死区跟舵机的型号有关系, 取决于舵机固件的设置, 不同型号的舵机会有差别
float servoDeadBlock = 1.0; 

// 查询舵机的角度
uint16_t calcIntervalMs(uint8_t servoId, float nextAngle, float speed){
    // 读取一下舵机的角度
    FSUS_QueryServoAngle(servoUsart, servoId, &curAngle);
    // 计算角度误差
    float dAngle =  (nextAngle > curAngle) ? (nextAngle - curAngle) : (curAngle - nextAngle);
    // 计算所需的时间
    return (uint16_t)((dAngle / speed) * 1000.0);
}

// 等待舵机进入空闲状态IDLE, 即舵机到达目标角度
void waitUntilServoIDLE(uint8_t servoId, float nextAngle){
    
    while(1){
        // 读取一下舵机的角度
        FSUS_QueryServoAngle(servoUsart, servoId, &curAngle);
        
        // 判断舵机是否达到目标角度
        float dAngle =  (nextAngle > curAngle) ? (nextAngle - curAngle) : (curAngle - nextAngle);
        
        // 打印一下当前的舵机角度
        printf("curAngle: %f dAngle: %f\r\n", curAngle, dAngle);
        
        // 判断是否小于死区
        if (dAngle <= servoDeadBlock){
            break;
        }
        // 等待一小段时间
        SysTick_DelayMs(5);
    }
}


int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();
    
    while (1)
    {   
        // 设置舵机的目标角度
        nextAngle = 120.0;
        // 根据转速还有角度误差计算周期
        interval = calcIntervalMs(servoId, nextAngle, speed);
        printf("Set Servo %f-> %f", curAngle, nextAngle);
        // 控制舵机角度
        FSUS_SetServoAngle(servoUsart, servoId, nextAngle, interval, power, wait);
        // SysTick_DelayMs(interval);
        SysTick_DelayMs(5);
        waitUntilServoIDLE(servoId, nextAngle);
        
        // 等待1s 看舵机死区范围
        SysTick_DelayMs(1000);
        // 读取一下舵机的角度
        FSUS_QueryServoAngle(servoUsart, servoId, &curAngle);
        printf("Final Angle: %f", curAngle);
        SysTick_DelayMs(1000);
        
        // 设置舵机的目标角度
        nextAngle = -120;
        // 根据转速还有角度误差计算周期
        interval = calcIntervalMs(servoId, nextAngle, speed);
        // 控制舵机角度
        FSUS_SetServoAngle(servoUsart, servoId, nextAngle, interval, power, wait);
        // 需要延时一会儿，确保舵机接收并开始执行舵机控制指令
        // 如果马上发送舵机角度查询信息,新发送的这条指令可能会覆盖舵机角度控制信息
        SysTick_DelayMs(5);
        waitUntilServoIDLE(servoId, nextAngle);
        
        // 等待1s 看舵机死区范围
        SysTick_DelayMs(1000);
        // 读取一下舵机的角度
        FSUS_QueryServoAngle(servoUsart, servoId, &curAngle);
        printf("Final Angle: %f", curAngle);
        SysTick_DelayMs(1000);
    }
}
```

---

## 6. 多圈角度控制

> [!NOTE]
> * **指令覆盖**：舵机采取“最新指令优先”原则。连续下发角度控制命令时，新指令会立即覆盖前序指令。建议在连续动作间加入延时，或轮询读取当前角度判断动作是否完成。
> * **总线保护**：向同一舵机连续发送指令时，建议指令间隔保持在 10ms 以上。
> * **功率保持**：若 `power = 0` 或设置值大于系统功率保持值，舵机将默认按照设定的功率保持值执行（可通过上位机修改配置）。
> * **物理限制**：实际到达目标位置的时间受制于舵机型号的最大物理转速及当前外加负载。
> * 多圈控制打破了传统单圈 `[-180°, +180°]` 的物理死区界限，特别适用于需要连续卷线、滑轨驱动、连续旋转台等场景。
> * 控制参数的逻辑与约束与单圈模式基本一致，但目标角度 `angle` 的有效取值范围大幅度扩展。

### 简易多圈角度控制

{{ fig_center("../images/6_1.png", "简易多圈控制曲线", "500px") }}

**函数原型**

```c
FSUS_STATUS FSUS_SetServoAngleMTurn(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    float angle,
    uint32_t interval,
    uint16_t power,
    uint8_t wait
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。
* `servo_id`：目标舵机 ID。
* `angle`：多圈目标绝对角度，最小单位 0.1°，取值跃升至 `[-368640.0°, 368640.0°]`（约合 ±1024 圈）。
* `interval`：期望的动作运行时间 (ms)。
* `power`：执行此动作时的最大功率限制 (mV)，默认为 `0`。
* `wait`：API 阻塞模式。`0` 表示非阻塞（指令下发即返回），`1` 表示阻塞等待（挂起直到舵机旋转到位）。

**函数调用示例**

```C
//// 舵机控制相关的参数
// 舵机的ID号
uint8_t servo_id = 0;  
// 舵机的目标角度
float angle= 720.0f; 
uint32_t interval = 2000; 	// 运行时间ms  
// 舵机执行功率，单位mV，默认为0	
uint16_t power = 0;
 //  API是否为阻塞式，0:不等待 1:等待舵机旋转到特定的位置; 
uint8_t wait = 0; 

FSUS_SetServoAngleMTurn(servo_usart, servo_id, angle, interval, power, wait);
```

### 高级多圈角度控制 (基于时间)

{{ fig_center("../images/6_2.png", "高级多圈角度控制曲线 (基于时间)", "500px") }}

**函数原型**

```c
FSUS_STATUS FSUS_SetServoAngleMTurnByInterval(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    float angle,
    uint32_t interval,
    uint16_t t_acc,
    uint16_t t_dec,
    uint16_t power,
    uint8_t wait
);
```

**参数说明**

* `interval`：总运行时间 (ms)，须满足 `interval > t_acc + t_dec`。
* `t_acc`：从静止加速到匀速阶段的耗时 (ms)，最小值 `> 20`。
* `t_dec`：从匀速状态减速到停止的耗时 (ms)，最小值 `> 20`。
  *(其他参数同上)*

**函数调用示例**

```c
//// 舵机控制相关的参数
// 舵机的ID号
uint8_t servo_id = 0;  
// 舵机的目标角度
float angle= 720.0f; 
uint32_t interval = 2000; 	// 运行时间ms  
// 舵机执行功率，单位mV，默认为0	
uint16_t power = 0;
 //  API是否为阻塞式，0:不等待 1:等待舵机旋转到特定的位置; 
uint8_t wait = 1; 
// 加速时间(单位ms)
uint16_t t_acc = 100;
// 减速时间
uint16_t t_dec = 200;

FSUS_SetServoAngleMTurnByInterval(servo_usart, servo_id, angle, interval, t_acc, t_dec, power, wait);
```

### 高级多圈角度控制 (基于速度)

{{ fig_center("../images/6_3.png", "高级多圈角度控制曲线 (基于速度)", "500px") }}

**函数原型**

```c
FSUS_STATUS FSUS_SetServoAngleMTurnByVelocity(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    float angle,
    float velocity,
    uint16_t t_acc,
    uint16_t t_dec,
    uint16_t power,
    uint8_t wait
);
```

**参数说明**

* `velocity`：目标巡航速度，单位 °/s。有效范围 `[1, 750]`。
  *(其他参数同上)*

**函数调用示例**

```c
//// 舵机控制相关的参数
// 舵机的ID号
uint8_t servo_id = 0;  
// 舵机的目标角度
float angle= 720.0f; 
float velocity = 100.0f;	// 电机转速, 单位dps,°/s 
// 舵机执行功率，单位mV，默认为0	
uint16_t power = 0;
 //  API是否为阻塞式，0:不等待 1:等待舵机旋转到特定的位置; 
uint8_t wait = 1; 
// 加速时间(单位ms)
uint16_t t_acc = 100;
// 减速时间
uint16_t t_dec = 200;

FSUS_SetServoAngleMTurnByVelocity(servo_usart, servo_id, angle, velocity, t_acc, t_dec, power, wait);
```

### 多圈当前角度读取

**函数原型**

```c
FSUS_STATUS FSUS_QueryServoAngleMTurn(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    float *angle
);
```

**函数调用示例**

```C
uint8_t servoId = 0;    // 舵机的ID号
float curAngle = 0;     // 舵机当前所在的角度
FSUS_QueryServoAngleMTurn(servoUsart, servoId, &curAngle); // 读取一下舵机的角度
//curAngle = 当前单圈角度
```

### 重置圈数

> [!NOTE]
> 在圈数重置前，必须先发送 **停止指令-失锁卸力** 指令，确保舵机处于自由状态。

通过指令重置舵机的 圈数信息，将当前绝对位置的角度重新记录为当前角度，角度范围 `[-180.0, 180.0]`。

**函数原型**

```C
FSUS_STATUS FSUS_ServoAngleReset(
    Usart_DataTypeDef *usart,
    uint8_t servo_id
);
```

**函数调用示例**

```C
uint8_t servoId = 0;    // 舵机的ID号
FSUS_ServoAngleReset(servoUsart, servoId); // 清除多圈圈数
```

<a id="quick-mturn-control"></a>
### ▶️ 多圈大角度运动控制

**逻辑说明：** 

- 演示舵机转动720度（两圈），再反转回到 0 度位置，并在控制过程中实时打印多圈角度。
- 该例程演示了以上三种多圈角度控制以及查询实时多圈角度的API使用方法

**完整示例代码：**

```c
/********************************************************
 * 舵机多圈控制模式演示
 ********************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx) 	<----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) 	<----> 总线伺服舵机转接板 Tx
// STM32F103 GND 		<----> 总线伺服舵机转接板 GND
// STM32F103 V5 		<----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servo_usart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
// <注意事项>
// 使用前确保已设置usart.h里面的USART2_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* loggingUsart = &usart2;

// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
	while((loggingUsart->pUSARTx->SR&0X40)==0){}
	/* 发送一个字节数据到串口 */
	USART_SendData(loggingUsart->pUSARTx, (uint8_t) ch);
	/* 等待发送完毕 */
	// while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);		
	return (ch);
}


// 使用串口3作为舵机控制的端口
// <接线说明>
// STM32F103 PB10(Tx) 	<----> 总线伺服舵机转接板 Rx
// STM32F103 PB11(Rx) 	<----> 总线伺服舵机转接板 Tx
// STM32F103 GND 		<----> 总线伺服舵机转接板 GND
// STM32F103 V5 		<----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
// Usart_DataTypeDef* servo_usart = &usart3; 

//// 舵机控制相关的参数
// 舵机的ID号
uint8_t servo_id = 0;  
// 舵机的目标角度
// 舵机角度在-135度到135度之间, 精确到小数点后一位
float angle; 
uint32_t interval; 	// 运行时间ms  
float velocity; 		// 电机转速, 单位dps,°/s
// 舵机执行功率 单位mV，默认为0	
uint16_t power = 0;
// 设置舵机角度的时候, 是否为阻塞式 
// 0:不等待 1:等待舵机旋转到特定的位置; 
uint8_t wait = 1; 
// 加速时间(单位ms)
uint16_t t_acc;
// 减速时间
uint16_t t_dec;

// 读取的角度
float angle_read;
int main (void)
{
	// 嘀嗒定时器初始化
	SysTick_Init();
	// 串口初始化
	Usart_Init();
	
	while (1){	
		printf("MTurn GOTO: 720.0f\r\n");
		//简易多圈角度控制 + 当前多圈角度查询
		angle = 720.0f;
		interval = 2000;
		FSUS_SetServoAngleMTurn(servo_usart, servo_id, angle, interval, power, wait);
		FSUS_QueryServoAngleMTurn(servo_usart, servo_id, &angle_read);
		printf("Cur Angle: %.1f\r\n", angle_read);
		
		// 等待2s
		SysTick_DelayMs(2000);
		
		
		printf("MTurn GOTO: 0.0f\r\n");
		angle = 0.0;
		FSUS_SetServoAngleMTurn(servo_usart, servo_id, angle, interval, power, wait);
		FSUS_QueryServoAngleMTurn(servo_usart, servo_id, &angle_read);
		printf("Cur Angle: %.1f\r\n", angle_read);
		
		// 等待2s
		SysTick_DelayMs(2000);
		
		
		//带加减速的多圈角度控制(指定周期) + 当前多圈角度查询
		printf("MTurn+Interval GOTO: -180.0f\r\n");
		angle = 180.0f;	
		interval = 1000;
		t_acc = 100;
		t_dec = 200;
		FSUS_SetServoAngleMTurnByInterval(servo_usart, servo_id, angle, interval, t_acc, t_dec, power, wait);
		FSUS_QueryServoAngleMTurn(servo_usart, servo_id, &angle_read);
		printf("Cur Angle: %.1f\r\n", angle_read);
		
		// 等待2s
		SysTick_DelayMs(2000);
		
		//带加减速的多圈角度控制(指定转速) + 当前多圈角度查询
		printf("MTurn+Velocity GOTO: -180.0f\r\n");
		angle = -180.0f;
		velocity = 100.0f;
		t_acc = 100;
		t_dec = 200;
		FSUS_SetServoAngleMTurnByVelocity(servo_usart, servo_id, angle, velocity, t_acc, t_dec, power, wait);
		FSUS_QueryServoAngleMTurn(servo_usart, servo_id, &angle_read);
		printf("Cur Angle: %.1f\r\n", angle_read);
		
		// 等待2s
		SysTick_DelayMs(2000);
		
  }
}

```

**终端输出日志参考**

```text
MTurn GOTO: 720.0f
Cur Angle: 719.7
MTurn GOTO: 0.0f
Cur Angle: 0.4
MTurn+Interval GOTO: -180.0f
Cur Angle: 179.7
MTurn+Velocity GOTO: -180.0f
Cur Angle: -179.5
MTurn GOTO: 720.0f
Cur Angle: 719.5
MTurn GOTO: 0.0f
Cur Angle: 0.4
MTurn+Interval GOTO: -180.0f
Cur Angle: 179.7
MTurn+Velocity GOTO: -180.0f
Cur Angle: -179.5
```



<a id="quick-wheel-keep"></a>
### ▶️ 舵机持续旋转

**完整示例代码：**

```c
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)  <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) <----> 总线伺服舵机转接板 Tx
// STM32F103 GND 	  <----> 总线伺服舵机转接板 GND
// STM32F103 V5 	  <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 

FSUS_STATUS statusCode; // 请求包的状态码
uint8_t servoId = 0; 	// 连接在转接板上的总线伺服舵机ID号
uint16_t speed = 20; 	// 舵机的旋转速度 20°/s
uint8_t is_cw = 0; 		// 舵机的旋转方向
int main (void)
{
	// 嘀嗒定时器初始化
	SysTick_Init();
	// 串口初始化
	Usart_Init();
	
	while (1){
		// 舵机轮式模式定速控制 顺时针旋转3s
		is_cw = 1;
		FSUS_WheelKeepMove(servoUsart, servoId, is_cw, speed);
		SysTick_DelayMs(3000);
		
		// 舵机刹车 停顿2s 
		FSUS_WheelStop(servoUsart, servoId);
		SysTick_DelayMs(1000);
		
		// 舵机轮式模式定速控制 逆时针旋转3s
		is_cw = 0;
		FSUS_WheelKeepMove(servoUsart, servoId, is_cw, speed);
		SysTick_DelayMs(3000);
		
		// 舵机刹车 停顿2s 
		FSUS_WheelStop(servoUsart, servoId);
		SysTick_DelayMs(1000);
	}
}
```

<a id="quick-wheel-timed"></a>
### ▶️ 舵机定时旋转

**完整示例代码：**

```c
/***************************************************
 * 轮式控制模式 定时旋转
 * <注意事项>
 * 在测试本例程时, 请确保舵机没有机械结构/接线的约束, 
 * 舵机可以360度旋转
 ***************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)  <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) <----> 总线伺服舵机转接板 Tx
// STM32F103 GND 	  <----> 总线伺服舵机转接板 GND
// STM32F103 V5 	  <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 

FSUS_STATUS statusCode; // 请求包的状态码
uint8_t servoId = 0; 	// 连接在转接板上的总线伺服舵机ID号
uint16_t speed = 20; 	// 舵机的旋转速度 20°/s
uint8_t is_cw = 0; 		// 舵机的旋转方向
uint16_t nTime = 3000; 	// 延时时间
int main (void)
{
	// 嘀嗒定时器初始化
	SysTick_Init();
	// 串口初始化
	Usart_Init();
	
	while (1){
		// 舵机轮式模式定速控制 顺时针旋转3s
		is_cw = 1;
		FSUS_WheelMoveTime(servoUsart, servoId, is_cw, speed, nTime);
		// FSUS_WheelMoveTime是非阻塞的,因为有时候需要控制多个舵机同时旋转
		// 所以在后面要手动加延迟
		SysTick_DelayMs(nTime);
		
		// 停顿1s 
		SysTick_DelayMs(1000);
		
		// 舵机轮式模式定速控制 逆时针旋转3s
		is_cw = 0;
		FSUS_WheelMoveTime(servoUsart, servoId, is_cw, speed, nTime);
		SysTick_DelayMs(nTime);
		
		// 停顿1s 
		SysTick_DelayMs(1000);
	}
}
```

<a id="quick-wheel-circle"></a>
### ▶️ 舵机定圈旋转

**完整示例代码：**

```c
/***************************************************
 * 轮式模式 定圈旋转
 * <注意事项>
 * 在测试本例程时, 请确保舵机没有机械结构/接线的约束, 
 * 舵机可以360度旋转
 ***************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)  <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) <----> 总线伺服舵机转接板 Tx
// STM32F103 GND 	  <----> 总线伺服舵机转接板 GND
// STM32F103 V5 	  <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 

FSUS_STATUS statusCode; // 请求包的状态码
uint8_t servoId = 0; 	// 连接在转接板上的总线伺服舵机ID号
uint16_t speed = 200; 	// 舵机的旋转速度 单位°/s
uint8_t is_cw = 0; 		// 舵机的旋转方向
uint16_t nCircle = 1; 	// 舵机旋转的圈数

// 估计旋转圈数所需要花费的时间
uint16_t estimateTimeMs(uint16_t nCircle, uint16_t speed){
	return (uint16_t)((float)nCircle * 360.0 / (float)speed * 1000);
}

int main (void)
{
	// 嘀嗒定时器初始化
	SysTick_Init();
	// 串口初始化
	Usart_Init();
	
	while (1){
		// 舵机轮转模式定速控制 顺时针旋转1圈
		is_cw = 1;
		FSUS_WheelMoveNCircle(servoUsart, servoId, is_cw, speed, nCircle);
		// FSUS_WheelMoveNCircle是非阻塞的,因为有时候需要控制多个舵机同时旋转
		// 延时估算所需时间
		SysTick_DelayMs(estimateTimeMs(nCircle, speed));
		
		// 停顿1s 
		SysTick_DelayMs(1000);
		
		// 舵机轮转模式定速控制 逆时针旋转1圈
		is_cw = 0;
		FSUS_WheelMoveNCircle(servoUsart, servoId, is_cw, speed, nCircle);
		// 注意: FSUS_WheelMoveNCircle是非阻塞的,因为有时候需要控制多个舵机同时旋转
		// 延时估算所需时间
		SysTick_DelayMs(estimateTimeMs(nCircle, speed));
		
		// 停顿1s 
		SysTick_DelayMs(1000);
	}
}
```

## 7. 阻尼模式

通过调节电机的电磁阻尼系数，让舵机在失去绝对刚性锁定状态时，能够提供一种“类似于浸泡在黏稠液体中”的抵抗外力的平滑阻力。非常适用于机械臂被动示教、重力降落缓冲等场景。

**函数原型**

```c
// 舵机阻尼模式
FSUS_STATUS FSUS_DampingMode(
    Usart_DataTypeDef *usart,
    uint8_t servoId,
    uint16_t power
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。
* `servoId`：目标舵机的 ID。
* `power`：配置该阻尼模式下的响应功率，单位 mW。设定的功率越大，外力试图转动舵机时感受到的迟滞阻力就越明显。

**函数调用示例**

```c
// 连接在转接板上的总线伺服舵机ID号
uint8_t servoId = 0; 
// 阻尼模式下的功率，功率越大阻力越大
uint16_t power = 500;
// 设置舵机为阻尼模式
FSUS_DampingMode(servoUsart, servoId, power);
```

<a id="quick-damping-feel"></a>
### ▶️ 体验阻尼手感

**逻辑说明：** 

- 开启阻尼模式后系统空闲挂起。
- 可以尝试用手直接扭动舵机输出轴，体会 `power = 500` 带来的特定柔性阻力。

**完整示例代码：**

```c
/***************************************************
 * 总线伺服舵机阻尼模式
 ***************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)  <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) <----> 总线伺服舵机转接板 Tx
// STM32F103 GND 	  <----> 总线伺服舵机转接板 GND
// STM32F103 V5 	  <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 

// 连接在转接板上的总线伺服舵机ID号
uint8_t servoId = 0; 
// 阻尼模式下的功率，功率越大阻力越大
uint16_t power = 500;
int main (void)
{
	// 嘀嗒定时器初始化
	SysTick_Init();
	// 串口初始化
	Usart_Init();
	// 设置舵机为阻尼模式
	FSUS_DampingMode(servoUsart, servoId, power);
	while (1)
    {	
		//主循环什么也不做
		// 等待1000ms
		SysTick_DelayMs(1000);
    }
}
```

<a id="quick-damping-track"></a>
### ▶️ 阻尼模式与运动轨迹捕获

**逻辑说明：** 

- 结合阻尼模式和位置查询功能，实现类似"机械臂动作示教"的效果。MCU 会实时捕获并打印您手动扭动舵机的拖拽轨迹。

**完整示例代码：**

```c
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)  <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) <----> 总线伺服舵机转接板 Tx
// STM32F103 GND 	  <----> 总线伺服舵机转接板 GND
// STM32F103 V5 	  <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 
// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND 	 <----> USB转TTL GND
// STM32F103 V5 	 <----> USB转TTL 5V (可选)
// <注意事项>
// 使用前确保已设置usart.h里面的USART2_ENABLE为1
Usart_DataTypeDef* loggingUsart = &usart2;

// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
	while((loggingUsart->pUSARTx->SR&0X40)==0){}
	/* 发送一个字节数据到串口 */
	USART_SendData(loggingUsart->pUSARTx, (uint8_t) ch);
	/* 等待发送完毕 */
	// while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);		
	return (ch);
}

FSUS_STATUS statusCode; // 请求包的状态码
uint8_t servoId = 0; 	// 连接在转接板上的总线伺服舵机ID号
uint16_t power = 500; 	// 阻尼模式下的功率，功率越大阻力越大
float angle = 0; 		// 舵机的角度

int main (void)
{
	// 嘀嗒定时器初始化
	SysTick_Init();
	// 串口初始化
	Usart_Init();
	// 设置舵机为阻尼模式
	FSUS_DampingMode(servoUsart, servoId, power);
	while (1)
    {	
		// 读取一下舵机的角度
		statusCode = FSUS_QueryServoAngle(servoUsart, servoId, &angle);
		
		if (statusCode ==FSUS_STATUS_SUCCESS){
			// 成功的读取到了舵机的角度
			printf("[INFO] servo id= %d ; angle = %f\r\n", servoId, angle);
		}else{
			// 没有正确的读取到舵机的角度
			printf("\r\n[INFO] read servo %d angle, status code: %d \r\n", servoId, statusCode);
			printf("[ERROR]failed to read servo angle\r\n");
		}
		// 等待1000ms
		SysTick_DelayMs(500);
    }
}
```

---

## 8. 停止指令

提供了三种停止模式，停止卸力失锁、保持当前位置维持锁力、进入阻尼模式。

> [!TIP]
> 该指令也可以用于使能舵机扭力，当伺服舵机在失锁状态下，发送 **保持锁力** 指令，可使其从当前位置重建锁力

**函数原型**

```c
FSUS_STATUS FSUS_StopOnControlMode(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    uint8_t mode,
    uint16_t power
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。
* `servo_id`：目标舵机 ID。
* `mode`：停止模式编号设定。
  * `0` - 完全卸力失锁（自由可掰动状态）。
  * `1` - 保持绝对位置锁力（当前位置锁定状态）。
  * `2` - 切入电磁阻尼状态（带迟滞柔感）。
* `power`：若模式选择了 `2` (阻尼)，此参数负责设定进入阻尼后的有效功率上限 (mW)。

**函数调用示例**

```c
/* 舵机控制模式停止指令*/
//mode 指令停止形式
//0-停止后卸力(失锁)
//1-停止后保持锁力
//2-停止后进入阻尼状态
uint8_t stopcolmode=0;
uint8_t servo_id = 0; 	// 连接在转接板上的总线伺服舵机ID号
uint16_t power = 500;  //功率
FSUS_StopOnControlMode(servoUsart, servo_id, stopcolmode, power);
```

<a id="quick-stop-to-damping"></a>
### ▶️ 动作执行成功自动切入阻尼

**逻辑说明：** 

- 演示了一个典型的工作流：指令舵机动作 -> 等待其动作周期结束 -> 立刻将内部电控模式切换为 `stopcolmode=2` 进入阻尼模式。

**完整示例代码：**

```c
/********************************************************
* 控制舵机执行完指令进入阻尼状态
 ********************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)    <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx)   <----> 总线伺服舵机转接板 Tx
// STM32F103 GND        <----> 总线伺服舵机转接板 GND
// STM32F103 V5         <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
Usart_DataTypeDef* servo_usart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
Usart_DataTypeDef* logging_usart = &usart2;

// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
    while((logging_usart->pUSARTx->SR&0X40)==0){}
    /* 发送一个字节数据到串口 */
    USART_SendData(logging_usart->pUSARTx, (uint8_t) ch);
    /* 等待发送完毕 */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}


//0-停止后卸力(失锁)
//1-停止后保持锁力
//2-停止后进入阻尼状态
uint8_t stopcolmode=2;
	
float	angle = 135.0;// 舵机的目标角度
uint16_t interval = 1000;// 时间间隔ms
uint16_t	power = 500;// 舵机执行功率
uint8_t servo_id=0;// 舵机的ID号

int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();

  	FSUS_SetServoAngle(servo_usart, servo_id, angle, interval, power);
	SysTick_DelayMs(2000);
	
	//停止后进入对应状态
	FSUS_StopOnControlMode(servo_usart, servo_id, stopcolmode, power);
	SysTick_DelayMs(1000);
    while (1){
			
  }
}
```

---

## 9. 同步指令

在开发如机械臂、人形机器人那么多轴联动的设备时，如果采用普通的“轮询式串行通信”，各个关节接收到指令将产生微小的时差，导致运动姿态变形。

`FSUS_SyncCommand` 允许主机一次性将所有关节的目标参数“打包”成一个长指令发送到总线上。所有在线舵机将在硬件层面临近的微妙级时间内统一触发，保证运动学算法的完美复现。

**函数原型**

```c
FSUS_STATUS FSUS_SyncCommand(
    Usart_DataTypeDef *usart,
    uint8_t servo_count,
    uint8_t ServoMode,
    FSUS_sync_servo servoSync[]
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。
* `servo_count`：本次参与同步控制的舵机数量。
* `ServoMode`：声明这批群控指令的具体用途。
  * `1`：简易角度控制
  * `2`：带加减速的角度控制 (指定周期)
  * `3`：带加减速的角度控制 (指定转速)
  * `4`：简易多圈角度控制
  * `5`：带加减速的多圈角度控制 (指定周期)
  * `6`：带加减速的多圈角度控制 (指定转速)
  * `7`：数据监控
* `servoSync[]`：用于存放待下发给各节点控制参数的核心结构体数组。

**函数调用示例**

```c
/*同步指令模式选择
* 1：设置舵机的角度
* 2：设置舵机的角度(指定周期)
* 3：设置舵机的角度(指定转速)
* 4：设置舵机的角度(多圈模式)
* 5：设置舵机的角度(多圈模式, 指定周期) 
* 6：设置舵机的角度(多圈模式, 指定转速)
* 7：读取舵机的数据*/
uint8_t sync_mode=1;//同步指令模式

uint8_t sync_count=5;//舵机数量

//数组定义在#include "fashion_star_uart_servo.c" 
FSUS_sync_servo SyncArray[20]; // 假设您要控制20个伺服同步
ServoData servodata[20];//假设您要读取20个伺服舵机的数据

//如需更改舵机数量在#include "fashion_star_uart_servo.h"对应修改extern
extern FSUS_sync_servo SyncArray[20]; // 假设您要控制20个伺服同步
extern ServoData servodata[20];//假设您要读取20个伺服舵机的数据

servoSyncArray[0].angle=90;/*角度*/
servoSyncArray[0].id=0;/*舵机ID号*/
servoSyncArray[0].velocity=100;/*速度*/				 servoSyncArray[0].interval_single=1000;/*单圈时间*/	servoSyncArray[0].interval_multi=1000; /*多圈时间*/		servoSyncArray[0].t_acc=100;/*加速时间*/    
servoSyncArray[0].t_dec=100;/*减速时间*/				servoSyncArray[0].power=100;/*功率*/
/*********************************以此类推赋值剩下舵机参数 灵活性高**************************************/

FSUS_SyncCommand(servo_usart, servo_count, servomode, servoSyncArray);
```

<a id="quick-sync-ms"></a>
### ▶️ 系统毫秒级同步协同

**逻辑说明：** 

- 演示如何填充 `SyncArray` 结构体，将 5 台舵机（ID:0~4）的控制参数拼接打包，并向总线广播，确保所有轴能够高实时性地同步启动并到达目标位姿。
- 随后立刻广播模式 7 读取最新系统状态。

**完整示例代码：**

```c
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)  <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) <----> 总线伺服舵机转接板 Tx
// STM32F103 GND 	  <----> 总线伺服舵机转接板 GND
// STM32F103 V5 	  <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef* servoUsart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
Usart_DataTypeDef* logging_usart = &usart2;



// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
    while((logging_usart->pUSARTx->SR&0X40)==0){}
    /* 发送一个字节数据到串口 */
    USART_SendData(logging_usart->pUSARTx, (uint8_t) ch);
    /* 等待发送完毕 */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}

/*同步指令模式选择
* 1：设置舵机的角度
* 2：设置舵机的角度(指定周期)
* 3：设置舵机的角度(指定转速)
* 4：设置舵机的角度(多圈模式)
* 5：设置舵机的角度(多圈模式, 指定周期) 
* 6：设置舵机的角度(多圈模式, 指定转速)
* 7：读取舵机的数据*/
uint8_t servomode=1;//自行更改数值设置模式

//舵机数量，如果id不是从0开始，请把参数设置为最大舵机id号
uint8_t servo_count=5;

int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();

    while (1){
			
   	SyncArray[0].angle=90;
		SyncArray[0].id=0;SyncArray[0].interval_single=100;SyncArray[0].interval_multi=1000;SyncArray[0].velocity=100;SyncArray[0].t_acc=20;SyncArray[0].t_dec=20;
		SyncArray[1].angle=-90;
		SyncArray[1].id=1;SyncArray[1].interval_single=100;SyncArray[1].interval_multi=1000;SyncArray[1].velocity=100;SyncArray[1].t_acc=20;SyncArray[1].t_dec=20;
		SyncArray[2].angle=90;
		SyncArray[2].id=2;SyncArray[2].interval_single=100;SyncArray[2].interval_multi=1000;SyncArray[2].velocity=100;SyncArray[2].t_acc=20;SyncArray[2].t_dec=20;
		SyncArray[3].angle=-90;
		SyncArray[3].id=3;SyncArray[3].interval_single=100;SyncArray[3].interval_multi=1000;SyncArray[3].velocity=100;SyncArray[3].t_acc=20;SyncArray[3].t_dec=20;
		SyncArray[4].angle=-90;
		SyncArray[4].id=4;SyncArray[4].interval_single=100;SyncArray[4].interval_multi=1000;SyncArray[4].velocity=100;SyncArray[4].t_acc=20;SyncArray[4].t_dec=20;
		//发送同步指令控制
		FSUS_SyncCommand(servo_usart,sync_count,servomode,SyncArray);
		SysTick_DelayMs(1000);
		//发送同步指令读取
		FSUS_SyncCommand(servo_usart,sync_count,7,SyncArray);
		SysTick_DelayMs(200);

		SyncArray[0].angle=45;SyncArray[0].interval_single=0;SyncArray[0].velocity=20;
		SyncArray[1].angle=-45;SyncArray[1].interval_single=0;SyncArray[1].velocity=20;
		SyncArray[2].angle=45;SyncArray[2].interval_single=0;SyncArray[2].velocity=20;
		SyncArray[3].angle=-45;SyncArray[3].interval_single=0;SyncArray[3].velocity=20;
		SyncArray[4].angle=-45;SyncArray[4].interval_single=0;SyncArray[4].velocity=20;
		//发送同步指令控制
		FSUS_SyncCommand(servo_usart,sync_count,servomode,SyncArray);
		SysTick_DelayMs(1000);
		//发送同步指令读取
		FSUS_SyncCommand(servo_usart,sync_count,7,SyncArray);
		SysTick_DelayMs(200);
  }
}

```

---

## 10. 异步指令(暂存与延后触发)

异步指令允许主机像“备忘录”一样提前将运动命令写进舵机的内部寄存器缓存中（舵机暂时不予理睬）；

直到主机认为时机成熟并向总线下发“异步执行”的使能命令，舵机才会立刻开始执行内存中的动作。特别适合构建复杂的分布式触发网络。

**异步写入（开启异步指令暂存模式）**

**函数原型**

```c
FSUS_STATUS FSUS_BeginAsync(
    Usart_DataTypeDef *usart
);
```

* **参数说明**
  * `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。

**函数调用示例**

```c
FSUS_BeginAsync(servo_usart); // 通知底层：后续指令不要立刻跑，先缓存起来
```

**异步执行（终结异步并执行/抛弃）**

**函数原型**

```c
FSUS_STATUS FSUS_EndAsync(
    Usart_DataTypeDef *usart,
    uint8_t mode
);
```

**参数说明**
* `mode`：终端逻辑触发标志。`0` 表示批准执行刚暂存的动作；`1` 表示作废并清空刚暂存的动作。

**函数调用示例**

```c
uint8_t async_mode=0; //0:执行存储的命令  1:取消存储的命令
FSUS_EndAsync(servo_usart,async_mode);
```

<a id="quick-async-delay"></a>
### ▶️ 异步命令延时触发
**逻辑说明：** 

- 演示了打开系统异步开关后下发角度指令（此刻设备保持静止），
- 通过 MCU 主动休眠阻塞延时 5 秒后，才下发确认执行的 End 命令唤醒底层硬件。

**完整示例代码：**

```c
/********************************************************
 * 存储一次命令，在下次发送命令的时候才执行 
 ********************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)    <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx)   <----> 总线伺服舵机转接板 Tx
// STM32F103 GND        <----> 总线伺服舵机转接板 GND
// STM32F103 V5         <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
Usart_DataTypeDef* servo_usart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
Usart_DataTypeDef* logging_usart = &usart2;



// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
    while((logging_usart->pUSARTx->SR&0X40)==0){}
    /* 发送一个字节数据到串口 */
    USART_SendData(logging_usart->pUSARTx, (uint8_t) ch);
    /* 等待发送完毕 */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}


#define ID 0 // 舵机的ID号
float angle;           //舵机角度设置
float angle_read;			 // 读取的角度
uint16_t power = 1000; // 舵机执行功率 单位mV 默认为0
uint16_t interval = 0; // 舵机旋转的周期

uint8_t async_mode=0; //0:执行存储的命令  1:取消存储的命令

int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();

    while (1){
			
    //异步写入
		FSUS_BeginAsync(servo_usart);
	
		printf("GOTO: 135.0f\r\n");
    // 简易角度控制 + 当前角度查询
    angle = 135.0;
    interval = 2000;
    FSUS_SetServoAngle(servo_usart, ID, angle, interval, power);
    FSUS_QueryServoAngle(servo_usart, ID, &angle_read);
    printf("Cur Angle: %.1f\r\n", angle_read);
		
		printf("*******************\n");
		
	//第一次发送上面的命令是不会动的，只是存储了命令
	//等待5秒
		SysTick_DelayMs(5000);
		
		//异步执行
		FSUS_EndAsync(servo_usart,async_mode);
  }
}
```

---

## 11. 数据监控（批量读取）

相比于逐一读取各项物理参数，系统提供了 `FSUS_ServoMonitor` 函数，它能一次性将舵机的全套状态数据装载到一个结构体中，大幅度缩短总线通信占用时间。

**函数原型**

```c
FSUS_STATUS FSUS_ServoMonitor(
    Usart_DataTypeDef *usart,
    uint8_t servo_id,
    ServoData servodata[]
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。
* `servoId`：目标舵机的 ID。

* `servodata[]`：用于存放舵机完整状态数据的接收结构体对象指针。

  数据包括：

**函数调用示例**

```c
//要读取的舵机id号
uint8_t servoId = 0; 
//舵机的存储数据结构体
ServoData servodata_single[1];
// 读取舵机数据函数
FSUS_ServoMonitor(servo_usart,servo_id,servodata_single);
```

<a id="quick-monitor-full"></a>
### ▶️ 舵机传感器数据全监控

**逻辑说明：** 

- 初始化舵机后，周期性地向底层发起 Monitor 请求，随后通过访问 `servodata_single` 的成员变量（如 `voltage`, `current`, `power`, `temperature`, `angle`），将实时硬件状况格式化输出至 UART2 调试口。

**完整示例代码：**

```c
/********************************************************
 * 测试舵机的数据回读，并通过串口打印全部数据
 ********************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)    <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx)   <----> 总线伺服舵机转接板 Tx
// STM32F103 GND        <----> 总线伺服舵机转接板 GND
// STM32F103 V5         <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
Usart_DataTypeDef* servo_usart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
Usart_DataTypeDef* logging_usart = &usart2;



// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
    while((logging_usart->pUSARTx->SR&0X40)==0){}
    /* 发送一个字节数据到串口 */
    USART_SendData(logging_usart->pUSARTx, (uint8_t) ch);
    /* 等待发送完毕 */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}

/*数据监控的数据
* id：舵机的id号
* voltage：舵机的电压
* current：舵机的电流
* power：舵机的执行功率
* temperature：舵机的温度 
* status：舵机的状态
* angle：舵机的角度
* circle_count：舵机的转动圈数
*/
ServoData servodata_single[1];//读取一个舵机数据的结构体

//要读取的舵机id号
uint8_t servo_id=0;

int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();
    while (1){
        	//每1秒读取一次
			FSUS_DampingMode(servo_usart,servo_id,500);
			FSUS_ServoMonitor(servo_usart,servo_id,servodata_single);
			printf("read ID: %d\r\n", servodata_single[0].id);
			printf("read sucess, voltage: %d mV\r\n", servodata_single[0].voltage);
			printf("read sucess, current: %d mA\r\n", servodata_single[0].current);
			printf("read sucess, power: %d mW\r\n", servodata_single[0].power);
			printf("read sucess, temperature: %d \r\n", servodata_single[0].temperature);
			if ((servodata_single[0].status >> 3) & 0x01)
			printf("read sucess, voltage too high\r\n");
			if ((servodata_single[0].status >> 4) & 0x01)
			printf("read sucess, voltage too low\r\n");
			printf("read sucess, angle: %f\r\n", servodata_single[0].angle);
			printf("read sucess, circle_count: %d\r\n",servodata_single[0].circle_count);
			SysTick_DelayMs(1000);
			
  }
}

```

---

## 12. 原点设置

> [!NOTE]
> 在触发原点重置前，必须先发送 **停止指令-失锁卸力** 指令，确保舵机处于自由状态。

**函数原型**

```C
FSUS_STATUS FSUS_SetOriginPoint(
    Usart_DataTypeDef *usart,
    uint8_t servo_id
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。
* `servo_id`：目标舵机 ID。

**函数调用示例**

```C
uint8_t servoId = 0;    // 舵机的ID号
FSUS_SetOriginPoint(servoUsart, servoId); // 将当前物理结构位置重新映射为固件级 0 度
```

---

## 13. 舵机自定义配置参数读写

在特定场合，您可能只需要读取或修改舵机内存表中的某一个特定硬件寄存器地址（如读取电压、保护值等）。


**函数原型**

```c
// 读取数据
FSUS_STATUS FSUS_ReadData(
    Usart_DataTypeDef *usart,
    uint8_t servoId,
    uint8_t address,
    uint8_t *value,
    uint8_t *size
);
```

**参数说明**

* `usart`：舵机控制对应的串口数据对象`Usart_DataTypeDef`。
* `servo_id`：目标舵机 ID。

* `address`：被查询参数位于舵机内部内存表的起始地址编号（详见附录表格）。
* `value`：用于存放读回数据的接收缓冲指针。
* `size`：返回该地址有效数据实际的字节长度 (1, 2, 或 4 字节)。

**函数调用示例**

```c
uint8_t servoId = 0;  		// 连接在转接板上的总线伺服舵机ID号
uint8_t value;
uint8_t dataSize;

statusCode = FSUS_ReadData(servoUsart, servoId, FSUS_PARAM_SERVO_STATUS, (uint8_t *)&value, &dataSize);

if (statusCode == FSUS_STATUS_SUCCESS)
{
    // 舵机工作状态标志位
    // BIT[0] - 执行指令置1，执行完成后清零。
    // BIT[1] - 执行指令错误置1，在下次正确执行后清零。
    // BIT[2] - 堵转错误置1，解除堵转后清零。
    // BIT[3] - 电压过高置1，电压恢复正常后清零。
    // BIT[4] - 电压过低置1，电压恢复正常后清零。
    // BIT[5] - 电流错误置1，电流恢复正常后清零。
    // BIT[6] - 功率错误置1，功率恢复正常后清零。
    // BIT[7] - 温度错误置1，温度恢复正常后清零。

    if ((value >> 3) & 0x01)
        printf("read sucess, voltage too high\r\n");
    if ((value >> 4) & 0x01)
        printf("read sucess, voltage too low\r\n");
}
```

**参数写入**

> [!WARNING]
> - 修改 ID 号、波特率等关键非易失性参数，**强烈建议通过 Windows 上位机可视化软件完成**。
> - 仅在必要情况下使用本 API 做运行期代码级修改，修改错误可能导致设备异常。

**函数原型**

```c
// 写入数据
FSUS_STATUS FSUS_WriteData(
    Usart_DataTypeDef *usart,
    uint8_t servoId,
    uint8_t address,
    uint8_t *value,
    uint8_t size
);
```

**函数调用示例**

```c
uint8_t servoId = 0;  		// 连接在转接板上的总线伺服舵机ID号
float angleLimitLow = -90.0; 	// 舵机角度下限设定值
value = (int16_t)(angleLimitLow*10); // 舵机角度下限 转换单位为0.1度
statusCode = FSUS_WriteData(servoUsart, servoId, FSUS_PARAM_ANGLE_LIMIT_LOW, (uint8_t *)&value, 2);
```

<a id="quick-read-params"></a>
### ▶️ 读取舵机参数

**逻辑说明：** 

- 展示了如何使用底层通信层 `FSUS_ReadData` 函数。
- 代码演示了电压、电流、功率及温度ADC值的读取，并对 温度ADC 值转换为摄氏度的底层数学计算公式，以及通过位运算解析 8 位的 `status` 状态寄存器标志位。

    // 舵机工作状态标志位
    // BIT[0] - 执行指令置1，执行完成后清零。
    // BIT[1] - 执行指令错误置1，在下次正确执行后清零。
    // BIT[2] - 堵转保护置1，解除堵转后清零。
    // BIT[3] - 电压过高置1，电压恢复正常后清零。
    // BIT[4] - 电压过低置1，电压恢复正常后清零。
    // BIT[5] - 电流保护置1，电流恢复正常后清零。
    // BIT[6] - 功率保护置1，功率恢复正常后清零。
    // BIT[7] - 温度保护置1，温度恢复正常后清零。

**完整示例代码：**

```c
/***************************************************
* 读取舵机参数
 ***************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"
#include "math.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)  <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx) <----> 总线伺服舵机转接板 Tx
// STM32F103 GND 	  <----> 总线伺服舵机转接板 GND
// STM32F103 V5 	  <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
// 设置完成之后, 将下行取消注释
Usart_DataTypeDef *servoUsart = &usart1;

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND 	 <----> USB转TTL GND
// STM32F103 V5 	 <----> USB转TTL 5V (可选)
// <注意事项>
// 使用前确保已设置usart.h里面的USART2_ENABLE为1
Usart_DataTypeDef *loggingUsart = &usart2;

// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
	while ((loggingUsart->pUSARTx->SR & 0X40) == 0)
	{
	}
	/* 发送一个字节数据到串口 */
	USART_SendData(loggingUsart->pUSARTx, (uint8_t)ch);
	/* 等待发送完毕 */
	// while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);
	return (ch);
}

uint8_t servoId = 0;	// 连接在转接板上的总线伺服舵机ID号
FSUS_STATUS statusCode; // 状态码

int main(void)
{
	// 嘀嗒定时器初始化
	SysTick_Init();
	// 串口初始化
	Usart_Init();

	// 读取用户自定义数据
	// 数据表里面的数据字节长度一般为1个字节/2个字节/4个字节
	// 查阅通信协议可知,舵机角度上限的数据类型是有符号短整型(UShort, 对应STM32里面的int16_t),长度为2个字节
	// 所以这里设置value的数据类型为int16_t
	int16_t value;
	uint8_t dataSize;
	// 传参数的时候, 要将value的指针强行转换为uint8_t

	// 读取电压
	statusCode = FSUS_ReadData(servoUsart, servoId, FSUS_PARAM_VOLTAGE, (uint8_t *)&value, &dataSize);
	
	printf("read ID: %d\r\n", servoId);

	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		printf("read sucess, voltage: %d mV\r\n", value);
	}
	else
	{
		printf("fail\r\n");
	}

	// 读取电流
	statusCode = FSUS_ReadData(servoUsart, servoId, FSUS_PARAM_CURRENT, (uint8_t *)&value, &dataSize);
	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		printf("read sucess, current: %d mA\r\n", value);
	}
	else
	{
		printf("fail\r\n");
	}

	// 读取功率
	statusCode = FSUS_ReadData(servoUsart, servoId, FSUS_PARAM_POWER, (uint8_t *)&value, &dataSize);
	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		printf("read sucess, power: %d mW\r\n", value);
	}
	else
	{
		printf("fail\r\n");
	}
	// 读取温度
	statusCode = FSUS_ReadData(servoUsart, servoId, FSUS_PARAM_TEMPRATURE, (uint8_t *)&value, &dataSize);
	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		double temperature, temp;
		temp = (double)value;
		temperature = 1 / (log(temp / (4096.0f - temp)) / 3435.0f + 1 / (273.15 + 25)) - 273.15;
		printf("read sucess, temperature: %f\r\n", temperature);
	}
	else
	{
		printf("fail\r\n");
	}	
	// 读取工作状态
	statusCode = FSUS_ReadData(servoUsart, servoId, FSUS_PARAM_SERVO_STATUS, (uint8_t *)&value, &dataSize);
	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		// 舵机工作状态标志位
		// BIT[0] - 执行指令置1，执行完成后清零。
		// BIT[1] - 执行指令错误置1，在下次正确执行后清零。
		// BIT[2] - 堵转保护置1，解除堵转后清零。
		// BIT[3] - 电压过高置1，电压恢复正常后清零。
		// BIT[4] - 电压过低置1，电压恢复正常后清零。
		// BIT[5] - 电流保护置1，电流恢复正常后清零。
		// BIT[6] - 功率保护置1，功率恢复正常后清零。
		// BIT[7] - 温度保护置1，温度恢复正常后清零。

		if ((value >> 3) & 0x01)
			printf("read sucess, voltage too high\r\n");
		if ((value >> 4) & 0x01)
			printf("read sucess, voltage too low\r\n");
	}
	else
	{
		printf("fail\r\n");
	}
	printf("================================= \r\n");
	// 死循环
	while (1)
		;
}

```

**终端输出日志参考**

```C
read ID: 0                                      //舵机id
read success, voltage: 8905 mv                 //当前电压
read success, current: 0 ma                    //当前电流
read success, power: 0 mw                      //当前功率
read success, temperature: 32.240993           //当前温度
read success, voltage too high                 //如果当前电压超过舵机参数设置的舵机高压保护值，可以读到标志位
=================================
```




<h3 align="center"><span style="color:#007ACC;">=== 第三篇：附录速查表 ===</span></h3>
---


## 附表1：只读参数表

配合 `FSUS_ReadData` 函数的 `address` 参数使用。

| Address | 参数名称   | 数据类型 | 单位 | 备注                                                         |
| :-----: | :--------- | :------: | :--: | :----------------------------------------------------------- |
|    1    | 电压       | uint16_t |  mV  |                                                              |
|    2    | 电流       | uint16_t |  mA  |                                                              |
|    3    | 功率       | uint16_t |  mW  |                                                              |
|    4    | 温度       | uint16_t | ADC  | 请参考[ADC–温度映射表]                                       |
|    5    | 状态标志位 | uint8_t  |      | BIT[0] - 指令执行中置1, 执行完毕后清零<BR>BIT[1] - 指令执行错误置1, 下次正确执行后清零<BR>BIT[2] - 堵转保护置1, 堵转解除后清零<BR>BIT[3] - 高压保护置1, 电压正常后清零<BR>BIT[4] - 低压保护置1, 电压正常后清零<BR>BIT[5] - 过流保护置1, 电流正常后清零<BR>BIT[6] - 功率保护置1, 功率正常后清零<BR>BIT[7] - 温度保护置1, 温度正常后清零 |



## 附表2：自定义参数表

配合 `FSUS_WriteData` 和 `FSUS_ReadData` 使用。

| Address | 参数名称         | 数据类型 | 单位 | 备注                                                         |
| :-----: | :--------------- | :------: | :--: | :----------------------------------------------------------- |
|   33    | 指令响应开关     | uint8_t  |      | **0x00：** 不发送响应封包 (**默认**) <BR>**0x01：** 发送响应封包 |
|   34    | 舵机 ID          | uint8_t  |      | 范围 0 ~ 254                                                 |
|   36    | 波特率配置       | uint8_t  |      | 0x01 - 9,600<BR>0x02 - 19,200<BR>0x03 - 38,400<BR>0x04 - 57,600<BR>**0x05 - 115,200 (默认) **<BR>0x06 - 250,000<BR>0x07 - 500,000<BR>0x08 - 1,000,000 |
|   37    | 堵转保护开关     | uint8_t  |      | 当舵机运行超过`功率保护值`的时候 <BR>**0x00：** (堵转保护-关)，降低至功率保护值运行 (**默认**) <BR>**0x01：** (堵转保护-开)，舵机释放锁力 |
|   38    | 堵转功率上限     | uint16_t |  mW  |                                                              |
|   39    | 电压保护下限     | uint16_t |  mV  |                                                              |
|   40    | 电压保护上限     | uint16_t |  mV  |                                                              |
|   41    | 温度保护值       | uint16_t | ADC  |                                                              |
|   42    | 功率保护值       | uint16_t |  mW  |                                                              |
|   43    | 电流保护值       | uint16_t |  mA  |                                                              |
|   46    | 舵机上电锁力开关 | uint8_t  |      | **0x00：** 释放锁力 (**默认**) **0x01：** 维持锁力           |
|   48    | 角度限制开关     | uint8_t  |      | **0x00：** 关闭 (**默认**) **0x01：** 开启                   |
|   49    | 上电缓启动开关   | uint8_t  |      | **0x00：** 关闭 (**默认**) **0x01：** 开启                   |
|   50    | 上电缓启动时间   | uint16_t |  ms  |                                                              |
|   51    | 舵机角度上限     | int16_t  | 0.1° |                                                              |
|   52    | 舵机角度下限     | int16_t  | 0.1° |                                                              |

## 附表3：NTC 热敏电阻 ADC 温度值映射转换表

通过 `address=4` 读取出来的原始数据为 ADC 数字量，需代入对数函数转换为摄氏度，下表提供了核心运行区间内的常见对查表。

{{ fig_center("../images/ADC.png", "ADC温度对照表", "500px") }}

*(以下为高频使用的 50℃-79℃ 温度与 ADC 返回值对照快查映射表)*

| 实际温度(℃) | 原始 ADC | 实际温度(℃) | 原始 ADC | 实际温度(℃) | 原始 ADC |
| :---------: | :------: | :---------: | :------: | :---------: | :------: |
|   **50**    |   1191   |   **60**    |   941    |   **70**    |   741    |
|   **51**    |   1164   |   **61**    |   918    |   **71**    |   723    |
|   **52**    |   1137   |   **62**    |   897    |   **72**    |   706    |
|   **53**    |   1110   |   **63**    |   876    |   **73**    |   689    |
|   **54**    |   1085   |   **64**    |   855    |   **74**    |   673    |
|   **55**    |   1059   |   **65**    |   835    |   **75**    |   657    |
|   **56**    |   1034   |   **66**    |   815    |   **76**    |   642    |
|   **57**    |   1010   |   **67**    |   796    |   **77**    |   627    |
|   **58**    |   986    |   **68**    |   777    |   **78**    |   612    |
|   **59**    |   963    |   **69**    |   759    |   **79**    |   598    |
