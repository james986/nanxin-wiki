# 舵机选型 CSV 最小字段规范（selection-value.csv）

为提升页面加载速度与前端解析效率，selection-value.csv 采用“最小字段集”并保留文件名不变（selection-value.csv）。请严格按以下表头与规则提供数据。

## 表头（推荐：自定义最小列方案 B）

按此顺序与命名输出字段（区分大小写）：

```
PRODUCT,PROTOCOL TYPE,INPUT VOLTAGE,MAX STALL TORQUE,MAX CONTINUOUS TORQUE,NO LOAD SPEED,MOTOR TYPE,REDUCTION RATIO,GEAR MATERIAL,APPEARANCE,CASE MATERIAL,DIMENSIONS,WEIGHT,link,Images
```

- PRODUCT：产品型号（如 RA8-U25H-M）
- PROTOCOL TYPE：通讯协议（UART/RS-485/CAN/PWM）
- INPUT VOLTAGE：输入电压（如 6.0-8.4v）
- MAX STALL TORQUE：堵转扭矩（如 2.45N·m (25kg-cm)）
- MAX CONTINUOUS TORQUE：动态扭矩（如 0.88N·m (9kg-cm)）
- NO LOAD SPEED：空载速度（如 51rpm (0.198sec@60°)）
- MOTOR TYPE：电机类型（Iron motor/Brushless 等）
- REDUCTION RATIO：减速比（如 273:1）
- GEAR MATERIAL：齿轮材质（如 Copper）
- APPEARANCE：外观形状（Single-shaft/Dual-shaft 等）
- CASE MATERIAL：外壳材质（如 Aluminum；未知可填 -）
- DIMENSIONS：外形尺寸（如 40×20×40mm）
- WEIGHT：重量（如 63g）
- link：产品详情页链接（可选）
- Images：缩略图 URL（仅放 1 张中小尺寸图，建议 webp）

## 填写与格式要求
- 编码：UTF-8（无 BOM）。
- 分隔：英文逗号 `,`。
- 图片：仅保留 1 张缩略图 URL，减少并发请求与首屏压力。
- 单位：
  - 扭矩统一写同一制式（N·m 或 kg-cm 二选一）；
  - 速度统一写同一制式（rpm 或 sec/60° 二选一）。
- 减速比：建议直接 `273:1`，页面会按需显示，无需 `273:01:00`。
- 允许缺省：未知字段可写 `-`。

## 与页面逻辑的对齐
页面会直接读取上述字段并渲染，无需改动前端。若保留 `Images` 仅 1 张缩略图，首屏性能最佳。

## 示例
见同目录 `data/Value.sample.csv`。
