# 规格书 - RS485/USB转接调试板 UC-05

<!-- 产品主图，中文taobao/英文simple-->
{% include-markdown "../../snippets/shop-info/product-primary-taobao.md"
  start="<!--start:UC-05-->"
      end="<!--end:UC-05-->" %}



## 1. 产品特点
- 集成了半双工和全双工的转换功能
- 支持 3.3V 与 5.0V 的电平切换
- 配备了 Type-C 数据接口
- 适用于 485 总线伺服舵机的 ID 配置、参数设置以及与 PC 和其他平台之间的通信

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
    <td>3.3V | 5.0V</td>
  </tr>
  <tr>
    <td>最大承载电流</td>
    <td>20A</td>
  </tr>
  <tr>
    <td>串口输出</td>
    <td>1 组</td>
  </tr>
  <tr>
    <td>数据接口</td>
    <td>Type-C</td>
  </tr>
  <tr>
    <td>工作温度</td>
    <td>-10 ~ 60℃</td>
  </tr>
  <tr>
    <td>舵机接口</td>
    <td>PH2.0 × 2、5264-4P × 2</td>
  </tr>
  <tr>
    <td>固定孔位</td>
    <td>M2.0 × 3</td>
  </tr>
  <tr>
    <td>电源指示灯</td>
    <td>绿色</td>
  </tr>
  <tr>
    <td>尺寸</td>
    <td>50 × 30.2mm</td>
  </tr>
  <tr>
    <td>重量</td>
    <td>12g</td>
  </tr>
</table>

## 3. 接口说明

{{ fig_center("../images/uc-05-pin-assignment.png", "引脚定义", "500px") }}


## 4. 外观尺寸

{{ fig_center("../images/uc-05-pin-cad-dimension.png", "外观尺寸图", "500px") }}

## 5. 参考线路图

- [点击下载](../data/uc-05-pinout.pdf){ uc-05-pinout.pdf } 

![uc-05-pinout](../images/uc-05-pinout.png)
