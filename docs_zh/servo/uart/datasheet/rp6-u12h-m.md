# 产品规格书 - QM3006M6-VB

<!--
MOSFET 规格书模板说明：
1. 替换其他产品时，优先更新“文档信息、产品概述、关键参数、极限额定值、热阻、电气特性、封装与引脚、典型特性”各表格。
2. 所有参数应以原厂 PDF 规格书为准，保留测试条件、温度条件、最小值/典型值/最大值和单位。
3. 若 PDF 中存在曲线图或封装图，可在对应章节补充图片；没有图片时，使用文字列表保留曲线名称。
4. 面向用户访问时，本页应呈现为完整器件规格书，不展示模板维护说明。
5. 若源 PDF 的关键信息以图片形式呈现，应导出原图或页面截图并在本页引用，避免丢失曲线图、封装图和推荐焊盘图。
-->

## 1. 文档信息

| 项目 | 内容 |
| --- | --- |
| 产品型号 | QM3006M6-VB |
| 器件类型 | N 沟道 MOSFET |
| 漏源电压 | 30 V |
| 封装 | DFN5X6 |
| 原厂 | Taiwan VBsemi Electronics Co., Ltd. |
| 官网 | www.VBsemi.com |
| 整理依据 | QM3006M6-VB PDF 规格书 |

## 2. 产品概述

QM3006M6-VB 是一款 30 V N 沟道功率 MOSFET，采用 DFN5X6 封装，适用于笔记本电脑核心供电、VRM/POL 等低压大电流电源场景。器件采用沟槽型功率 MOSFET 工艺，规格书标注已进行 100% 栅极电阻（Rg）和单脉冲雪崩（UIS）测试。

![QM3006M6-VB 产品摘要、封装与引脚图](../images/qm3006m6-vb-summary-package-pinout.png)

### 2.1 关键参数

| 参数 | 符号 | 数值 | 条件 |
| --- | --- | --- | --- |
| 漏源电压 | V<sub>DS</sub> | 30 V | - |
| 连续漏极电流 | I<sub>D</sub> | 120 A | T<sub>C</sub> = 25 °C |
| 导通电阻 | R<sub>DS(on)</sub> | 0.003 Ω | V<sub>GS</sub> = 10 V |
| 导通电阻 | R<sub>DS(on)</sub> | 0.005 Ω | V<sub>GS</sub> = 4.5 V |
| 总栅极电荷 | Q<sub>g</sub> | 71 nC（典型值） | V<sub>DS</sub> = 15 V，V<sub>GS</sub> = 10 V，I<sub>D</sub> = 32 A |
| 工作结温 / 存储温度 | T<sub>J</sub> / T<sub>stg</sub> | -55～175 °C | - |

### 2.2 产品特点

- 沟槽型功率 MOSFET。
- 低导通电阻，适合低压大电流开关应用。
- 100% Rg 测试。
- 100% UIS 测试。
- DFN5X6 小型化贴片封装。

### 2.3 典型应用

- 笔记本电脑核心供电。
- VRM / POL 电源模块。
- 低压同步整流和负载开关。
- 需要低 R<sub>DS(on)</sub>、高电流能力的 DC-DC 转换器。

## 3. 极限额定值

> 除非另有说明，测试环境温度为 T<sub>A</sub> = 25 °C。超过极限额定值可能造成器件永久损坏，长期工作在极限条件下会影响可靠性。

| 参数 | 符号 | 条件 | 额定值 | 单位 |
| --- | --- | --- | --- | --- |
| 漏源电压 | V<sub>DS</sub> | - | 30 | V |
| 栅源电压 | V<sub>GS</sub> | - | ±20 | V |
| 连续漏极电流 | I<sub>D</sub> | T<sub>C</sub> = 25 °C | 120 | A |
| 连续漏极电流 | I<sub>D</sub> | T<sub>C</sub> = 70 °C | 90 | A |
| 连续漏极电流 | I<sub>D</sub> | T<sub>A</sub> = 25 °C，1" × 1" FR4，t = 10 s | 21 | A |
| 连续漏极电流 | I<sub>D</sub> | T<sub>A</sub> = 70 °C，1" × 1" FR4，t = 10 s | 20.8 | A |
| 脉冲漏极电流 | I<sub>DM</sub> | - | 250 | A |
| 雪崩电流脉冲 | I<sub>AS</sub> | L = 0.1 mH | 6 | A |
| 单脉冲雪崩能量 | E<sub>AS</sub> | L = 0.1 mH | 60 | mJ |
| 连续源漏二极管电流 | I<sub>S</sub> | T<sub>C</sub> = 25 °C | 80 | A |
| 连续源漏二极管电流 | I<sub>S</sub> | T<sub>A</sub> = 25 °C，1" × 1" FR4，t = 10 s | 76 | A |
| 最大功耗 | P<sub>D</sub> | T<sub>C</sub> = 25 °C | 210 | W |
| 最大功耗 | P<sub>D</sub> | T<sub>C</sub> = 70 °C | 155 | W |
| 最大功耗 | P<sub>D</sub> | T<sub>A</sub> = 25 °C，1" × 1" FR4，t = 10 s | 35 | W |
| 最大功耗 | P<sub>D</sub> | T<sub>A</sub> = 70 °C，1" × 1" FR4，t = 10 s | 13 | W |
| 工作结温与存储温度 | T<sub>J</sub> / T<sub>stg</sub> | - | -55～175 | °C |

注：T<sub>C</sub> 条件基于壳温；T<sub>A</sub> 条件基于表贴在 1" × 1" FR4 板上。规格书说明稳态最大结到环境热阻为 90 °C/W，封装限制电流为 80 A。

## 4. 热阻参数

| 参数 | 符号 | 条件 | 典型值 | 最大值 | 单位 |
| --- | --- | --- | --- | --- | --- |
| 结到环境热阻 | R<sub>thJA</sub> | t ≤ 10 s | 41 | 50 | °C/W |
| 结到外壳热阻 | R<sub>thJC</sub> | 稳态 | 0.7 | 0.9 | °C/W |

## 5. 电气特性

> 除非另有说明，T<sub>J</sub> = 25 °C。

### 5.1 静态特性

| 参数 | 符号 | 测试条件 | 最小值 | 典型值 | 最大值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- |
| 漏源击穿电压 | V<sub>DS</sub> | V<sub>GS</sub> = 0 V，I<sub>D</sub> = 250 µA | 30 | - | - | V |
| V<sub>DS</sub> 温度系数 | ΔV<sub>DS</sub>/T<sub>J</sub> | I<sub>D</sub> = 250 µA | - | 35 | - | mV/°C |
| V<sub>GS(th)</sub> 温度系数 | ΔV<sub>GS(th)</sub>/T<sub>J</sub> | - | - | -5.5 | - | mV/°C |
| 栅源阈值电压 | V<sub>GS(th)</sub> | V<sub>DS</sub> = V<sub>GS</sub>，I<sub>D</sub> = 250 µA | 1.0 | - | 2.5 | V |
| 栅源漏电流 | I<sub>GSS</sub> | V<sub>DS</sub> = 0 V，V<sub>GS</sub> = ±20 V | - | - | ±100 | nA |
| 零栅压漏极电流 | I<sub>DSS</sub> | V<sub>DS</sub> = 30 V，V<sub>GS</sub> = 0 V | - | - | 1 | µA |
| 零栅压漏极电流 | I<sub>DSS</sub> | V<sub>DS</sub> = 30 V，V<sub>GS</sub> = 0 V，T<sub>J</sub> = 55 °C | - | - | 10 | µA |
| 导通状态漏极电流 | I<sub>D(on)</sub> | V<sub>DS</sub> ≥ 5 V，V<sub>GS</sub> = 10 V | 80 | - | - | A |
| 导通电阻 | R<sub>DS(on)</sub> | V<sub>GS</sub> = 10 V，I<sub>D</sub> = 32 A | - | - | 0.003 | Ω |
| 导通电阻 | R<sub>DS(on)</sub> | V<sub>GS</sub> = 4.5 V，I<sub>D</sub> = 29 A | - | - | 0.005 | Ω |
| 正向跨导 | g<sub>fs</sub> | V<sub>DS</sub> = 15 V，I<sub>D</sub> = 32 A | - | 130 | - | S |

### 5.2 动态特性

| 参数 | 符号 | 测试条件 | 典型值 | 最大值 | 单位 |
| --- | --- | --- | --- | --- | --- |
| 输入电容 | C<sub>iss</sub> | V<sub>DS</sub> = 12.5 V，V<sub>GS</sub> = 0 V，f = 1 MHz | 3200 | - | pF |
| 输出电容 | C<sub>oss</sub> | V<sub>DS</sub> = 12.5 V，V<sub>GS</sub> = 0 V，f = 1 MHz | 1025 | - | pF |
| 反向传输电容 | C<sub>rss</sub> | V<sub>DS</sub> = 12.5 V，V<sub>GS</sub> = 0 V，f = 1 MHz | 970 | - | pF |
| 总栅极电荷 | Q<sub>g</sub> | V<sub>DS</sub> = 15 V，V<sub>GS</sub> = 10 V，I<sub>D</sub> = 32 A | 71 | - | nC |
| 总栅极电荷 | Q<sub>g</sub> | V<sub>DS</sub> = 15 V，V<sub>GS</sub> = 4.5 V，I<sub>D</sub> = 29 A | 61.5 | - | nC |
| 栅源电荷 | Q<sub>gs</sub> | V<sub>DS</sub> = 15 V，V<sub>GS</sub> = 4.5 V，I<sub>D</sub> = 29 A | 34 | - | nC |
| 栅漏电荷 | Q<sub>gd</sub> | V<sub>DS</sub> = 15 V，V<sub>GS</sub> = 4.5 V，I<sub>D</sub> = 29 A | 29 | - | nC |
| 栅极电阻 | R<sub>g</sub> | f = 1 MHz | 1.4 | 2.1 | Ω |

### 5.3 开关特性

| 参数 | 符号 | 测试条件 | 典型值 | 最大值 | 单位 |
| --- | --- | --- | --- | --- | --- |
| 开通延迟时间 | t<sub>d(on)</sub> | V<sub>DD</sub> = 15 V，R<sub>L</sub> = 0.555 Ω，I<sub>D</sub> ≈ 27 A，V<sub>GEN</sub> = 10 V，R<sub>g</sub> = 1 Ω | 18 | 27 | ns |
| 上升时间 | t<sub>r</sub> | 同上 | 11 | 17 | ns |
| 关断延迟时间 | t<sub>d(off)</sub> | 同上 | 70 | 105 | ns |
| 下降时间 | t<sub>f</sub> | 同上 | 10 | 15 | ns |
| 开通延迟时间 | t<sub>d(on)</sub> | V<sub>DD</sub> = 15 V，R<sub>L</sub> = 0.625 Ω，I<sub>D</sub> ≈ 24 A，V<sub>GEN</sub> = 4.5 V，R<sub>g</sub> = 1 Ω | 55 | 83 | ns |
| 上升时间 | t<sub>r</sub> | 同上 | 180 | 270 | ns |
| 关断延迟时间 | t<sub>d(off)</sub> | 同上 | 55 | 83 | ns |
| 下降时间 | t<sub>f</sub> | 同上 | 12 | 18 | ns |

### 5.4 体二极管特性

| 参数 | 符号 | 测试条件 | 典型值 | 最大值 | 单位 |
| --- | --- | --- | --- | --- | --- |
| 连续源漏二极管电流 | I<sub>S</sub> | T<sub>C</sub> = 25 °C | - | 80 | A |
| 脉冲二极管正向电流 | I<sub>SM</sub> | - | - | 100 | A |
| 体二极管正向电压 | V<sub>SD</sub> | I<sub>S</sub> = 22 A | 0.8 | 1.2 | V |
| 体二极管反向恢复时间 | t<sub>rr</sub> | I<sub>F</sub> = 20 A，di/dt = 100 A/µs，T<sub>J</sub> = 25 °C | 52 | 78 | ns |
| 体二极管反向恢复电荷 | Q<sub>rr</sub> | I<sub>F</sub> = 20 A，di/dt = 100 A/µs，T<sub>J</sub> = 25 °C | 70.2 | 105 | nC |
| 反向恢复下降时间 | t<sub>a</sub> | I<sub>F</sub> = 20 A，di/dt = 100 A/µs，T<sub>J</sub> = 25 °C | 27 | - | ns |
| 反向恢复上升时间 | t<sub>b</sub> | I<sub>F</sub> = 20 A，di/dt = 100 A/µs，T<sub>J</sub> = 25 °C | 25 | - | ns |

注：静态导通类参数为脉冲测试，脉宽 ≤ 300 µs，占空比 ≤ 2%。动态参数由设计保证，不作为量产测试项目。

## 6. 典型特性曲线

PDF 规格书包含以下典型特性曲线，可用于评估器件在不同电压、电流和温度条件下的行为：

| 曲线 | 说明 |
| --- | --- |
| 输出特性 | I<sub>D</sub> 与 V<sub>DS</sub> 的关系，覆盖不同 V<sub>GS</sub> 条件。 |
| 转移特性 | I<sub>D</sub> 与 V<sub>GS</sub> 的关系，覆盖不同壳温条件。 |
| 跨导曲线 | g<sub>fs</sub> 与 I<sub>D</sub> 的关系。 |
| R<sub>DS(on)</sub> 与漏极电流 | 比较 V<sub>GS</sub> = 4.5 V 和 10 V 条件下的导通电阻。 |
| 电容特性 | C<sub>iss</sub>、C<sub>oss</sub>、C<sub>rss</sub> 与 V<sub>DS</sub> 的关系。 |
| 栅极电荷 | V<sub>GS</sub> 与 Q<sub>g</sub> 的关系。 |
| R<sub>DS(on)</sub> 与结温 | 导通电阻随 T<sub>J</sub> 变化的归一化曲线。 |
| 正向二极管电压 | I<sub>S</sub> 与 V<sub>SD</sub> 的关系。 |
| R<sub>DS(on)</sub> 与 V<sub>GS</sub> | 不同温度下导通电阻与栅源电压的关系。 |
| 阈值电压 | V<sub>GS(th)</sub> 随结温变化的曲线。 |
| 安全工作区 | 单脉冲条件下 I<sub>D</sub> 与 V<sub>DS</sub> 的安全工作范围。 |
| 电流降额 | I<sub>D</sub> 随壳温 T<sub>C</sub> 的降额曲线。 |
| 功耗降额 | P<sub>D</sub> 随壳温 T<sub>C</sub> 的降额曲线。 |
| 瞬态热阻抗 | 结到外壳的归一化瞬态热阻抗曲线。 |

![QM3006M6-VB 典型特性曲线 1](../images/qm3006m6-vb-typical-characteristics-1.png)

![QM3006M6-VB 典型特性曲线 2](../images/qm3006m6-vb-typical-characteristics-2.png)

![QM3006M6-VB 电流降额、功耗降额与瞬态热阻抗曲线](../images/qm3006m6-vb-derating-thermal-impedance.png)

## 7. 封装与引脚

| 项目 | 内容 |
| --- | --- |
| 封装形式 | DFN5X6 |
| 视图 | PDF 提供 Top View 与 Bottom View |
| 器件结构 | N-Channel MOSFET，端子包含 D（漏极）、G（栅极）、S（源极） |
| 引脚编号 | PDF 图示包含 1～8 脚编号及 PIN1 标识 |

![QM3006M6-VB DFN5X6 封装外形与推荐焊盘](../images/qm3006m6-vb-package-outline.png)

设计 PCB 时应根据原厂封装图确认焊盘、散热铜皮和引脚连接。大电流路径应尽量降低寄生电阻和寄生电感，并结合 R<sub>thJC</sub>、R<sub>thJA</sub>、功耗降额曲线评估热设计余量。

## 8. 使用与可靠性提示

- 本器件的极限额定值仅用于器件承受能力说明，不能作为长期工作条件。
- 实际应用中需根据开关频率、占空比、散热条件、PCB 铜厚和铜皮面积重新计算结温。
- 在同步整流、VRM/POL 等高 di/dt 应用中，应关注栅极驱动回路、环路面积、栅极电阻和开关尖峰。
- 雪崩能力、体二极管反向恢复和安全工作区应按应用场景逐项核算。
- 原厂规格和数据可能因产品改进而变更，量产设计应以最新原厂 PDF 为准。

## 9. 环保与材料声明

规格书声明该系列产品符合 RoHS 要求，并符合 JEDEC JS709A 无卤标准。若应用对环保、可靠性或法规认证有强制要求，应在采购和量产前向供应商确认最新材料声明与合规文件。

## 10. 原始规格书页面图

以下图片由原始 PDF 逐页导出，用于保留表格、曲线、封装图和声明页等全部版面信息。

![QM3006M6-VB 规格书第 1 页](../images/qm3006m6-vb-page-01.png)

![QM3006M6-VB 规格书第 2 页](../images/qm3006m6-vb-page-02.png)

![QM3006M6-VB 规格书第 3 页](../images/qm3006m6-vb-page-03.png)

![QM3006M6-VB 规格书第 4 页](../images/qm3006m6-vb-page-04.png)

![QM3006M6-VB 规格书第 5 页](../images/qm3006m6-vb-page-05.png)

![QM3006M6-VB 规格书第 6 页](../images/qm3006m6-vb-page-06.png)

![QM3006M6-VB 规格书第 7 页](../images/qm3006m6-vb-page-07.png)
