# 规格书 - STM32多合一主控板开发板 PTC-32

<!-- 产品主图，中文taobao/英文simple-->
{% include-markdown "../../snippets/shop-info/product-primary-taobao.md"
  start="<!--start:PTC-32-->"
      end="<!--end:PTC-32-->" %}



## 1. 产品特点
- 集成 TTL / USB 转换功能
- 板载 4+2 按键
- OpenMV 专用接口


## 2. 规格参数

<table>
  <tr>
    <th width="200" align="left">参数项</th>
    <th width="400" align="left">参数值</th>
  </tr>
  <tr>
    <td>输入电压</td>
    <td>6.0-8.7v</td>
  </tr>
  <tr>
    <td>转换信号</td>
    <td>半双工转全双工</td>
  </tr>
  <tr>
    <td>TTL电平</td>
    <td>3.3v | 5.0v</td>
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
    <td>MicroUSB</td>
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
    <td>PH2.0 × 2</td>
  </tr>
  
  
</table>

## 3. 接口说明

{{ fig_center("../images/ptc-32-pin-assignment.png", "引脚定义", "500px") }}


## 4. 参考线路图

- [点击下载](../data/ptc-32-pinout.pdf){ ptc-32-pinout.pdf } 

![ptc-32-pinout](../images/ptc-32-pinout.png)
