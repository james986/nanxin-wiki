# 规格书 - TTL / RS232 转接调试板 UC-02

<!-- 产品主图，中文taobao/英文simple-->
{% include-markdown "../../snippets/shop-info/product-primary-taobao.md"
  start="<!--start:UC-02-->"
      end="<!--end:UC-02-->" %}



## 1. 产品特点
- UC-02 是一款 TTL/RS232 转换板，集成了半双工和全双工的转换功能
- 支持 5.0V 的 TTL 电平输出
- 配备了 RS232 数据接口
- 适用于总线伺服舵机与其他平台之间的通信，提高了设备的兼容性和使用便捷性

## 2. 规格参数

<table>
  <tr>
    <th width="200" align="left">参数项</th>
    <th width="400" align="left">参数值</th>
  </tr>
  <tr>
    <td>输入电压</td>
    <td>6.0-15.0V</td>
  </tr>
  <tr>
    <td>转换信号</td>
    <td>半双工转全双工</td>
  </tr>
  <tr>
    <td>TTL 电平</td>
    <td>5.0V</td>
  </tr>
  <tr>
    <td>最大承载电流</td>
    <td>20A</td>
  </tr>
  <tr>
    <td>串口输出</td>
    <td>1组</td>
  </tr>
  <tr>
    <td>数据接口</td>
    <td>RS232</td>
  </tr>
  <tr>
    <td>工作温度</td>
    <td>-10 ~ 60℃</td>
  </tr>
  <tr>
    <td>保护功能</td>
    <td>反接保护</td>
  </tr>
  <tr>
    <td>舵机接口</td>
    <td>PH2.0 × 6</td>
  </tr>
  <tr>
    <td>固定孔位</td>
    <td>M2.0 × 2</td>
  </tr>
  <tr>
    <td>电源指示灯</td>
    <td>绿色</td>
  </tr>
  <tr>
    <td>尺寸</td>
    <td>36×24mm</td>
  </tr>
  <tr>
    <td>重量</td>
    <td>5g</td>
  </tr>
  
</table>

## 3. 接口说明

{{ fig_center("../images/uc-02-pin-assignment.png", "引脚定义", "500px") }}


## 4. 参考线路图

- [点击下载](../data/uc-02-pinout.pdf){ uc-02-pinout.pdf } 

![uc-02-pinout](../images/uc-02-pinout.png)
