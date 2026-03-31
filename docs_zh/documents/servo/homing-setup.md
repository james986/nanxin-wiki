# 原点设置详解及应用



<div class="fs-video-tutorial" style="position: relative; padding-top: 56.25%;">
  <video
    controls
    playsinline
    webkit-playsinline
    preload="auto"
    poster="../images/homing-setup-cover.jpg"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: #000;">
    <source src="https://fashionrobo.com/wp-content/uploads/2026/02/homing-setup.mp4" />
    当前浏览器不支持视频播放，请前往下方链接观看。
  </video>
</div>


## 1. 原点设置详解





在舵机处于**锁力释放**的状态下，通过上位机或指定指令，可将当前舵机的角度重置为零位，便于装配后的零位校准，同时为算法提供后续动作的起始角度。





## 2. 数据包示例





设置1号舵机当前角度为原点





| **指令示例** | **0x12 0x4c 0x17 0x02 0x01 0x00 0x78** |
| ------------ | -------------------------------------- |
| **包头**     | 0x12 0x4c                              |
| **指令编号** | 0x17                                   |
| **内容长度** | 0x02                                   |
| **舵机ID**   | 0x01                                   |
| **预设值**   | 0x00                                   |
| **校验和**   | 0x78                                   |





<iframe src="https://player.bilibili.com/player.html?bvid=BV1FEEyz9Edn&as_wide=1&v=0" width="100%" height="500" frameborder="0" scrolling="no" allowfullscreen></iframe>
