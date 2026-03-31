# 产品规格书 - RA8-U25H-M

<!-- 分割线+PDF文件下载图标，用宏调用（路径/鼠标悬浮显示名称/48px不要动） -->
{{ pdf_line("../pdf/Fashion-Star-RA8-U25H-M.pdf", "下载规格书", "48px") }}


<!-- 产品主图，中文taobao/英文simple-->
{% include-markdown "../../../snippets/shop-info/product-primary-taobao.md"
  start="<!--start:RA8-U25H-M-->"
      end="<!--end:RA8-U25H-M-->" %}

<!-- ##1.产品特点，不同马达类型引用不同段落 -->
{% include-markdown "../../../snippets/datasheet/datasheet-snippets.md"
  start="<!--start:spec-01-cored-->"
      end="<!--end:spec-01-cored-->" %}



<!-- ##2.型号定义 -->
{% include-markdown "../../../snippets/datasheet/datasheet-snippets.md"
  start="<!--start:spec-02-->"
      end="<!--end:spec-02-->" %}


<!-- ##3.规格参数（全部手工填写） -->
## 3. 规格参数
### 3.1 基础参数
<table>
  <tr>
    <th width="200" align="left">参数项</th>
    <th width="400" align="left">参数值</th>
  </tr>
  <tr>
    <td>工作电压</td>
    <td>9.0～12.6 V</td>
  </tr>


  <tr>
    <td>马达类型</td>
    <td>铁芯马达</td>
  </tr>
  <tr>
    <td>位置传感器</td>
    <td>12-bit 非接触式绝对值编码器（磁编码）</td>
  </tr>
  <tr>
    <td>分辨率</td>
    <td>2048 阶 / 360°（0.176°）</td>
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
    <td>全金属铜铝组合</td>
  </tr>
  <tr>
    <td>输出齿规格</td>
    <td>铜 / Ø6 mm / 25T</td>
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
    <td>40 × 20 × 40 mm / 63 g</td>
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

### 3.2 特性参数（@12V）
<table>
  <tr>
    <th width="200" align="left">参数项</th>
    <th width="400" align="left">参数值</th>
  </tr>
  <tr>
    <td>静态堵转扭矩</td>
    <td>2.45 N·m（25kg·cm）</td>
  </tr>
  <tr>
    <td>最大动态扭矩</td>
    <td>0.88 N·m（9kg·cm）</td>
  </tr>
  <tr>
    <td>额定扭矩</td>
    <td>0.44 N·m（3.4kg·cm）</td>
  </tr>
  <tr>
    <td>空载转速</td>
    <td>51 rpm（0.198 s / 60°）</td>
  </tr>
  <tr>
    <td>额定转速</td>
    <td>18 rpm（0.556 s / 60°）</td>
  </tr>
  <tr>
    <td>峰值电流</td>
    <td>3 A</td>
  </tr>
  <tr>
    <td>空载电流</td>
    <td>＜200 mA</td>
  </tr>
  <tr>
    <td>待机电流</td>
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

<!-- 两张特性曲线图，用宏加载（路径/标题/大小500px不要动）-->
{{ fig_center("../images/U25H-torque-speed-curve.png", "T-N 特性曲线", "500px") }}

{{ fig_center("../images/U25H-mechanical-overload-curve.png", "机械过载曲线", "500px") }}





<!-- ##3.规格参数（没有include，按照模版填入） -->
## 4. 外观尺寸与安装

**文件下载：**
[PDF](../cad-files/data/ra8-rp8-rx8-series-dimension.pdf){ ra8-rp8-rx8-series-dimension.pdf } ｜ 
[STEP](../cad-files/data/ra8-rp8-rx8-series-3D.STEP.zip){ ra8-rp8-rx8-series-3D.STEP.zip } ｜ 
[DWG](../cad-files/data/ra8-rp8-rx8-series-dimension.dwg.zip){ ra8-rp8-rx8-series-dimension.dwg.zip }｜ 
[更多配件图纸](../../parts/index.md)

![ra8-rp8-rx8-series-dimension](../cad-files/data/ra8-rp8-rx8-series-dimension.jpg)

![ra8-rp8-rx8-series-installation](../cad-files/data/ra8-rp8-rx8-series-installation.png)



<!-- ##5.接口与连线 -->
{% include-markdown "../../../snippets/datasheet/datasheet-snippets.md"
  start="<!--start:spec-05-ph20-3pin-->"
      end="<!--end:spec-05-ph20-3pin-->" %}




<!-- ##6.开发环境与SDK -->
{% include-markdown "../../../snippets/datasheet/datasheet-snippets.md"
  start="<!--start:spec-06-uart-->"
      end="<!--end:spec-06-uart-->" %}

<!-- ##7-10.开发环境与SDK/保护功能/指令与协议/运动控制/参数设置与升级 -->
{% include-markdown "../../../snippets/datasheet/datasheet-snippets.md"
  start="<!--start:spec-07/10-->"
      end="<!--end:spec-07/10-->" %}
