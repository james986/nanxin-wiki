# Atom S 快速开始（10 自由度双足机器人）

{{ fig_indent_adjustable("../images/atom-s-primary.webp","Atom S","100%","3.5em") }}

## 1. 产品简介

### 1.1 项目定位

**项目名称**：Fashion Star Atom S 10-DOF Open Source Robot Kit

Atom S 是一款完全开源的 10 自由度（DOF）人形机器人套件，面向机器人开发者、创客及教育机构，提供一个低成本、高扩展性的硬件平台。整机采用 10 颗 Fashion Star RA8-U25H-M 总线伺服舵机作为核心动力系统，并配合高度集成的电子架构，为后续的二次开发、动作设计和功能扩展预留了充足空间。

### 1.2 核心特性

- **自由度配置**：整机 10 DOF，覆盖头部、手臂及腿部关节。
- **关节执行器**：Fashion Star RA8-U25H-M 总线伺服舵机 × 10，支持总线通讯，布线简洁。
- **结构与外观**：采用全 3D 打印结构，官方开源 STP / STL 模型文件，便于部件替换、结构强化与外观再设计。
- **Web 可视化动作编辑器**：提供免安装网页端控制平台，支持实时舵机调试与示教模式编程。动作组可导出为标准 `.json` 文件，便于 Arduino、STM32、树莓派等主控平台解析与集成。
- **开箱即用**：标配 Seeed Studio XIAO ESP32S3 与 Grove 扩展板，出厂已预置完整控制固件，完成组装后可直接通过 Web 端遥控进行快速验证。
- **生态扩展能力**：借助 Seeed Studio XIAO 扩展板上的 Grove 接口，可快速接入视觉、环境感知等 Grove 生态传感器与控制模块。
- **跨平台兼容性设计**：标配 RUC-01 驱动转接板，提供 5V / 3.3V 稳压输出与通用 UART 通讯接口，方便外接 Raspberry Pi、STM32、Arduino、ESP32 或 PC 平台。

### 1.3 规格参数

| 项目 | 参数 |
| --- | --- |
| 自由度（DOF） | 10 |
| 机身 | 3D 打印，结构数据开源 |
| 舵机 | 标配 RA8-U25H-M 总线伺服舵机；孔位兼容，支持升级至 RP8-U45H-M / RX8-U40H-M |
| 舵机电源接口板 | RUC-01（提供 4 路总线接口、5V / 3.3V 逻辑供电、UART / Grove 通讯接口） |
| 标配主控 | Seeed Studio XIAO ESP32S3 + Seeed Studio XIAO 扩展板 |
| 通讯协议 | 异步串行通讯（UART） |
| 兼容控制器 | Raspberry Pi、STM32、Arduino、ESP32、PC（需配套 USB 转 TTL 模块） |
| 尺寸 | 154 × 105 × 283 mm |

{{ fig_indent_adjustable("../images/atom-s-quick-start-01-dimensions.png","Atom S 外观尺寸","100%","3.5em") }}

## 2. 开箱即用（快速上手指南）

> [!TIP]
> Atom S 出厂时已烧录基础控制程序并完成初始装配。只要准备好电源和一台智能手机，即可快速体验机器人的动作与遥控功能。

### 2.1 硬件供电准备

由于物流限制，套件出厂默认不含电池。开始体验前，请准备一块兼容电池，并接入机器人背部电源接口：

- **电池规格**：3S 12.6V 航模锂电池
- **电池接口类型**：T 插（T-Plug）
- **上电确认**：接通电源后，主控板（XIAO ESP32S3）上的指示灯会亮起，表示系统已启动

### 2.2 Web 端遥控器连接

请使用智能手机或具备蓝牙功能的 PC 终端开启蓝牙，并根据操作系统选择合适的浏览器。由于 Web 遥控依赖底层 `Web Bluetooth API`，浏览器兼容性非常关键：

- **PC 端（Windows / macOS）**：请使用 Google Chrome 或 Microsoft Edge
- **Android 端**：请使用 Google Chrome，不要使用系统自带浏览器或微信扫码打开
- **iOS 端**：Safari、Chrome 和 Edge 均不支持网页蓝牙功能，请前往 App Store 下载支持 WebBLE 协议的第三方浏览器，例如 Bluefy
- **访问地址**：`https://wiki.fashionrobo.com/ps2v2/`

### 2.3 蓝牙配对与初始化

1. 打开 Web 遥控页面后，点击界面上方的 **SYSTEM LINK** 按钮。
2. 在弹出的蓝牙设备列表中，选择名为 **ESP32_Pro_Remote** 的设备并点击配对。

{{ fig_indent_adjustable("../images/atom-s-quick-start-02-device-pairing.png","蓝牙配对设备列表","50%","3.5em") }}

3. 配对成功后，网页会显示“已连接状态”。
4. 此时机器人会自动执行一次“鞠躬”动作，并恢复到默认站立姿态，说明系统已经准备就绪。

{{ fig_indent_adjustable("../images/atom-s-quick-start-03-linked-status.png","连接成功状态","50%","3.5em") }}

### 2.4 开始你的第一次“连续动作”示教

通过 Web 虚拟手柄，即使不编写代码，也可以快速教机器人完成一段连续动作：

{{ fig_indent_adjustable("../images/atom-s-quick-start-04-web-remote-layout.png","Web 端遥控按键布局","100%","3.5em") }}

- **环境准备**：点击左上角的 **HOME** 键，确保机器人处于标准初始站立姿态。
- **解锁关节**：点击左上角的 **RELAX** 键，使机器人进入阻尼模式。此时所有伺服舵机卸力，可以手动摆动各个关节。
- **记录第一帧姿态**：手动摆好第一个姿态后，点击方向键 **左 ◀**，记录当前姿势。
- **记录后续动作帧**：继续改变机器人姿态，再次点击 **左 ◀**。重复该操作，即可记录一连串动作帧，默认最高支持记录 100 帧。
- **连续播放动作序列**：全部姿态记录完成后，点击方向键 **右 ▶**，机器人会平滑回放刚才记录的所有动作。
- **调整运行速度**：如果回放过快或过慢，可点击 **上 ▲**（加速）或 **下 ▼**（减速）调整动作速度。
- **一键演示**：点击右侧 **方形键 □**，可直接播放出厂内置的默认演示动作。

> [!TIP]
> 如果你已经完成快速体验，并希望进一步导出动作 JSON、修改主控逻辑或接入其他控制器，请继续阅读后续章节。

## 3. 硬件架构与机械结构

### 3.1 驱动与电源管理（RUC-01 接口板）

RUC-01 接口板是整机的动力枢纽，负责总线通信管理与电源分配：

- **舵机通讯**：板载 4 路总线舵机接口，支持串联扩展，负责总线伺服舵机的信号与供电。
- **PC 调试接口**：集成 USB Type-C 接口，可直接连接 PC 上位机进行动作组编辑与调试。
- **系统供电**：负责电压转换，并为主控板提供稳定的电源输入。
- **通讯接口**：提供标准 UART 串口，用于接收上层主控板的控制指令。

### 3.2 逻辑主控与扩展（MCU + Grove Shield）

主控与扩展部分是机器人的“大脑”，负责运行控制算法与传感器数据处理：

- **核心主控**：采用 Seeed Studio XIAO 系列开发板，体积小巧，性能强大。
- **生态扩展**：配套 Grove 接口扩展板，引出丰富的通用接口。
- **主要功能**：运行机器人运动学程序，并通过 Grove 接口无缝连接各类传感器，实现更多交互功能。

### 3.3 通用通讯接口说明（跨平台开发必看）

虽然套件默认采用 XIAO ESP32S3 作为主控，但 RUC-01 接口板对所有外部控制器都是开放的。主控与 RUC-01 之间仅需 4 根线，即可完成基础通信：

- **5V / 3.3V**：RUC-01 可向主控反向提供稳定电源
- **GND**：共地端
- **RX / TX**：标准异步串行通讯（UART），用于收发控制指令与读取舵机反馈

### 3.4 数据流向说明

**调试 / 编辑模式（Debug Mode）**

```text
PC --(USB)--> RUC-01 --(总线)--> 舵机
```

说明：通过电脑端软件直接调节舵机角度并保存动作组，不经过主控板。

**自主运行模式（Autonomous Mode）**

```text
Web 遥控端 / 传感器 --(信号)--> ESP32 / 树莓派 / STM32 等主控
                       --(UART 指令)--> RUC-01 --(总线)--> 舵机
```

说明：主控根据传感器反馈或预存代码，自主控制机器人行动。

{{ fig_indent_adjustable("../images/atom-s-quick-start-05-hardware-architecture.png","RUC-01 与主控板接口说明","50%","3.5em") }}

| 编号 | 接口说明 | 编号 | 接口说明 |
| --- | --- | --- | --- |
| ① | 整机电源开关 | ⑤ | 转接板通讯 UART / Grove 接口（连接主控 ⑧） |
| ② | 电源输入接口 | ⑥ | 主控 ESP32S3 Type-C 数据接口（程序下载） |
| ③ | 舵机接口 × 4 | ⑦ | Seeed XIAO ESP32S3 主控板 |
| ④ | Type-C 数据接口（舵机调试，连接 PC） | ⑧ | 主控板通讯 UART / Grove 接口（连接 RUC-01 接口板 ⑤） |

> [!WARNING]
> RUC-01 接口板 ④ 号 Type-C 接口附近的拨动开关，以及图示左侧的两个 Type-C 接口均为预留或作他用，本项目中无需使用，请避免误操作。

### 3.5 机械结构与关节寻址

为确保底层代码能够准确驱动对应的物理关节，系统对全身 10 个自由度进行了明确的 ID 寻址与零位姿态标定。

**结构分布与舵机 ID 映射**

整机 10 颗伺服舵机共享同一条控制总线，因此每颗舵机都拥有唯一的数字 ID（0~9）。

> [!TIP]
> 后续在使用动作编辑器或编写 JSON 动作数据时，数据中的 `id` 字段必须与下图中的物理关节位置严格一一对应，否则会导致动作错乱。

{{ fig_indent_adjustable("../images/atom-s-quick-start-06-servo-id-mapping.png","结构展示与默认 ID","100%","3.5em") }}

**标定零度姿态**

零度姿态是机器人运动学解算的基础基准位。当主控下发全机 0 度指令，或用户点击 Web 控制台的 **HOME** 复位键时，机器人应呈现下图所示的标定站立姿态。

> [!TIP]
> 受 3D 打印件装配公差影响，整机装配后可能存在轻微姿态偏斜。请在确认零度姿态后，前往底层源码中的 `ROBOT_RESET_POSITION_0 ~ 9` 参数区进行软件级微调补偿。

{{ fig_indent_adjustable("../images/atom-s-quick-start-07-zero-pose.png","零度姿态","100%","3.5em") }}

## 4. 自定义动作开发核心工作流（Web 动作编辑器）

> [!NOTE]
> 动作编辑器的详细操作步骤，请参阅单独发布的《动作编辑器独立说明文档》：  
> [点击查看 Robot Studio 使用手册](../../software/humanoid/robot-studio-pro.md)

Web 版动作编辑器在线地址：`https://wiki.fashionrobo.com/uartbasic/robotstudiopro/`

为了让开发者更清楚地理解“如何让机器人执行自定义动作”，整套工作流可以概括为以下三个阶段：

### 4.1 姿态设计与数据导出（Web 动作编辑器）

1. **连接与读取**：通过 PC 浏览器连接 RUC-01 接口板，实时读取机器人舵机状态。
2. **解锁与示教**：将舵机一键卸力进入阻尼模式，手动摆动机器人并记录每一帧姿态。
3. **编排与微调**：调整各关键帧之间的执行时间与间隔，并在软件端实时回放以优化动作连贯性。
4. **导出 JSON**：确认动作无误后，将整套动作组导出为标准 `.json` 文件。

### 4.2 数据集成与固件烧录（ESP32 主控端）

1. **打开源码**：在 Arduino IDE 中打开配套的 ESP32 主控工程源码。
2. **替换代码**：将导出的 `.json` 数据完整复制，替换 `Robot.ino` 文件中原有的 `jsonData` 变量内容。
3. **编译烧录**：重新编译工程，并将更新后的固件烧录至 ESP32S3 主控板中。

### 4.3 无线遥控与触发运行（Web 遥控终端）

1. **无线连接**：打开手机 Web 端遥控器 `https://wiki.fashionrobo.com/ps2v2/` 并与机器人配对。
2. **一键触发**：点击界面上的 **方形键 □**（指令 `0x10`），机器人即可脱离数据线，自主且连贯地执行刚刚设计的动作序列。

## 5. 标配主控固件烧录指南（基于 Seeed Studio XIAO ESP32S3）

> [!TIP]
> 本节仅适用于标配 XIAO ESP32S3 主控环境。若你的项目使用 STM32 或 Raspberry Pi，请直接参考附录中的多平台 Fashionstar 舵机控制 SDK。

### 5.1 开发环境搭建（Arduino IDE）

前往 Arduino 官网下载并安装最新版 Arduino IDE，推荐使用 Arduino IDE 2.x 版本。

### 5.2 导入 ESP32 硬件支持包

请先打开 Arduino IDE 的首选项设置：

- **Windows**：`File > Preferences`
- **macOS**：`Arduino IDE > Settings...` 或 `Preferences...`

在“附加开发板管理器网址（Additional Boards Manager URLs）”中填入以下链接：

```text
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```

{{ fig_indent_adjustable("../images/atom-s-quick-start-08-arduino-preferences.png","Arduino IDE 首选项设置","100%","3.5em") }}

### 5.3 部署 ESP32 编译环境（严格版本要求）

1. 打开 `Tools > Board > Boards Manager`
2. 搜索 `esp32`
3. 找到由 `Espressif Systems` 提供的安装包
4. 手动指定安装 **3.3.5** 版本

> [!WARNING]
> 请不要直接安装最新版本。当前工程依赖的蓝牙与总线驱动组合要求使用 **3.3.5** 版本，否则可能导致蓝牙或总线通讯编译失败，或运行异常。

{{ fig_indent_adjustable("../images/atom-s-quick-start-09-esp32-board-manager.png","ESP32 开发板管理器版本选择","100%","3.5em") }}

### 5.4 安装功能依赖库（ArduinoJson 与 ArduinoBLE）

系统依赖以下第三方库实现 JSON 解析与蓝牙服务：

- `ArduinoJson`
- `ArduinoBLE`

安装方法：

1. 打开 `Sketch > Include Library > Manage Libraries...`
2. 搜索并安装 `ArduinoJson`
3. 搜索并安装 `ArduinoBLE`

{{ fig_indent_adjustable("../images/atom-s-quick-start-10-arduinojson-library.png","安装 ArduinoJson 库","50%","3.5em") }}

{{ fig_indent_adjustable("../images/atom-s-quick-start-11-arduinoble-library.png","安装 ArduinoBLE 库","50%","3.5em") }}

### 5.5 部署 Fashion Star Servo 核心驱动 SDK

为保证底层驱动正常调用，需要手动安装官方 SDK：

1. 从配套资料包中找到 `fashionstar-uart-servo-arduino-sdk-V2.rar`
2. 解压缩该文件
3. 将整个 SDK 文件夹复制到 Arduino 默认库目录下

默认库路径：

- **Windows**：`C:\Users\用户名\Documents\Arduino\libraries`
- **macOS**：`~/Documents/Arduino/libraries`

复制完成后，请彻底关闭并重新打开 Arduino IDE，使其重新加载本地库。

### 5.6 选择开发板与编译烧录

1. 使用 Type-C 数据线将 XIAO ESP32S3 连接到电脑
2. 打开 `Tools > Board > esp32`，选择 `XIAO_ESP32S3`
3. 打开 `Tools > Port`，选择主控板对应端口

端口命名通常表现为：

- **Windows**：`COM3`、`COM5` 等
- **macOS**：`/dev/cu.usbmodem...` 或 `/dev/cu.usbserial...`

最后在 Arduino IDE 中打开项目源码（`.ino`），点击左上角 **Upload** 按钮，等待控制台显示“上传成功”即可。

## 6. 底层控制参数配置规范（基于标配主控 Seeed Studio XIAO ESP32S3）

在 Arduino IDE 中打开工程源码后，可按实际项目需求修改以下宏定义与常量。请确认参数所在文件，避免误改。

### 6.1 基础硬件参数（位于 `Control.h`）

- `BAUDRATE`：主控与 RUC-01 通讯的串口波特率
- `SERVO_NUM`：机器人舵机总数量

```cpp
/* 用户可修改机器人数据区域 */
/* define */
#define BAUDRATE                            115200  /* 波特率 */
#define SERVO_NUM                           10      /* 舵机的总个数 */
```

### 6.2 UART 物理引脚重映射（位于 `Robot.ino`）

- `TX_PIN / RX_PIN`：ESP32S3 与 RUC-01 转接板通讯所使用的串口引脚

```cpp
/* 串口1--GPIO D6=GPIO43 D7=GPIO44 */
#define TX_PIN 43
#define RX_PIN 44
```

### 6.3 Web 遥控蓝牙通讯参数（位于 `Robot.ino` 与 `Control.h`）

- `BLE_NAME`：蓝牙广播名称
- `SERVICE_UUID / CHARACTERISTIC_UUID`：Web 端遥控器与主控建立通讯所依赖的服务 UUID 与特征 UUID

```cpp
/* 设置蓝牙名称 */
BLE.setLocalName("ESP32_Pro_Remote");
```

```cpp
/* ESP32的服务UUID以及特征UUID */
#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"
```

### 6.4 示教模式参数说明（位于 `Control.h`）

- `MAX_ACTIONNUM`：示教模式允许记录的最大动作帧数量
- `Default_RobotRunSpeed_Demonstration`：默认运行速度
- `MIN / MAX_RobotRunSpeed_Demonstration`：速度调节上下限
- `Adjust_RobotRunSpeed_Step`：每次加减速度的步进值

```cpp
#define MAX_ACTIONNUM                       100     /* 最大示教动作组数量 */
#define Default_RobotRunSpeed_Demonstration 1000    /* “默认”的示教运行速度 */
#define MIN_RobotRunSpeed_Demonstration     5000    /* “最慢”的示教运行速度 */
#define MAX_RobotRunSpeed_Demonstration     500     /* “最快”的示教运行速度 */
#define Adjust_RobotRunSpeed_Step           200     /* 调节示教运行速度的步进值 */
```

### 6.5 按键数据及命令宏定义说明（位于 `Control.h`）

无线遥控通讯中，Web 遥控端会将按键状态打包为两个独立变量发送：

- `btn_Main`：主操作区按键
- `btn_border`：系统控制区按键

因此，部分十六进制指令可能在不同区域重复出现，但它们对应不同变量，不会冲突。

```cpp
/* 蓝牙遥控器命令--根据不同的命令自行更改功能需求--用户根据实际情况进行更改 */
/* 以下指令对应 btn_Main (映射图中的红色十六进制标注) */
#define RemoteControl_DefaultDemoAction     0x10    /* 默认演示动作指令 (方形键) */
#define RemoteControl_Exe                   0x08    /* 示教模式执行指令 (方向键 右) */
#define RemoteControl_Record                0x04    /* 记录动作帧指令 (方向键 左) */
#define RemoteControl_ReduceRunSpeed        0x02    /* 减少示教运行速度 (方向键 下) */
#define RemoteControl_AddRunSpeed           0x01    /* 增加示教运行速度 (方向键 上) */

/* 以下指令对应 btn_border (映射图中的黄色十六进制标注) */
#define RemoteControl_Damping               0x04    /* 阻尼/卸力模式指令 (RELAX 键) */
#define RemoteControl_Reset                 0x08    /* 机器人复位指令 (HOME 键) */
```

### 6.6 动作组数据挂载区（位于 `Robot.ino`）

将动作编辑器导出的 `.json` 数据复制到 `jsonData` 变量中，注意保留 `R"(` 和 `)";`：

```cpp
/* 默认表演动作 */
const char* jsonData = R"(
[
    // 请将动作编辑器导出的JSON数据完整覆盖粘贴到这里
    {"angles":[{"id":0,"angle":0},{"id":1,"angle":0} ... ],"time":2000,"delay":500}
]
)";
```

### 6.7 JSON 缓存分配大小（位于 `Control.cpp`）

如果动作序列过长，可能会导致运行时内存不足或 JSON 解析失败。此时可适当增大 `DynamicJsonDocument` 容量：

```cpp
/* 创建JSON文档对象，分配足够的空间 */
DynamicJsonDocument doc(4096);
```

必要时可根据动作复杂度调大至 `8192` 或更高。

### 6.8 机器人复位角度参数及零点补偿说明（位于 `Control.h`）

- `ROBOT_RESET_POSITION_0 ~ 9`：分别对应 0 号至 9 号舵机的零位初始角度

> [!TIP]
> 由于机械装配公差，每台机器人的绝对零位可能略有偏差。建议在机器人站立姿态验证后，对这些参数进行微调补偿。

```cpp
/* 机器人复位角度设置--用户根据实际情况进行更改 */
constexpr float ROBOT_RESET_POSITION_0 = 0;
constexpr float ROBOT_RESET_POSITION_1 = 0;
constexpr float ROBOT_RESET_POSITION_2 = 0;
constexpr float ROBOT_RESET_POSITION_3 = 0;
constexpr float ROBOT_RESET_POSITION_4 = 0;
constexpr float ROBOT_RESET_POSITION_5 = 0;
constexpr float ROBOT_RESET_POSITION_6 = 90;
constexpr float ROBOT_RESET_POSITION_7 = 0;
constexpr float ROBOT_RESET_POSITION_8 = -90;
constexpr float ROBOT_RESET_POSITION_9 = 0;
```

## 7. Web 端遥控终端功能字典与底层映射

> [!TIP]
> 关于浏览器兼容性和蓝牙配对基础步骤，请先参考本文档第 2 章。本章主要用于说明控制界面中的按键布局与底层十六进制映射关系，方便后续二次开发。

{{ fig_indent_adjustable("../images/atom-s-quick-start-12-remote-hex-mapping.png","Web 端遥控按键与十六进制映射","100%","3.5em") }}

### 7.1 系统控制区（对应代码变量：`btn_border`）

该区域主要位于界面顶部和两侧边缘，用于控制机器人的全局状态：

- **HOME**（`0x08`）：中断当前动作，使机器人恢复到默认标定站姿，并清空当前内存中的示教数据
- **RELAX**（`0x04`）：进入阻尼 / 卸力模式，释放全部舵机锁止力矩，便于手动示教
- **其他黄色标注按键**：如 `L1`、`L2`、`R1`、`R2`、`L3`、`R3` 等，在当前出厂 Demo 中默认未分配动作，可由开发者自行扩展

### 7.2 主操作区（对应代码变量：`btn_Main`）

主操作区包含方向键与右侧功能键，主要负责动作编排与执行：

- **方向键 左 ◀**（`0x04`）：记录当前动作帧
- **方向键 右 ▶**（`0x08`）：回放当前记录的动作序列
- **方向键 上 ▲**（`0x01`）：增加运行速度
- **方向键 下 ▼**（`0x02`）：降低运行速度
- **方形键 □**（`0x10`）：执行主控 Flash 中预存的 `jsonData` 默认动作
- **其他红色标注按键**：如 `△`、`○`、`×` 等，在当前固件中默认未定义，可在底层代码中自行映射

## 8. 常见工程故障排查

### 8.1 固件烧录无响应 / 假死状态

- **现象**：Arduino IDE 提示 `A fatal error occurred: Failed to connect`，或上传过程中卡死
- **修复方法**：
  1. 保持 USB 数据线连接
  2. 长按开发板上的 **BOOT** 键
  3. 点击 IDE 中的 **上传** 按钮
  4. 当控制台出现 `Connecting...` 或开始显示传输进度时，释放 **BOOT** 键

### 8.2 Web 终端无法枚举蓝牙设备

- **现象**：点击“寻找设备”后，蓝牙设备列表为空
- **排查方向**：
  1. 检查是否使用支持 `Web Bluetooth API` 的浏览器
  2. Windows 用户确认系统版本不低于 Win10（1703+）
  3. macOS 用户检查系统“隐私与安全性”设置，确认浏览器蓝牙权限已放行

### 8.3 关节无力 / 无法锁止

- **现象**：固件运行正常，通讯也已建立，但机器人无法有效支撑负载
- **排查方向**：
  1. 检查 3S 电池电量与放电能力是否充足
  2. 检查总线排线是否存在虚接、反接
  3. 若更换过舵机，确认全机 10 个舵机的 ID（0~9）是否与工程定义一致，避免 ID 冲突

## 附录与开发资源

- Fashionstar 官方技术 Wiki：`https://wiki.fashionstar.com.hk`
- Web 动作编辑器使用说明：[Robot Studio 使用手册](../../software/humanoid/robot-studio-pro.md)
- Web 端蓝牙遥控说明：[蓝牙遥控器使用说明](../../software/humanoid/bt-remote-control.md)
- 提供 STM32 / Python / ROS / C++ / Arduino 等多平台舵机控制 SDK
