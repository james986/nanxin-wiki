# 欢迎来到南芯微电子

这是南芯微 Wiki 的首版站点骨架，当前已按“中文单站 + GitHub Pages 项目站点”方式整理完成，可直接作为新仓库的基础版本继续删改。

- 预设访问地址：`https://james986.github.io/nanxin-wiki/`
- 当前内容状态：沿用原 wiki 的结构与大部分内容，后续请按保留栏目清单继续删减
- 当前部署方式：GitHub Actions 自动构建并发布到 GitHub Pages


---

## 🔥 舵机选型器

**[进入舵机选型器](./servo/selection/)**  
按扭矩、尺寸、通信方式快速筛选型号，建议先从这里确定目标产品。

---

## 🚀 快速开始

通过以下入口，可快速完成 UART 总线舵机从选型、开发到调试的基础流程。

| 资源 | 描述 |
| :--- | :--- |
| **[产品规格书](./servo/uart/datasheet/index.md)** | 查看 UART 总线舵机各型号的关键参数、接口定义与应用说明。 |
| **[图纸与模型下载](./servo/uart/cad-files/index.md)** | 获取 CAD 图纸与 3D 模型（PDF / DWG / STEP），用于结构设计与工程集成。 |
| **[通讯协议](./servo/uart/protocols/uart-rs485-protocol.md)** | 查阅 UART/RS485 协议格式、指令定义、回包结构与校验规则。 |
| **[上位机使用手册](./software/servo/pc-config-software.md)** | 进入上位机相关文档，完成串口连接、参数配置、状态读取与功能调试。 |

---

## 💻 软件开发工具 SDK

通过多语言、多平台 SDK，快速完成总线舵机的控制开发与系统集成。

- **[SDK 工具包总览](./sdk/index.md)**：查看全部 SDK 分类与入口。
- **Arduino 平台：**
    - [Arduino Uno SDK](./sdk/servo/arduino-uno-sdk.md)
    - [Arduino Mega 2560 SDK](./sdk/servo/arduino-mega-2560-sdk.md)
    - [ESP32（NodeMCU-32S）SDK](./sdk/servo/arduino-esp32-sdk.md)
    - [STM32F103C8T6（Arduino Core）SDK](./sdk/servo/arduino-stm32f103c8t6-sdk.md)
- **STM32 原生开发：**
    - [STM32F103 SDK](./sdk/servo/stm32f103-sdk.md)
    - [STM32F407 SDK](./sdk/servo/stm32f407-sdk.md)
- **桌面与通用语言：**
    - [Python SDK](./sdk/servo/python-sdk.md)
    - [C++ SDK](./sdk/servo/cpp-sdk.md)
    - [C# SDK](./sdk/servo/csharp-sdk.md)
- **嵌入式与机器人中间件：**
    - [MicroPython SDK](./sdk/servo/micropython-sdk.md)
    - [ROS2 SDK](./sdk/servo/ros2-sdk.md)

---

## 🏭 工业 PLC 应用

面向主流 PLC 平台，提供从硬件接线、通信配置到控制示例的完整接入方案。**[总览](./industrial/index.md)**

| 平台 | 适配型号 |
| :--- | :--- |
| 西门子 | <ul><li><a href="./industrial/plc/sinamics-tia-portal-v19.md">TIA Portal v19（S7-1200）</a></li><li><a href="./industrial/plc/step7-microwin-smart.md">STEP 7-MicroWIN SMART（S7-200 SMART）</a></li></ul> |
| 汇川 | <ul><li><a href="./industrial/plc/autoshop.md">AutoShop（H5U）</a></li><li><a href="./industrial/plc/inovance-inoproshop.md">InoproShop（AM401）</a></li></ul> |
| 三菱 | <ul><li><a href="./industrial/plc/mitsubishi-gx-works2.md">GX Works2（FX3U）</a></li></ul> |
| Codesys | <ul><li><a href="./industrial/plc/codesys.md">GCAN302</a></li></ul> |

---

## 🤖 具身智能化机器人平台

<style>
.md-typeset .robot-platform-cards {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
@media (max-width: 960px) {
  .md-typeset .robot-platform-cards {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="grid cards robot-platform-cards" markdown>

-   __[机械手臂](./robotic-arm/index.md)__
    
    覆盖 StarAI Arm、Star Arm 102、PiPER Mate 的规格、快速上手、仿真与开源资料。

-   __[双足机器人](./humanoid/index.md)__
    
    提供 Atom 系列的规格书、图纸下载、用户手册与常见问题。

-   __[舵机云台](./gimbal/index.md)__
    
    提供云台项目的物料清单、接线、控制与组装教程。

-   __[机器人软件与工具](./software/index.md)__
    
    包含动作编辑器、PID 调试工具、网页调试工具等开发辅助资源。

</div>

---

## 📚 技术资料

提供协议解析、功能原理、上位机排障与工程实践等技术内容，支持快速定位问题并完成系统集成。

- **[技术文档总览](./documents/index.md)**：查看全部知识文档入口。
- **[总线舵机使用基础](./documents/servo/model-selection-and-naming.md)**：选型、命名规则、线序、供电、安装等基础知识。
- **[通信协议对比](./documents/servo/protocol-comparison.md)**：UART / RS485 / CAN Bus 通信方式与适配建议。
- **[上位机使用技巧](./documents/servo/troubleshooting-not-detected-or-no-response.md)**：常见连接、参数、响应异常问题排查。
- **[功能详解](./documents/servo/single-turn-vs-multi-turn-angle.md)**：单圈/多圈、阻尼、同步、停止、数据监控等模式说明。

---

!!! tip "下一步建议"
    1. 先在 `mkdocs.yml` 中替换 `<owner>` 与 `<repo>` 占位符。  
    2. 先删导航中的不保留栏目，再删除对应文档和资源。  
    3. 替换首页文案、联系方式、品牌素材与外链。  
    4. 推送到 GitHub 后，在仓库设置中启用 GitHub Pages。  
