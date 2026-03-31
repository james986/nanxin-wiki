# StarAI Arm - CAD 图纸与周边模型下载

---

> [!TIP]
> - 建议使用 SolidWorks 2021 及以上版本打开模型。
> - 图中尺寸仅供参考，请以实物为准；如差异较大，请联系我们确认。

<style>
.cad-download-inline { display: inline; }
.cad-download-block { display: none; }
.cad-download-block span { display: block; margin: 2px 0; }
.cad-files-table { width: 100%; }

.md-typeset .cad-files-table {
  width: 100% !important;
  display: table !important;
  border-collapse: collapse !important;
  border: 0.5px solid var(--fs-divider) !important;
  font-size: 14px !important;
}

.md-typeset .cad-files-table th,
.md-typeset .cad-files-table td {
  padding: 10px 16px !important;
  border: 0.5px solid var(--fs-divider) !important;
  line-height: 1.4 !important;
  vertical-align: middle !important;
}

.md-typeset .cad-files-table th {
  background-color: var(--fs-table-header-bg) !important;
  font-weight: 600 !important;
  text-align: center !important;
}

.md-typeset .cad-files-table tr:nth-child(even) {
  background-color: rgba(0, 0, 0, 0.012) !important;
}
[data-md-color-scheme="slate"] .md-typeset .cad-files-table tr:nth-child(even) {
  background-color: rgba(255, 255, 255, 0.02) !important;
}

.cad-thumb img {
  width: 110px;
  height: auto;
  display: block;
  margin: 0 auto;
  padding: 0;
}

@media (min-width: 900px) {
  .cad-files-table {
    table-layout: fixed;
    width: 100%;
  }
  .cad-files-table th:nth-child(2),
  .cad-files-table td:nth-child(2) {
    width: 160px;
  }
  .cad-files-table th:nth-child(3),
  .cad-files-table td:nth-child(3) {
    width: 320px;
  }
}

@media (max-width: 640px) {
  .cad-download-inline { display: none; }
  .cad-download-block { display: block; }
}
</style>

## StarAI Arm 系列

<table class="cad-files-table" cellpadding="0" cellspacing="0">
  <tr>
    <th width="110" align="center">外观</th>
    <th width="140" align="center">型号</th>
    <th align="center">下载</th>
  </tr>
  <tr>
    <td align="center">
      <div class="cad-thumb"><img src="./images/cello-primary.webp" alt="Cello"></div>
    </td>
    <td align="center"><strong><a href="../datasheet/cello/">Cello（遥操臂）</a></strong></td>
    <td align="center">
      <span class="cad-download-inline"><a href="./data/cello-dimension.pdf" download>PDF</a> ｜ <a href="./data/cello-dimension.dwg" download>DWG</a></span>
      <span class="cad-download-block">
        <span><a href="./data/cello-dimension.pdf" download>PDF</a></span>
        <span><a href="./data/cello-dimension.dwg" download>DWG</a></span>
      </span>
    </td>
  </tr>
  <tr>
    <td align="center">
      <div class="cad-thumb"><img src="./images/viola-primary.webp" alt="Viola"></div>
    </td>
    <td align="center"><strong><a href="../datasheet/viola/">Viola（遥操臂）</a></strong></td>
    <td align="center">
      <span class="cad-download-inline"><a href="./data/viola-dimension.pdf" download>PDF</a> ｜ <a href="./data/viola-dimension.dwg" download>DWG</a></span>
      <span class="cad-download-block">
        <span><a href="./data/viola-dimension.pdf" download>PDF</a></span>
        <span><a href="./data/viola-dimension.dwg" download>DWG</a></span>
      </span>
    </td>
  </tr>
  <tr>
    <td align="center">
      <div class="cad-thumb"><img src="./images/violin-primary.webp" alt="Violin"></div>
    </td>
    <td align="center"><strong><a href="../datasheet/violin/">Violin（跟随臂）</a></strong></td>
    <td align="center">
      <span class="cad-download-inline"><a href="./data/violin-dimension.pdf" download>PDF</a> ｜ <a href="./data/violin-dimension.dwg" download>DWG</a></span>
      <span class="cad-download-block">
        <span><a href="./data/violin-dimension.pdf" download>PDF</a></span>
        <span><a href="./data/violin-dimension.dwg" download>DWG</a></span>
      </span>
    </td>
  </tr>
</table>

## 周边配件

- **[平行夹爪](../quick-start/cello-violin.md)**

    适用于机械臂末端抓取任务，支持常见物体的稳定夹持与抓取验证。

- **[L 型宽幅指尖替换件](../quick-start/cello-violin.md)**

    用于扩展夹爪接触面积，适配大尺寸或异形目标的抓取场景。

## URDF模型

- **[Cello](../quick-start/ros2.md)**

    提供 Cello（遥操臂）的 URDF 模型与 ROS2/MoveIt2 集成参考。

- **[Viola](../quick-start/ros2.md)**

    提供 Viola（遥操臂）的 URDF 模型与 ROS2/MoveIt2 集成参考。
