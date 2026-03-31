# 总线舵机连线及电源解决方案

基于客户实际使用环境，按舵机使用数量分为以下三种场景：

- [常规场景应用（1-6 颗）](#wiring-1-6)
- [复杂场景应用（7-14 颗）](#wiring-7-14)
- [大规模场景应用（15 颗及以上）](#wiring-15-plus)



<a id="wiring-1-6"></a>

## 常规场景应用（1-6 颗）

- 适用于单套系统、轻负载工况使用 1-6 颗舵机的常规应用场景。
- 在转接板带载能力、线材压降和连接端子损耗允许的前提下，可灵活选择串联、并联或串并结合的接线方式。
- 若为重载工况（如100kg大扭矩舵机应用），应根据实际总工作电流减少带载数量。

> [!CAUTION]
> 通过单个 UC-01 转接板的总工作电流，不得高于 20A。

### 串联

{{ fig_indent_adjustable("../../images/serial-connection.jpg","串联", "100%", "3.5em") }}

### 并联

{{ fig_indent_adjustable("../../images/parallel-connection.jpg","并联", "100%", "3.5em") }}



<a id="wiring-7-14"></a>

## 复杂场景应用（7-14 颗）

- 适用于单套系统使用 7-14 颗舵机的应用场景。
- 当舵机数量增加后，应重点关注单颗舵机功率需求、长距离布线压降以及数据线缆载流能力。
- 推荐使用分线板进行电源转接，并由独立主供电回路为分线板供电，以降低线路损耗并提升供电稳定性。
- 可直接使用配套分线板，也可根据项目需求自行设计适配的分线板电路。
- 推荐单路回路内串联挂载的舵机数量不超过 6 颗（大扭矩负载则相应减少）

<style>
.md-typeset .wiring-product-grid {
  display: grid;
  grid-template-columns: minmax(0, 220px);
  justify-content: center;
  margin: 1rem 0;
}

.md-typeset .wiring-product-card {
  display: block;
  color: inherit;
  text-decoration: none;
  background: var(--md-default-bg-color);
  border: 1px solid var(--fs-divider);
  border-radius: 10px;
  padding: 10px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}

.md-typeset .wiring-product-card:hover {
  border-color: var(--fs-accent);
}

.md-typeset .wiring-product-card img {
  width: 100% !important;
  max-width: 100% !important;
  height: auto;
  display: block;
  margin: 0 auto !important;
}

.md-typeset .wiring-product-label {
  display: inline-block;
  margin-top: 6px;
  font-size: 14px;
  font-weight: 600;
}
</style>

<div class="wiring-product-grid">
  <a class="wiring-product-card" href="../../../parts/boards/datasheet-ph8">
    <img src="../../../snippets/shop-info/images/ph8-primary.webp" alt="PH8">
    <span class="wiring-product-label">UART串行总线舵机分线板<br>PH8</span>
  </a>
</div>

### 推荐接线方案

{{ fig_indent_adjustable("../../images/wiring-2.png","", "100%", "3.5em") }}



<a id="wiring-15-plus"></a>

## 大规模场景应用（15 颗及以上）

- 适用于单套系统使用 15 颗及以上舵机的大规模应用场景。
- 在该档位下，建议通过多块分线板进行分组供电与分线管理，避免单一路径负载过高。
- 分线板之间，以及分线板与 UC-01 转接板之间，仅需连接信号线（S）与电源负极（-，GND）。
- 转接板与主控单元完成通信连接后，即可实现对全链路舵机的统一控制。
- 具体接线方式可参考下方示意图与视频演示。

### 接线示意图

{{ fig_indent_adjustable("../../images/wiring-3.png","", "100%", "3.5em") }}



{{ fig_indent_adjustable("../../images/wiring-4.png","", "100%", "3.5em") }}

### 数据线改装说明
配套的数据线，可以参考如方法改装，用于分线板之间，以及分线板和 UC-01 转接板之间的连线使用。

<table style="width: 100%; table-layout: fixed;">
  <thead>
    <tr>
      <th style="text-align: center;">线修改前</th>
      <th style="text-align: center;">线修改后</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center; vertical-align: middle; padding: 12px;">
        <img src="../../images/wire-before.png" alt="线修改前" style="width: 320px; max-width: 100%; height: auto; display: inline-block;">
      </td>
      <td style="text-align: center; vertical-align: middle; padding: 12px;">
        <img src="../../images/wire-after.png" alt="线修改后" style="width: 320px; max-width: 100%; height: auto; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

### 接线视频演示
<div class="fs-video-tutorial" style="position: relative; padding-top: 56.25%;">
  <video
    controls
    playsinline
    webkit-playsinline
    preload="auto"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: #000;">
    <source src="https://fashionrobo.com/wp-content/uploads/2026/03/multi-servo-daisy-chain.mp4" />
    当前浏览器不支持视频播放，请前往下方链接观看。
  </video>
</div>

> [!TIP]
> - 若视频无法加载，请前往 **[B站观看](https://b23.tv/4PlYopf)**。



## 注意事项
> [!WARNING]
> - 相邻两台舵机间的级联通信线路长度**最大限值为 1m**；若线路长度超出 1m，必须采用屏蔽线缆，降低信号传输干扰与衰减风险。
> - 受连接端子、供电线缆的固有阻抗影响，大电流工况下会产生线路压降损耗；实际设计需结合具体应用场景完成校验，以系统全工况运行下的**实测电压值**为最终判定依据。
