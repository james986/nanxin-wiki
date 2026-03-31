# 停止模式详解及应用


<div class="fs-video-tutorial" style="position: relative; padding-top: 56.25%;">
  <video
    controls
    playsinline
    webkit-playsinline
    preload="auto"
    poster="../images/stop-mode-cover.jpg"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: #000;">
    <source src="https://fashionrobo.com/wp-content/uploads/2026/02/stop-mode.mp4" />
    当前浏览器不支持视频播放，请前往下方链接观看。
  </video>
</div>



1. 客户可以根据不同运动控制需要，选择合适的停止指令类型，具体类型详见下表。





2. 停止指令也可被用于伺服舵机在堵转保护下，恢复正常工作状态使用。





3. 当伺服舵机在失锁状态下，发送“保持锁力”指令，可使其从当前位置重建锁力。





| 停止指令类型    | 动作模式                                               |
| :-------------- | :----------------------------------------------------- |
| 失去锁力 (0x10) | 舵机立即停止运动，并释放锁力。                         |
| 保持锁力 (0x11) | 舵机立即停止运动，并维持锁力，或在无锁力状态恢复锁力。 |
| 保持阻尼 (0x12) | 舵机立即停止运动，并进入阻尼模式，外力可以调整角度。   |











### 1.1 数据包示例





设置1号舵机停止后保持锁力 功率6000mW





0x12 0x4c 0x18 0x04 0x01 0x11 0x70 0x17 0x13





to be continued
