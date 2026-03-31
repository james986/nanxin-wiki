# 规格书 - TTL / RS485 转接调试板 UC-04

<!-- 产品主图，中文taobao/英文simple-->
{% include-markdown "../../snippets/shop-info/product-primary-taobao.md"
  start="<!--start:UC-04-->"
      end="<!--end:UC-04-->" %}



## 1. 产品特点
- UC-04 是一款总线伺服舵机的 RS485 转换板
- 集成了 RS485 和半双工转换，以及稳压器线路等功能
- 可用于总线伺服舵机和 PLC 及其他平台之间的通讯

## 2. 规格参数

<table>
  <tr>
    <th width="200" align="left">参数项</th>
    <th width="400" align="left">参数值</th>
  </tr>
  <tr>
    <td>输入电压</td>
    <td>6.0-18.4V</td>
  </tr>
  <tr>
    <td>转换信号</td>
    <td>485转半双工</td>
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
    <td>15EDG-3.81 mm</td>
  </tr>
  <tr>
    <td>工作温度</td>
    <td>-10 ~ 60℃</td>
  </tr>
  <tr>
    <td>保护功能</td>
    <td>50A保险丝</td>
  </tr>
  <tr>
    <td>舵机接口</td>
    <td>PH2.0 × 2</td>
  </tr>
  <tr>
    <td>固定孔位</td>
    <td>M2.0 × 4</td>
  </tr>
  <tr>
    <td>电源指示灯</td>
    <td>绿色</td>
  </tr>
  <tr>
    <td>尺寸</td>
    <td>36×36mm</td>
  </tr>
  <tr>
    <td>重量</td>
    <td>17.2g</td>
  </tr>
  
</table>

## 3. 接口说明

{{ fig_center("../images/uc-04-pin-assignment.png", "引脚定义", "500px") }}
{{ fig_center("../images/uc-04-pin-plc-assignment.png", "西门子S7-1200 PLC接线图", "500px") }}

## 4. 外观尺寸

{{ fig_center("../images/uc-04-pin-cad-dimension.png", "外观尺寸图", "500px") }}

## 5. 参考线路图

- [点击下载](../data/uc-04-pinout.pdf){ uc-04-pinout.pdf } 

![uc-04-pinout](../images/uc-04-pinout.png)
