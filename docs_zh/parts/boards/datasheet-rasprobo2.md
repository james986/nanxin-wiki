# 规格书 - 树莓派总线舵机扩展板 Rasprobo2

<!-- 产品主图，中文taobao/英文simple-->
{% include-markdown "../../snippets/shop-info/product-primary-taobao.md"
  start="<!--start:Rasprobo2-->"
      end="<!--end:Rasprobo2-->" %}



## 1. 产品特点
- 直接兼容树莓派，无需其他连线
- 集成 UART 串行总线舵机接口
- 集成全双工/半双工舵机信号转换
- 集成 USB/TTL 转换，支持 UART 舵机调试软件
- 集成气泵和电磁阀控制电路，方便机械手臂设计
- 集成惯性导航模块（IMU）
- 支持机器人自平衡及高级姿态算法
- 集成电源管理，可直接给树莓派供电
- 集成摄像头补光灯控制（GPIO4）
- 集成 I2C｜数字｜按键 三种接口
- 支持低压报警

## 2. 规格参数

<table>
  <tr>
    <th width="200" align="left">参数项</th>
    <th width="400" align="left">参数值</th>
  </tr>
  <tr>
    <td>电源接口</td>
    <td>6.0-8.4V</td>
  </tr>
  <tr>
    <td>电源开关</td>
    <td>电源 ON/OFF</td>
  </tr>
  <tr>
    <td>I2C 接口</td>
    <td rowspan="3">树莓派功能引出接口，兼容 Grove 接口定义</td>
  </tr>
  <tr>
    <td>5.0V扩展口</td>
  </tr>
  <tr>
    <td>3.3V扩展口</td>
  </tr>
  <tr>
    <td>补光灯接口</td>
    <td>集成补光灯控制电路，用于摄像头补光</td>
  </tr>
  <tr>
    <td>舵机接口</td>
    <td>CH1-CH6，连接UART串行总线舵机</td>
  </tr>
  <tr>
    <td>功能按键</td>
    <td>扩展按键，可自定义功能</td>
  </tr>
  <tr>
    <td>惯性导航模块</td>
    <td>IMU（MPU6050），支持机器人自平衡及高级姿态算法</td>
  </tr>
  <tr>
    <td>Micro USB</td>
    <td>连接PC进行上位机调试及控制</td>
  </tr>
  <tr>
    <td>SW 接口</td>
    <td>连接电磁阀</td>
  </tr>
  <tr>
    <td>MT接口</td>
    <td>连接气泵马达</td>
  </tr>
  <tr>
    <td>蜂鸣器</td>
    <td>低压报警</td>
  </tr>
  <tr>
    <td>电源指示灯</td>
    <td>上电后常亮</td>
  </tr>
  <tr>
    <td>状态指示灯</td>
    <td>电压正常-常亮；低电压-闪烁</td>
  </tr>
  
</table>

## 3. 接口说明

{{ fig_center("../images/rasprobo2-pin-assignment.png", "引脚定义", "500px") }}


## 4. 参考线路图

- [点击下载](../data/rasprobo2-pinout.pdf){ rasprobo2-pinout.pdf } 

![rasprobo2-pinout](../images/rasprobo2-pinout.png)
