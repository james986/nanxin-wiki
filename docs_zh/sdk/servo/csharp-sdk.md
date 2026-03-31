# 总线伺服舵机 SDK 使用手册（C#）

<!--一以下是SDK页面用的表格宏（适用协议/版本/GitHub链接/单个下载文件-->
{{ github_download_table("UART/RS-485 全系列", "v1.2026.0214", "https://github.com/servodevelop/servo-uart-rs485-sdk", "./data/csharp-sdk.zip", "28px") }}

## 1. 简介

### 1.1 命名空间

```c#
using BrightJade;

using BrightJade.Serial;

using FashionStar.Servo.Uart;

using FashionStar.Servo.Uart.Protocol;
```

### 1.2 定义与宣告

```c#
// Serial Port 管理器。
private SerialPortManager _serialPortManager;
// 舵机控制器。
private ServoController _servoController;

_serialPortManager = new SerialPortManager();
_servoController = new ServoController(_serialPortManager);
```

## 2. 代码撰写

 

### 2.1 Serial Port 管理器

#### 2.1.1 SerialSettings 物件

SerialPortManager包装并管理 SerialPort对象的收发行为，并有一型态为SerialSettings的成员CurrentSerialSettings，储存相关信息。

#### 2.1.2 初始化

SerialPortManager创建同时，会寻找目前装置所有可用的Serial Port，并将清单存于CurrentSerialSettings.PortNameCollection中。

其中第一个元素给予CurrentSerialSettings.PortName。同时根据选择的Baud，在CurrentSerialSettings.BaudRateCollection中更新可用Baud的清单。可以实作需求，自行调用。

其余参数正常状况下多维持初始值，若有需要请自行参考调用。

#### 2.1.3 参考范例

以下是初始化范例：

```c#
// Serial Port 管理器。
private SerialPortManager _serialPortManager;
// 舵机控制器。
private ServoController _servoController;

_serialPortManager = new SerialPortManager();
_servoController = new ServoController(_serialPortManager);

// 接收事件。
_servoController.ReadAngleResponsed += OnReadAngleResponsed;
_servoController.ReadMultiTurnAngleResponsed += OnReadMultiTurnAngleResponsed;
_serialPortManager.ErrorOccured += OnErrorOccured;
```

在某个按钮的Click事件

```c#
// 开始监听。
_servoController.StartListening();
```

在某个按钮的Click事件

```c#
// 读取角度，结果将回传至回呼 OnReadAngleResponsed。
_servoController.ReadAngle((byte)_numServoID.Value);
```

在某个按钮的Click事件

```c#
// 停止监听
_servoController.StopListening();
```



### 2.2 舵机控制器的方法与事件

舵机控制器的方法可视为Tx请求封包；事件可视为Rx响应封包。

{{ fig_indent_adjustable("../images/csharp-sdk/loH6cnFrQwxYGyT.png","image-20210521162314143", "100%", "3.5em") }}

请参考文件：[标准协议舵机通讯封包定义表](https://fashionrobo.com/wp-content/uploads//download/uart-servo-protocol-SC-20210121.pdf)，呼叫与封包命名同名的方法作为请求，接收命名后缀Responsed的事件，作为舵机信息响应。

例如：上图ReadAngle封包，呼叫ServoController对象的ReadAngle()方法，即可向舵机询问角度。

```c#
_servoController.ReadAngle((byte)_numServoID.Value);
```

接收ReadAngleResponsed事件，以处理回传的角度数值。



### 2.3 多线程处理

舵机控制器的事件，与UI的线程不同，必须额外处理，如下所示：

{{ fig_indent_adjustable("https://i.loli.net/2021/05/21/u8OJXHSt64RLAde.png","image-20210521162314143", "100%", "3.5em") }}
