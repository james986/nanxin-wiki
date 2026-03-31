# 🚀 快速开始

### 环境要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Ubuntu 22.04 |
| ROS版本 | ROS2 Humble |
| 硬件设备 | PiPER Mate机械臂 + Piper 机械臂 |
| 驱动程序 | [CH340 USB驱动](https://www.wch.cn/downloads/CH341SER_EXE.html) |

### 安装步骤

#### 方式一：Python SDK（推荐新手）

```bash
# 1. 安装依赖
sudo apt update && sudo apt install can-utils ethtool
sudo pip install serial fashionstar-uart-sdk piper-sdk python-can scipy

# 2. 配置CAN接口
cd piper-mate
bash find_all_can_port.sh
bash can_activate.sh can0 1000000

# 3. 运行程序
sudo chmod 777 /dev/ttyUSB*
python3 ./Python_SDK/piper_pipermate.py
```

#### 方式二：ROS2 HUMBLE

```bash
# 1. 安装ROS2依赖
cd ROS2_HUMBLE
colcon build
source install/setup.bash

# 2. 启动节点（需要两个终端）
# 终端1：启动PiPER Mate驱动
ros2 run piper-mate driver --ros-args -p port:=/dev/ttyUSB0 -p auto_enable:=false

# 终端2：启动Piper控制
bash can_activate.sh can0 1000000
ros2 run piper piper_single_ctrl --ros-args -p can_port:=can0 -p auto_enable:=true
```

#### 方式三：Lerobot 框架

```bash
# 参考Lerobot/README.md配置说明
```

---

## 📂 项目结构

```bash
PiPER-Mate/
├── Python_SDK/                  # Python SDK控制方式
│   ├── piper_pipermate.py       # 主控制程序
│   └── README.md                # 详细使用文档
├── ROS2_HUMBLE/                 # ROS2控制方式
│   ├── src/piper/               # Piper驱动节点
│   ├── src/piper-mate/          # Piper_mate驱动节点
│   ├── src/piper_msgs/          # Piper消息定义
│   └── README.md                # ROS2使用文档
├── Lerobot/                     # Lerobot框架控制方式
│   ├── lerobot_robot_piper/     # Piper机器人配置
│   ├── lerobot_teleoperator_pipermate/  # 遥操作器
│   └── piper-star_en.md         # Lerobot使用文档（英文）
│   └── piper-star.md            # Lerobot使用文档
│   └── README.md                # 使用步骤
├── can_activate.sh              # CAN接口激活（根目录）
├── can_config.sh                # CAN接口配置
└── README.md                    # 本文档
```

---

## 🎯 控制方式对比

| 特性 | Python SDK | ROS2 HUMBLE | Lerobot |
|------|------------|-------------|---------|
| 难度 | ⭐ 简单 | ⭐⭐⭐ 中等 | ⭐⭐⭐⭐⭐ 复杂 |
| 实时性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 扩展性 | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 适用场景 | 快速测试、教学 | 机器人系统集成 | AI训练、研究 |

---

## 🔧 硬件连接

### 连接拓扑

```bash
┌─────────────────┐         USB          ┌─────────────────┐
│                 │◄────────────────────►│                 │
│   PiPER Mate    │                      │      计算机      │
│     机械臂       │                      │ (Ubuntu 22.04)  │
└─────────────────┘                      └────────┬────────┘
                                                  │
                                                 USB
                                                  │
┌─────────────────┐         CAN          ┌────────┴────────┐
│                 │◄────────────────────►│                 │
│      Piper      │                      │  CAN转USB适配器  │
│      机械臂      │                      │                 │
└─────────────────┘                      └─────────────────┘
```

---

## 📊 关节映射

系统自动将 PiPER Mate 的 6 个关节映射到 Piper 机械臂：

| 关节 | PiPER Mate 角度 | Piper 弧度 | 方向 |
|------|------------------|------------|------|
| Joint1 | -150° ~ 150° | -2.62 ~ 2.62 rad | 反向 |
| Joint2 | 0° ~ 180° | 0 ~ 3.14 rad | 正向 |
| Joint3 | -170° ~ 0° | -2.97 ~ 0 rad | 正向 |
| Joint4 | -100° ~ 100° | -1.75 ~ 1.75 rad | 反向 |
| Joint5 | -70° ~ 70° | -1.22 ~ 1.22 rad | 正向 |
| Joint6 | -120° ~ 120° | -2.09 ~ 2.09 rad | 反向 |

---

## ⚠️ 安全注意事项

1. **操作前检查**：确保机械臂周围无障碍物，工作空间安全
2. **急停控制**：程序运行时按 `Ctrl+C` 可立即停止
3. **关节限制**：系统已自动设置安全角度限制，避免越界运动
4. **电源管理**：确保机械臂供电稳定，避免电压波动

---

## 🐛 故障排除

### 常见问题

**Q1: 找不到 `/dev/ttyUSB0` 设备？**

```bash
# 检查USB设备
ls -l /dev/ttyUSB*

# 检查CH340驱动
lsusb | grep CH340

# 如果没有安装驱动，请从官网下载安装
```

**Q2: CAN 接口无法激活？**

```bash
# 查找CAN端口
bash find_all_can_port.sh

# 手动激活CAN接口
sudo ip link set can0 type can bitrate 1000000
sudo ip link set up can0

# 检查CAN接口状态
ip link show can0
```

**Q3: 机械臂连接失败？**

- 检查USB线连接是否松动
- 确认机械臂电源已开启
- 检查驱动板开关位置（应拨向电源接口一侧）
- 尝试更换USB端口

**Q4: USB连接断开时程序不终止？**

程序已添加异常处理，当PiPER Mate USB断开时会自动终止并显示错误信息：

```bash
❌ 致命错误：PiPER Mate USB连接断开！
```

---

## 📖 详细文档

选择你需要的控制方式查看详细文档：

- 📘 **[Python SDK 详细文档](./Python_SDK/README.md)** - 推荐！最简单易用
- 📗 **[ROS2 HUMBLE 详细文档](./ROS2_HUMBLE/README.md)** - 适用于机器人系统集成
- 📙 **[Lerobot 详细文档](./Lerobot/README.md)** - 适用于AI训练和研究

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源。

---

## 👥 作者与致谢

- **项目维护者**：[Welt-liu](https://github.com/Welt-liu)
- **感谢**：PiPER Mate 和 Piper 团队的硬件支持

---

## 🔗 相关链接

- [PiPER Mate 官方仓库](https://github.com/servodevelop/piper-mate/tree/main)
- [Piper ROS2 官方仓库](https://github.com/agilexrobotics/piper_ros/tree/humble/)
- [Lerobot 框架](https://github.com/huggingface/lerobot)

---
- **项目维护者**：<span class="fs-contributors-inline"><a href="https://github.com/Welt-liu" target="_blank"><img src="https://github.com/Welt-liu.png" class="fs-avatar" title="Welt-liu"></a></span>

- **感谢**：PiPER Mate 和 Piper 团队的硬件支持


## 3. 规格参数
### 3.1. 基础参数
<table>
  <tr>
    <th width="200" align="left">参数项目</th>
    <th width="400" align="left">技术规格</th>
  </tr>
  <tr>
    <td>工作电压</td>
    <td>9.0～12.6 V</td>
  </tr>
  <tr>
    <td>马达类型</td>
    <td>空心杯马达</td>
  </tr>
  <tr>
    <td>位置传感器</td>
    <td>12-bit 非接触式绝对值编码器</td>
  </tr>
  <tr>
    <td>分辨率</td>
    <td>4096 阶 / 360°（0.088°）</td>
  </tr>
  <tr>
    <td>有效角度</td>
    <td>±180°(单圈)/±368,640°(多圈)</td>
  </tr>
  <tr>
    <td>处理器</td>
    <td>32-bit MCU</td>
  </tr>
  <tr>
    <td>通信类型</td>
    <td>UART / TTL 半双工</td>
  </tr>
  <tr>
    <td>波特率</td>
    <td>9,600 bps ～ 1 Mbps</td>
  </tr>
  <tr>
    <td>ID 范围</td>
    <td>0 ～ 254</td>
  </tr>
  <tr>
    <td>减速比</td>
    <td>273:1</td>
  </tr>
  <tr>
    <td>齿轮材料</td>
    <td>全金属不锈钢组合</td>
  </tr>
  <tr>
    <td>输出轴规格</td>
    <td>不锈钢 / Ø6 mm / 25T</td>
  </tr>
  <tr>
    <td>外壳材料</td>
    <td>铝合金中段 / 上下壳工程塑胶</td>
  </tr>
  <tr>
    <td>接口类型</td>
    <td>PH2.0 – 3Pin</td>
  </tr>
  <tr>
    <td>尺寸重量</td>
    <td>40 × 20 × 40 mm / 73 g</td>
  </tr>
  <tr>
    <td>工作温度</td>
    <td>-10～60 ℃</td>
  </tr>
  <tr>
    <td>工作模式</td>
    <td>单圈角度 | 多圈角度 | 阻尼模式</td>
  </tr>
</table>

### 3.2. 特性参数（@12V）
<table>
  <tr>
    <th width="200" align="left">参数项目</th>
    <th width="400" align="left">规格内容</th>
  </tr>
  <tr>
    <td>最大静态扭矩（堵转）</td>
    <td>4.41 N·m（45 kg·cm）</td>
  </tr>
  <tr>
    <td>最大动态扭矩</td>
    <td>1.67 N·m（17 kg·cm）</td>
  </tr>
  <tr>
    <td>额定扭矩</td>
    <td>0.54 N·m（5.5 kg·cm）</td>
  </tr>
  <tr>
    <td>额定转速</td>
    <td>64 rpm（0.156 s / 60°）</td>
  </tr>
  <tr>
    <td>空载转速</td>
    <td>90 rpm（0.110 s / 60°）</td>
  </tr>
  <tr>
    <td>峰值电流</td>
    <td>6 A</td>
  </tr>
  <tr>
    <td>空载电流</td>
    <td>＜300 mA</td>
  </tr>
  <tr>
    <td>静态电流</td>
    <td>＜30 mA</td>
  </tr>
  <tr>
    <td>轴向</td>
    <td>20 N</td>
  </tr>
   <tr>
    <td>径向</td>
    <td>40 N</td>
  </tr>

</table>


<div style="text-align: center; margin-bottom: 20px;">
  <img src="/servo/uart/datasheet/images/U25-torque-speed-curve.png" 
       style="width: 500px !important; height: auto !important; display: inline-block;">
  <div style="margin-top: 10px; font-weight: bold; font-size: 14px;">
    T-N 特性曲线
  </div>
</div>

<div style="text-align: center; margin-bottom: 20px;">
  <img src="/servo/uart/datasheet/images/U25-mechanical-overload-curve.png" 
       style="width: 500px !important; height: auto !important; display: inline-block;">
  <div style="margin-top: 10px; font-weight: bold; font-size: 14px;">
    机械过载曲线
  </div>
</div>
