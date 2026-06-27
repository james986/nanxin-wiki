# MOSFET 选型 CSV 最小字段规范（selection-value.csv）

为提升页面加载速度与前端解析效率，selection-value.csv 采用 MOSFET 选型字段，并保留文件名不变。页面筛选方式参考 SINOPOWER LV MOSFET 列表：Package、Cfg.、BV(V)、VGS(±V) 使用勾选筛选；ID(A)、VTH(V)-typ.、RDS(on) 使用范围筛选。

## 表头

推荐按以下顺序输出字段：

```csv
PRODUCT,PACKAGE,CFG,BV,VGS,ID_TC,ID_TA,VTH_TYP,RDS_ON_10V,RDS_ON_4_5V,PRODUCT_URL,DATASHEET_URL,PACKAGE_URL,TAPE_REEL_URL,IMAGE
```

- PRODUCT：产品型号，例如 SM1401PSSC。
- PACKAGE：封装，例如 SC-70、SOT-723。
- CFG：MOSFET 配置，例如 N、P、Dual N、N+P。
- BV：击穿电压，表格标题显示为 BV(V)。
- VGS：栅源耐压，表格标题显示为 VGS(±V)。
- ID_TC：TC=25 条件下的 ID(A)。
- ID_TA：TA=25 条件下的 ID(A)。
- VTH_TYP：典型阈值电压，表格标题显示为 VTH(V)-typ.。
- RDS_ON_10V：VGS=10V 条件下的 RDS(on)，单位 mΩ MAX.。
- RDS_ON_4_5V：VGS=4.5V 条件下的 RDS(on)，单位 mΩ MAX.。
- PRODUCT_URL：产品详情页链接。
- DATASHEET_URL：规格书下载链接。
- PACKAGE_URL：封装资料链接。
- TAPE_REEL_URL：编带资料链接。
- IMAGE：预留字段，当前页面不强制显示。

## 不纳入筛选的字段

当前页面只使用上述字段作为筛选项。如果后续业务需要扩展其他参数，应先确认是否仍与参考页面的控件类型保持一致。

## 填写与格式要求

- 编码：UTF-8（无 BOM）。
- 分隔：英文逗号 `,`。
- 数值字段建议只填写数值，不重复单位；单位已经在表格标题中表达。
- P-Channel 参数可以保留负号，例如 BV=-20、ID_TA=-3.3。
- 未知字段可留空，页面会显示为 `-`。

## 示例

见同目录 `data/selection-value.csv`。
