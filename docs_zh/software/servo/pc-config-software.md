# 总线伺服舵机调试软件

| 版本 | 适配 OS | 安装包 |
| :---: | :---: | :---: |
| <span class="no-wrap">v1.1.9.288</span> | <span class="no-wrap">Windows</span> | [点击下载](./data/Develop-US-1.1.9.288.zip){ .fs-download-btn } |


## 1. 视频教程

<div class="fs-video-tutorial" style="position: relative; padding-top: 56.25%;">
  <video
    controls
    playsinline
    webkit-playsinline
    preload="auto"
    poster="../images/pc-config-software-cover.jpg"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: #000;">
    <source src="https://fashionrobo.com/wp-content/uploads/2026/02/pc-config-software.mp4" />
    当前浏览器不支持视频播放，请前往下方链接观看。
  </video>
</div>

> [!TIP]
> 若视频无法加载，请前往 **[B站观看](https://www.bilibili.com/video/BV1DnZLBTEgv/?share_source=copy_web&vd_source=2f21812dc64a5300b475fe4c7d5c183f)**。


## 2. 软件运行

- 软件为绿色版程序，无需安装，解压后直接运行 `Develop.exe` 即可使用。
  
 {{ fig_indent_adjustable("../images/pc-config-software-01.png","软件运行", "100%", "3.5em") }}




## 3. 舵机连接与识别

### 3.1 物理接线

请按照以下顺序完成舵机与电脑的硬件连接：

1. 用数据线连接舵机与转接板。
2. 接通舵机外部电源。
3. 使用 USB 数据线将转接板连接至电脑。

 {{ fig_indent_adjustable("../images/pc-config-software-02.png","物理连线", "100%", "3.5em") }}


> [!WARNING]
> 转接板输入电压必须与舵机的电源输入范围一致，否则会触发电压保护，无法正常使用。

### 3.2 串口连接

1. 点击左上角 **刷新装置** 刷新串口列表；
2. 在列表中选择自动识别到的转接板串口（如 COM10）；
3. 点击 **开关** 进行串口参数配置；
4. 点击 **确认** 完成串口连接。


 {{ fig_indent_adjustable("../images/pc-config-software-03.png","串口连接", "100%", "3.5em") }}

> [!NOTE]
> 若串口列表中未显示转接板的串口信息，可能驱动未正确安装。  
> 请[下载 ch340 驱动](./data/ch340.zip){ download }，安装后重新刷新串口列表。

### 3.3 扫描舵机
- **1.** 点击 **扫描舵机** 按钮，软件开始自动扫描；

{{ fig_indent_adjustable("../images/pc-config-software-04.png","扫描舵机", "100%", "3.5em") }}

- **2.** 扫描完成后，中间列表会显示找到的所有舵机；逐个选择即可查看当前工作状态；

- **3.** 列表中同时显示舵机固件版本信息，便于后续 固件升级 参考。

{{ fig_indent_adjustable("../images/pc-config-software-05.png","扫描舵机", "100%", "3.5em") }}
## 4. 实时控制

### 4.1 单圈角度控制

1. 点击 **舵机控制**；
2. 进入 **单圈角度控制** 标签页；
3. 按需设置 **控制模式** 参数；输入目标角度并点击 **送出**，舵机会运动到目标角度；
4. 点击 **停止**，舵机会停止工作，并进入所选停止模式；
5. 再次点击 **舵机控制** ，退出当前模式；

{{ fig_indent_adjustable("../images/pc-config-software-07.png","单圈角度控制", "100%", "3.5em") }}
> [!TIP]
> - 请先确认 **实时控制** 未被勾选；
> - 若勾选 **实时控制**，只能通过下方滑块拖拉进行控制；

### 4.2 多圈角度控制

1. 点击 **舵机控制**；
2. 进入 **多圈角度控制** 标签页；
3. 按需设置 **控制模式** 参数；输入目标角度并点击 **送出**，舵机会运动到目标角度；
4. 点击 **停止**，舵机会停止工作，并进入所选停止模式；
5. 再次点击 **舵机控制** ，退出当前模式；

{{ fig_indent_adjustable("../images/pc-config-software-08.png","多圈角度控制", "100%", "3.5em") }}

> [!TIP]
> - 多圈模式不支持实时拖动模式

### 4.3 读取当前角度
1. 点击 **舵机控制**；
2. 进入 **多圈角度控制** 标签页；
3. 点击 **更新**，对话框会显示舵机当前角度；当角度大于 360° 时，将以 **圈数 + 角度** 的形式显示；
64. 再次点击 **舵机控制** ，退出当前模式；


{{ fig_indent_adjustable("../images/pc-config-software-09.png","角度读取", "100%", "3.5em") }}

> [!TIP]
> - 单圈角度读取，也在 **多圈角度控制** 标签页中。

### 4.4 重置圈数
1. 点击 **舵机控制**；
2. 进入 **多圈角度控制** 标签页；
3. 点击 **重置圈数**，清除舵机记录的圈数信息，当前角度将被保留；
4. 再次点击 **舵机控制** ，退出当前模式；

{{ fig_indent_adjustable("../images/pc-config-software-10.png","重置圈数", "100%", "3.5em") }}

### 4.5 阻尼模式

1. 点击 **舵机控制**；
2. 进入 **阻尼控制** 标签页；
3. 按需设置 **功率** 参数；并点击 **送出**，此时，用外力转动舵机会有阻尼的效果；

{{ fig_indent_adjustable("../images/pc-config-software-14.png","阻尼模式", "100%", "3.5em") }}

> [!TIP]
> - 因为不同舵机的齿轮比不同，建议你先填入 **600mW** 进行尝试，根据实际效果再做微调。

## 5. 常用设置

### 5.1 修改舵机ID

1. 选中需要修改的舵机；
2. 点击 **修改舵机ID** 按钮，在弹窗中输入新的 ID 编号；
3. 点击 **确认**，设置立即生效；

{{ fig_indent_adjustable("../images/pc-config-software-06.png","修改舵机ID", "100%", "3.5em") }}


### 5.2 参数读取/写入

#### 5.2.1 参数配置表
<table>
  <colgroup>
    <col style="width: 200px;">
    <col style="width: 400px;">
  </colgroup>
  <thead>
    <tr>
      <th>参数</th>
      <th>描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>低压保护电压（mV）</td>
      <td>
        当舵机工作电压低于此参数设定值，<strong>自动释放锁力</strong>，无力矩输出，进入自由状态，<strong>必须重新上电</strong>，且电压恢复至正常区间。
      </td>
    </tr>
    <tr>
      <td>高压保护电压（mV）</td>
      <td>
        当舵机工作电压高于此参数设定值，<strong>自动释放锁力</strong>，无力矩输出，进入自由状态，<strong>必须重新上电</strong>，且电压恢复至正常区间。
      </td>
    </tr>
    <tr>
      <td>堵转失锁保护</td>
      <td>
        当 <strong>堵转失锁保护 = 开</strong>， 且检测到舵机当前功率超过 <strong>功率保护值</strong>，舵机会自动释放锁力，无需断电，发送停止指令即可恢复工作。
      </td>
    </tr>
    <tr>
      <td>功率保护值（mW）</td>
      <td>功率保护的阈值，超过则执行对应的 <code>堵转保护</code> 或 <code>功率保护</code>；</td>
    </tr>
    <tr>
      <td>堵转功率上限（mW）</td>
      <td>当 <strong>堵转失锁保护= 关</strong>， 且检测到舵机当前功率超过 <strong>功率保护值</strong>，舵机会降低到此设定功率运行。</td>
    </tr>
    <tr>
      <td>电流保护值（mA）</td>
      <td>当舵机工作电流超过此设定参数，<strong>自动释放锁力</strong>，作为末端安全冗余保障，电流回落至阈值以下，自动恢复工作。</td>
    </tr>
    <tr>
      <td>温度保护值（℃）</td>
      <td>当舵机工作温度超过此设定参数，<strong>强制低功率运行</strong>，限制出力，维持基础运动；当舵机温度降至设定值 - 10℃ 时，自动恢复工作。</td>
    </tr>
    <tr>
      <td>角度限制</td>
      <td>角度限制开关；开启后，角度运动受上/下限约束；关闭则不限制。</td>
    </tr>
    <tr>
      <td>角度上限（°）</td>
      <td>允许的最大角度值，超过该值将被限制在上限内。</td>
    </tr>
    <tr>
      <td>角度下限（°）</td>
      <td>允许的最小角度值，低于该值将被限制在下限内。</td>
    </tr>
    <tr>
      <td>上电缓启动</td>
      <td>上电后缓慢启动，逐步提升输出，减少冲击与抖动。</td>
    </tr>
    <tr>
      <td>上电锁力</td>
      <td>上电后自动施加锁力，用于保持当前位置。</td>
    </tr>
    <tr>
      <td>指令送出后是否响应</td>
      <td>默认 <strong>关闭</strong>，仅固定响应的指令返回数据；开启后，可配置指令也会返回响应数据。</td>
    </tr>
  </tbody>
</table>

> [!WARNING]
> - 参数修改会直接影响舵机保护与运行行为，请在安全工况下操作；
> - 不确定参数含义或范围时，建议先保留默认值或小幅度调整后验证；

> [!CAUTION]
> - **内部参数** 会直接影响舵机运动特性，非必要请勿修改。需要调整时，请先参考 xxx 文章或联系技术支持，在指导下操作。

#### 5.2.2 读取参数

1. 点击 **舵机控制**；
2. 进入 **参数** 标签页；
3. 左侧栏（灰色底色）会显示当前舵机的参数配置。

{{ fig_indent_adjustable("../images/pc-config-software-12.png","参数读取", "100%", "3.5em") }}

#### 5.2.3 写入参数

1. 点击 **舵机控制**；
2. 进入 **参数** 标签页，选中需要修改的配置项；
3. 在右侧栏将参数调整为目标数值；
4. 点击 **写入参数**，使参数生效；

{{ fig_indent_adjustable("../images/pc-config-software-13.png","写入参数", "100%", "3.5em") }}


> [!TIP]
> - 已修改的参数会以橙色背景标识，请确认无误再执行写入参数。

### 5.3 原点设定
舵机出厂已完成原点校准。如因装配或程序适配需要，可将任意位置重新设为原点。

1. 手动将舵机输出轴转到需要设为原点的位置；
2. 点击 **原点设定**；
3. 选择 **设置当前位**，点击 **确认**；

{{ fig_indent_adjustable("../images/pc-config-software-11.png","原点设定", "100%", "3.5em") }}

> [!WARNING]
> - 需重新上下电后，新设定的原点才会生效。


### 5.4 修改波特率

1. 选中需要修改的舵机；
2. 点击 **写入波特率** 按钮，在弹窗中选择希望修改的波特率选项；
3. 点击 **确认**，软件会再次自动扫描舵机，并在修改的波特率找到该舵机；

{{ fig_indent_adjustable("../images/pc-config-software-15.png","写入波特率", "100%", "3.5em") }}

### 5.5 修改 ID 扫描范围
1. 为提高扫描的效率，软件默认的ID扫描范围是 **#0-30** ；
2. 如果需要修改扫描的范围，可以进入工具/设置/修改扫描的范围；

## 6. 常见问题与处理方法

<details markdown>
<summary><strong>扫描不到舵机。</strong></summary>

- 确认转接板已接入电源，仅接 USB 无法识别；
- 确认电源电压在舵机工作范围内，过高或过低都会导致识别失败；
- 不要同时接入相同 ID 的舵机，请先分别修改为不同 ID 后再接入。
</details>


<details markdown>
<summary><strong>转接板连接串口不显示。</strong></summary>

- 若串口列表中未显示转接板的串口信息，可能驱动未正确安装。  
- 请<a href="./data/ch340.zip" download>下载ch340驱动</a>，安装后重新刷新串口列表。
</details>


<details markdown>
<summary><strong>实时控制拖动，舵机运转不顺畅。</strong></summary>

- 打开舵机 **参数配置** 选项，确认 **指令送出后是否响应** 为关闭；
- 若未关闭，请关闭后写入参数，再重试。
</details>
