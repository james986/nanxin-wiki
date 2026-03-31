# Pidadapter - Cello 机械臂调优工具

| 版本 | 适配环境 | 入口 |
| :---: | :---: | :---: |
| <span class="no-wrap">v2026.02.14</span> | <span class="no-wrap">Windows、macOS、Linux</span> | [打开网页调试工具](./data/pidadapter/index.html){ .fs-download-btn target="_blank" } |


## 概述

Pidadapter 是华馨京科技（Fashion Star）开发的 Cello 机械臂调优工具，用于连接和配置机械臂的串口参数，提供不同的动力模式以适应不同的使用场景。



## 功能特性

### 设备连接
- **串口连接**：通过浏览器连接机械臂串口
- **推荐浏览器**：Chrome 或 Edge 浏览器

### 动力模式优化

提供三种动力模式，可根据实际应用场景选择：

#### 轻载模式（柔顺防抖）
- **适用场景**：空载场景
- **特点**：优化慢速运动抖动，提供柔顺的运动体验
- **优势**：运动更加平滑，减少振动

#### 标准模式（平衡通用）
- **适用场景**：常规操作
- **特点**：平衡力度与平顺性
- **优势**：在力度和运动平顺性之间达到最佳平衡

#### 重载模式（高刚性）
- **适用场景**：末端负载较大场景
- **特点**：增强大臂刚性
- **优势**：提供更强的支撑能力，确保负载稳定



> [!CAUTION]
> - 写入参数期间**禁止断电**或**拔出数据线**
> - 更新参数期间请务必保证电源稳定
> - 任何中断都可能导致舵机配置损坏



## 详细操作流程

### 第一步：打开工具页面

<ol class="ol-plain">
  <li><a href="./data/pidadapter/index.html" target="_blank">点击打开网页调试工具</a></li>
  <li>页面加载完成后，您将看到主界面</li>
</ol>

{{ fig_indent_adjustable("../images/image.png","工具主界面", "100%", "3.5em") }}

### 第二步：连接机械臂

<ol class="ol-plain">
  <li>
    <strong>找到连接按钮</strong>
    <ul>
      <li>页面上方显示“1. 设备连接”区域</li>
      <li>点击蓝色的“连接机械臂”按钮</li>
    </ul>
  </li>
  <li>
    <strong>串口选择</strong>
    <ul>
      <li>浏览器会弹出串口设备选择对话框</li>
      <li>从下拉列表中选择您的机械臂对应的串口设备</li>
      <li>端口名称通常为 <code>/dev/ttyUSB*</code>（Linux/macOS）或 <code>COM*</code>（Windows）</li>
    </ul>
  </li>
  <li>
    <strong>确认连接</strong>
    <ul>
      <li>点击“连接”按钮</li>
      <li>等待连接建立</li>
      <li>连接成功后，状态会从“DISCONNECTED”变为“CONNECTED”</li>
    </ul>
  </li>
</ol>

### 第三步：选择合适的动力模式

根据您的实际使用场景选择模式：

| 场景描述 | 推荐模式 | 选择原因 |
|---------|---------|---------|
| 机械臂空载运行 | 轻载模式 | 减少抖动，运动更柔顺 |
| 常规作业（负载适中） | 标准模式 | 平衡性能与稳定性 |
| 承载重物作业 | 重载模式 | 增强刚性，防止变形 |

**操作步骤**：

<ol class="ol-plain">
  <li>
    <strong>选择模式</strong>
    <ul>
      <li>选择所需的动力模式，出现蓝色高亮 <code>[ ]</code> 后点击按钮。</li>
    </ul>
  </li>
  <li>
    <strong>确认写入</strong>
    <ul>
      <li>页面会弹出确认对话框：“确认写入参数？”</li>
      <li>对话框提示：<em>更新参数期间请务必保证电源稳定。任何中断都可能导致舵机配置损坏。</em></li>
    </ul>
    {{ fig_indent_adjustable("../images/image-1.png","确认写入参数", "100%", "3.5em") }}
  </li>
  <li>
    <strong>安全检查</strong>
    <ul>
      <li>✅ 确认电源稳定连接</li>
      <li>✅ 确认机械臂数据线未松动</li>
      <li>✅ 确认周围无断电风险</li>
    </ul>
  </li>
  <li>
    <strong>执行写入</strong>
    <ul>
      <li>点击“确定写入”按钮。</li>
      <li>或点击“取消”放弃操作。</li>
    </ul>
  </li>
  <li>
    <strong>进度监控</strong>
    <ul>
      <li>页面显示进度条：“就绪... 0%”。</li>
      <li>进度条会从 0% 逐渐增加到 100%。</li>
      <li>此过程中<strong>严禁</strong>断电或拔线。</li>
    </ul>
  </li>
  <li>
    <strong>完成写入</strong>
    <ul>
      <li>页面显示“配置成功”提示。</li>
      <li>机械臂参数已更新为新模式。</li>
      <li>可以开始使用机械臂。</li>
    </ul>
  </li>
</ol>

{{ fig_indent_adjustable("../images/image-2.png","写入完成", "100%", "3.5em") }}



## 常见问题与处理方法

<details markdown>
<summary><strong>无法连接机械臂。</strong></summary>

  - **可能原因**：
    - 浏览器不支持 Web Serial API；
    - 串口设备未被识别。
  - **处理方法**：
    - 使用 Chrome 或 Edge 最新版本浏览器；
    - 检查机械臂电源和 USB 线连接；
    - 尝试更换 USB 端口；
    - 重新插拔机械臂 USB 线。
</details>

<details markdown>
<summary><strong>连接后立即断开。</strong></summary>

  - **可能原因**：
    - USB 驱动问题；
    - 串口权限不足。
  - **处理方法**：
    - Linux/macOS 可尝试运行 `sudo chmod 666 /dev/ttyUSB*`；
    - 检查防火墙设置；
    - 尝试以管理员权限运行浏览器。
</details>

<details markdown>
<summary><strong>写入参数失败。</strong></summary>

  - **可能原因**：
    - 电源不稳定；
    - 数据线松动；
    - 机械臂未正常启动。
  - **处理方法**：
    - 检查电源供电是否稳定；
    - 确保数据线连接牢固；
    - 重启机械臂后重试。
</details>



## 故障排查清单

!!! tip "在操作前，请确认以下项目："
    <span style="font-size: 1.2em; line-height: 1;">☐</span> 机械臂已通电并正常运行  
    <span style="font-size: 1.2em; line-height: 1;">☐</span> USB 数据线连接牢固  
    <span style="font-size: 1.2em; line-height: 1;">☐</span> 串口设备已被识别  
    <span style="font-size: 1.2em; line-height: 1;">☐</span> 网络连接正常  
    <span style="font-size: 1.2em; line-height: 1;">☐</span> 电源供应稳定  
    <span style="font-size: 1.2em; line-height: 1;">☐</span> 环境无断电风险
