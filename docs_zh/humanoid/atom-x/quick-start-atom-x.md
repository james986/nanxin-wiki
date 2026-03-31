# Fashionstar Atom X：17 自由度双足机器人

{{ fig_indent_adjustable("../images/image_1.png","Atom X 外观", "100%", "3.5em") }}

## 1. 简介

{{ fig_indent_adjustable("../images/image_2.png","简介配图 1", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_3.png","简介配图 2", "100%", "3.5em") }}

- **项目名称**：Fashionstar Atom X 17-DOF Open Source Robot Kit  
  {{ fig_indent_adjustable("../images/image_4.png","项目名称", "100%", "3.5em") }}
- **简介**：这是一个完全开源的 17 自由度人形机器人，旨在为机器人爱好者提供一个低成本、高可玩性的硬件平台。核心动力源自 17 颗 Fashionstar RA8-U25H-M 总线舵机，配合极简的电子架构，让你专注于运动算法的开发。  
  {{ fig_indent_adjustable("../images/image_5.png","简介", "100%", "3.5em") }}
- **机器人架构**：总线舵机 + RUC-01 转接板（供电/通信）+ Seeed Studio XIAO 主控（可选 Grove 扩展）+ 3D 打印结构件。  
  {{ fig_indent_adjustable("../images/image_6.png","机器人架构", "100%", "3.5em") }}
- **自由度配置**：整机 17 DOF，覆盖头部、手臂及腿部关节。  
  {{ fig_indent_adjustable("../images/image_7.png","自由度配置", "100%", "3.5em") }}
- **关节执行器**：Fashionstar RA8-U25H-M 总线伺服舵机 × 17（支持总线通讯，布线简洁）。  
  {{ fig_indent_adjustable("../images/image_8.png","关节执行器", "100%", "3.5em") }}
- **机器人骨架**：全 3D 打印结构，提供 STP/STL 文件下载，损坏可随时重新打印，也可根据需求重新设计外观。  
  {{ fig_indent_adjustable("../images/image_9.png","机器人骨架", "100%", "3.5em") }}
- **控制与接口**：USB Type-C（上位机调试）、UART 串口（主控通信）、总线舵机接口、Grove 扩展接口（可选）。  
  {{ fig_indent_adjustable("../images/image_10.png","控制与接口", "100%", "3.5em") }}
- **Web 可视化动作编辑器**：提供免安装的网页端控制平台，支持实时舵机调试与示教模式编程。编辑完成的动作组可导出为标准的 `.json` 格式文件，便于各类主控（如 Arduino、STM32、树莓派）解析与集成。  
  {{ fig_indent_adjustable("../images/image_11.png","Web 动作编辑器", "100%", "3.5em") }}
- **开箱即用**：默认适配 Seeed Studio XIAO 系列作为主控，提供出厂演示程序。  
  {{ fig_indent_adjustable("../images/image_12.png","开箱即用", "100%", "3.5em") }}
- **多模块扩展**：搭配 Seeed Studio XIAO 扩展板，板载 Grove 接口，可连接 Seeed Grove 系列传感器/控制器模块。  
  {{ fig_indent_adjustable("../images/image_13.png","多模块扩展", "100%", "3.5em") }}
- **跨平台兼容**：为了降低开发门槛，我们提供 RUC-01 转接板，板载 5V/3.3V 电源输出及 UART 接口，任何具备串口功能的控制器均可通讯。  
  {{ fig_indent_adjustable("../images/image_14.png","跨平台兼容", "100%", "3.5em") }}

> [!TIP]
>
> 👉 想跑 Python AI？接上 树莓派。  
> 👉 想做物联网控制？接上 ESP32。  
> 👉 想学底层控制？接上 STM32 或 Arduino。

{{ fig_indent_adjustable("../images/image_15.png","扩展建议 1", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_16.png","扩展建议 2", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_17.png","扩展建议 3", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_18.png","扩展建议 4", "100%", "3.5em") }}

## 2. 硬件架构说明

{{ fig_indent_adjustable("../images/image_19.png","硬件架构配图 1", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_20.png","硬件架构配图 2", "100%", "3.5em") }}

### 2.1 驱动与电源管理（RUC-01 接口板）

驱动与电源管理（RUC-01 接口板）作为机器人的动力枢纽，该模块负责总线通信管理与电源分配：

- **舵机通讯**：板载 4 路总线舵机接口（支持串联扩展），负责 17 颗总线伺服舵机的信号和电源。  
  {{ fig_indent_adjustable("../images/image_21.png","舵机通讯", "100%", "3.5em") }}
- **PC 调试接口**：集成 USB Type-C 接口，可直接连接 PC 上位机进行动作组编辑与调试。  
  {{ fig_indent_adjustable("../images/image_22.png","PC 调试接口", "100%", "3.5em") }}
- **系统供电**：负责电压转换，并为主控板提供稳定的电源输入。  
  {{ fig_indent_adjustable("../images/image_23.png","系统供电", "100%", "3.5em") }}
- **通讯接口**：提供标准 UART 串口，用于接收上层主控板的控制指令。  
  {{ fig_indent_adjustable("../images/image_24.png","通讯接口", "100%", "3.5em") }}

### 2.2 逻辑主控与扩展（MCU + Grove Shield）

逻辑主控与扩展（MCU + Grove Shield）作为机器人的“大脑”，负责运行控制算法及处理传感器数据：

- **核心主控**：采用 Seeed Studio XIAO 系列开发板，体积小巧，性能强大。  
  {{ fig_indent_adjustable("../images/image_26.png","核心主控", "100%", "3.5em") }}
- **生态扩展**：配套 Grove 接口扩展板，引出丰富的通用接口。  
  {{ fig_indent_adjustable("../images/image_27.png","生态扩展", "100%", "3.5em") }}
- **主要功能**：运行机器人运动学程序，并通过 Grove 接口无缝连接各类传感器（如超声波、视觉、语音模块等），实现复杂的交互功能。  
  {{ fig_indent_adjustable("../images/image_28.png","主要功能", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_25.png","逻辑主控与扩展", "100%", "3.5em") }}

### 2.3 数据流向说明

{{ fig_indent_adjustable("../images/image_29.png","数据流向说明", "100%", "3.5em") }}

**调试/编辑模式（Debug Mode）**

{{ fig_indent_adjustable("../images/image_30.png","Debug Mode", "100%", "3.5em") }}

```
PC --(USB)--> RUC-01 --(总线)--> 舵机
```

{{ fig_indent_adjustable("../images/image_31.png","Debug Mode 流程", "100%", "3.5em") }}

说明：直接通过电脑软件调节舵机角度、保存动作组，不经过 XIAO 主控。  
{{ fig_indent_adjustable("../images/image_32.png","Debug Mode 说明", "100%", "3.5em") }}

**自主运行模式（Autonomous Mode）**

{{ fig_indent_adjustable("../images/image_33.png","Autonomous Mode", "100%", "3.5em") }}

```
传感器/遥控器 --(信号)--> XIAO --(UART 指令)--> RUC-01 --(总线)--> 舵机
```

{{ fig_indent_adjustable("../images/image_34.png","Autonomous Mode 流程", "100%", "3.5em") }}

说明：XIAO 主控根据传感器反馈或预存代码，自主控制机器人行动。  
{{ fig_indent_adjustable("../images/image_35.png","Autonomous Mode 说明", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_36.png","数据流向补充", "100%", "3.5em") }}

## 3. 机器人结构说明

{{ fig_indent_adjustable("../images/image_37.png","结构配图 1", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_38.png","结构配图 2", "100%", "3.5em") }}

1. 机器人结构展示以及舵机默认 ID 编号  
   {{ fig_indent_adjustable("../images/image_39.png","结构展示与默认 ID", "100%", "3.5em") }}
   {{ fig_indent_adjustable("../images/image_40.png","结构展示与默认 ID（补充）", "100%", "3.5em") }}
2. 机器人伺服舵机处于零度时的姿态  
   {{ fig_indent_adjustable("../images/image_41.png","零度姿态", "100%", "3.5em") }}
   {{ fig_indent_adjustable("../images/image_42.png","零度姿态（补充）", "100%", "3.5em") }}

## 4. 动作编辑器使用说明

{{ fig_indent_adjustable("../images/image_43.png","动作编辑器配图 1", "100%", "3.5em") }}

{{ fig_indent_adjustable("../images/image_44.png","动作编辑器配图 2", "100%", "3.5em") }}

Web 版动作编辑器：`https://wiki.fashionrobo.com/uartbasic/robotstudiopro/`

### 4.1 编辑器整体框架说明

动作编辑器整体可分为 3 个模块：

1. 串口连接/断开操作以及发送信息情况模块
2. 舵机状态/角度查询与角度控制模块
3. 机器人动作组优化与动作组数据导出/导入模块

### 4.2 编辑器控件说明

#### 4.2.1 串口连接与关闭

#### 4.2.2 实时姿态数据页面

- **布局**：每个舵机的控件可以在画布中拖动，可以将机器人的位置摆放出来并且 ID 号也与之对应，点击即可将该布局锁定。
- **扫描**：重新扫描机器人中所有的在线舵机。
- **检查**：点击可检查到是否高低压保护以及堵转等异常状态。
- **单次读取**：单次读取舵机的实时角度。
- **状态颜色**：绿色状态为舵机在角度控制状态下，红色状态为舵机在卸力/阻尼释放状态下。

通过拖拽可对舵机的角度进行控制：

- **实时读取**：实时读取舵机的角度。
- **速度**：该速度为上方拖拽滑动条舵机角度控制的速度，防止舵机角度控制速度太快。
- **解锁模式**：将舵机进行释放以方便进行动作编辑，可卸力释放/阻尼释放。

#### 4.2.3 动作组数据页面

- **动作组**：用户可自行配置动作组，数量不限。
- **添加动作组**
- **检查异常状态**（高低压保护/堵转等）
- **删除整个动作组**（至少保留一组）
- **运动验证**：点击即可对刚刚添加的所有动作进行运动验证。
- **循环播放**：点击循环开启即可重复播放动作。
- **停止播放**：停止动作组的播放。
- **调整动作顺序**：可通过拖动单个动作来调整动作之间的顺序。
- **动作时间（Time）**：舵机转到目标角度需要的时间（如图示例为 2s）。
- **间隔时间（Interval）**：动作与动作之间的等待时间。
- **删除所属动作**
- **运行所属动作**
- **添加当前编辑动作**
- **导出动作组数据**：导出整个动作组的舵机数据，便于导入到控制器中。
- **导入动作组数据**：导入已有动作组数据并进行更改。

### 4.3 从动作编辑到机器人离线动作的流程（示例：Seeed Studio XIAO ESP32S3 Sense）

1. 点击“连接串口”对机器人进行串口连接。
2. 选择机器人所在的串口。
3. 扫描出机器人身上的所有伺服舵机。
4. 点击“全卸”将机器人身上的所有舵机释放控制，以方便进行掰动结构进行动作编辑；若只需要对手部或者腿部舵机进行编辑，可单独解锁需要执行的舵机进行动作编辑。
5. 设置“动作时间”以及“间隔时间”。
6. 每编辑好一个动作后点击“添加当前”，可将当前机器人的动作添加进当前动作组。
7. 动作组编辑完成后可以点击播放进行验证。

说明：单独的每个动作均可以进行单个舵机的角度修改、时间修改、间隔修改以及动作验证。

8. 点击“导出(JSON)”将动作组数据导出为 JSON 文件。
9. 打开导出的 JSON 文件，复制 `frames` 里面的内容（包括 `[]` 在内的所有内容）。
10. 将刚刚在 JSON 文件复制的内容替换 `jsonData` 里面的所有内容，完成后即可编译将程序下载到控制板中，并且通过蓝牙手柄对机器人进行具体控制（可参考“机器人控制参数说明章节”）。

## 5. 机器人控制参数说明（按实际情况修改）

### 5.1 机器人默认参数说明

- `BAUDRATE`：机器人串口波特率。  
- `SERVO_NUM`：机器人舵机数量。  

### 5.2 蓝牙参数说明（如使用）

- `BLE_NAME`：蓝牙手柄名称。  
- `BLE_UUID`：蓝牙手柄 UUID。  

### 5.3 Web 端遥控参数说明（如使用）

- `SERVICE_UUID`：服务 ID。  
- `CHARACTERSTIC_UUID`：特征 ID。  

### 5.4 示教模式参数说明

- `MAX_ACTIONNUM`：示教模式最大的动作组数量。  
- `Default_RobotRunSpeed_Demonstration`：示教模式运行的默认速度。  
- `MIN_RobotRunSpeed_Demonstration`：示教模式运行的最大速度。  
- `MAX_RobotRunSpeed_Demonstration`：示教模式运行的最小速度。  
- `Adjust_RobotRunSpeed_Step`：在调节示教模式运行速度时的步进值，每次加减 200。  

### 5.5 数据说明（按实际需求修改）

- `RemoteControl_DefaultDemoAction`：默认演示动作，即用户通过动作编辑器实现的动作。  
- `RemoteControl_Exe`：示教模式执行命令。  
- `RemoteControl_Record`：示教模式记录动作命令。  
- `RemoteControl_Damping`：阻尼模式命令。  
- `RemoteControl_Reset`：机器人复位命令。  
- `RemoteControl_ReduceRunSpeed`：减少示教运行速度。  
- `RemoteControl_AddRunSpeed`：增加示教运行速度。  

蓝牙手柄说明：遥控器的具体数据需要用户自行确认，并且确定自己的按键需求，再对控制程序进行修改。  
Web 端遥控说明：遥控器的具体数据需要用户自行确认，并且确定自己的按键需求，再对控制程序进行修改。  

### 5.6 机器人复位角度参数说明

- `ROBOT_RESET_POSITION_0` ~ `ROBOT_RESET_POSITION_16`：0 号舵机 ~ 16 号舵机的零位角度设置（机器人复位角度）。  

说明：用户需要按照自己的机器人复位角度进行参数修改。  

## 6. 遥控说明

### 6.1 蓝牙手柄按键使用说明

1. 蓝牙手柄长按开机并与 MCU（XIAO_ESP32S3）进行蓝牙配对连接。
2. 当蓝牙手柄与 MCU 配对成功时，机器人会执行鞠躬动作与复位。

操作说明：

- 按下“机器人默认动作执行”：机器人会执行内置的一个动作。
- 按下“机器人复位”：机器人处于默认的复位动作。
- 按下“机器人阻尼模式”：机器人处于可摆动状态，用户可通过阻尼模式进行示教动作编辑。
- 按下“机器人示教动作记录”：机器人会记录此时用户所摆动的机器人动作。
- 按下“机器人示教模式动作执行”：机器人会执行用户刚刚所记录的示教动作，执行完默认不会清除。
- 按下“减少机器人示教模式执行速度”：系统会减少机器人执行示教动作的运行速度，机器人头部的 13 号舵机会进行左右旋转来展示当前的动作速度。
- 按下“增加机器人示教模式执行速度”：系统会增加机器人执行示教动作的运行速度，机器人头部的 13 号舵机会进行左右旋转来展示当前的动作速度。

### 6.2 手机/电脑 Web 端遥控使用说明

- 未连接状态。
- 寻找设备并点击配对进行连接。
- 已连接状态：当 Web 端遥控与 MCU 配对成功时，机器人会执行鞠躬动作与复位。

Web 端遥控所有按键说明：程序中“红色”的按键数据存在 `btn_Main`，“黄色”的按键数据存在 `btn_border`。

在 Demo 程序中，默认遥控按键定义如下：

- **红色**
  - `0X01`：“增加机器人示教模式执行速度”，系统会增加机器人执行示教动作的运行速度，机器人头部的 13 号舵机会进行左右旋转来展示当前的动作速度。
  - `0X02`：“增加机器人示教模式执行速度”，系统会减少机器人执行示教动作的运行速度，机器人头部的 13 号舵机会进行左右旋转来展示当前的动作速度。
  - `0X04`：“机器人示教动作记录”，机器人会记录此时用户所摆动的机器人动作。
  - `0X08`：“机器人示教模式动作执行”，机器人会执行用户刚刚所记录的示教动作，执行完默认不会清除。
  - `0X10`：“机器人默认动作执行”，机器人会执行内置的一个动作。
  - `0X20` ~ `0X80`：默认未定义。
- **黄色**
  - `0X01` ~ `0X02`：默认未定义。
  - `0X04`：“机器人阻尼模式”，机器人处于可摆动状态，用户通过阻尼模式进行示教动作编辑。
  - `0X08`：“机器人复位”，机器人处于默认的复位动作。
  - `0X10` ~ `0X80`：默认未定义。

Web 端遥控器链接：`https://wiki.fashionrobo.com/ps2v2/`

## 7. 附录

- Fashionstar 舵机 Wiki 资料：`https://wiki.fashionrobo.com/`
- 提供 STM32 / Python / ROS / C++ / Arduino 等舵机控制 SDK
