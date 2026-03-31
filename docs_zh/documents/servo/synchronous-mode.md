# 同步模式详解及应用


<div class="fs-video-tutorial" style="position: relative; padding-top: 56.25%;">
  <video
    controls
    playsinline
    webkit-playsinline
    preload="auto"
    poster="../images/synchronous-mode-cover.jpg"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: #000;">
    <source src="https://fashionrobo.com/wp-content/uploads/2026/02/synchronous-mode.mp4" />
    当前浏览器不支持视频播放，请前往下方链接观看。
  </video>
</div>



1.1  单条指令同时包含多个伺服舵机的控制指令，适用于多个舵机协同动作的场景。





1.2  每个伺服舵机通过唯一的 ID 与指令内容中的参数进行匹配，仅解析并响应与自身ID 相关的控制信息。





1.3  所有伺服舵机接收完指令后，将同时开始执行各自的指令，实现同步动作效果





| **指令示例**         | **0x12 0x4c 0x19 0x11 0x08 0x07 0x02 0x01 0x2c 0x01 0xe8 0x03 0x00** **0x00 0x02 0x58 0x02 0xd0 0x07 0x00 0x00 0xE5** |
| -------------------- | ------------------------------------------------------------ |
| **包头**             | 0x12 0x4c                                                    |
| **指令编号**         | 0x19                                                         |
| **内容长度**         | 0x11                                                         |
| **同步数据监控指令** | 0x08                                                         |
| **舵机总数**         | 0x02                                                         |
| **舵机1编号**        | 0x01                                                         |
| **舵机1角度**        | 0x2c 0x01                                                    |
| **舵机1时间**        | 0xE8 0x03                                                    |
| **舵机1功率**        | 0x00 0x00                                                    |
| **舵机2编号**        | 0x02                                                         |
| **舵机2角度**        | 0x58 0x02                                                    |
| **舵机2时间**        | 0xD0 0x07                                                    |
| **舵机2功率**        | 0x00 0x00                                                    |
| **校验和**           | 0xE5                                                         |
|                      |                                                              |





如还需增加舵机，继续在舵机2后面增加即可。





to be continued