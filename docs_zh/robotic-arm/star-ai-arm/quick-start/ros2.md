# StarAI Arm 机械臂 ROS2 MoveIt2 使用教程

<div align="center">
  <div style="display: flex; gap: 1rem; justify-content: center; align-items: center;" >
    <img
      src="../images/viola_and_violin.jpg"
      alt="SO-101 follower arm"
      title="SO-101 follower arm"
      style="width: 80%;"
    />
    <img
      src="../images/cello.jpg"
      alt="SO-101 leader arm"
      title="SO-101 leader arm"
      style="width: 80%;"
    />
  </div>
</div>


## 1. 环境依赖

- Ubuntu 22.04.5 LTS（Jammy）
- ROS2 Humble

### 1.1 安装 ROS2 Humble

[ROS2 Humble 安装指南](https://wiki.seeedstudio.com/cn/install_ros2_humble/)

[ROS2 Humble Installation](https://wiki.seeedstudio.com/install_ros2_humble/)

### 1.2 安装 MoveIt2

```bash
sudo apt install ros-humble-moveit*
```

### 1.3 安装舵机 SDK 库

```bash
sudo pip install pyserial
sudo pip install fashionstar-uart-sdk
```

### 1.4 克隆 star-arm-moveit2 功能包

```bash
cd ~/
git clone https://github.com/servodevelop/star-arm-moveit2.git
cd ~/star-arm-moveit2
colcon build
echo "source ~/star-arm-moveit2/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

<video controls style="width:100%; max-width:900px;">
  <source src="../images/stararm.mp4" type="video/mp4">
</video>


## 2. MoveIt2

### 2.1 使用虚拟机械臂

本模式仅启动 MoveIt2 的仿真规划环境，不连接真实硬件。可用于验证关节运动、路径规划与末端位姿交互流程。

默认使用 **Viola**，请执行：

```bash
ros2 launch viola_moveit_config demo.launch.py 
```
<!-- markdownlint-disable MD033 -->

如需切换到 **Cello**，请展开下方对应指令：

<details>

<summary>Cello</summary>

```bash
ros2 launch cello_moveit_config demo.launch.py 
```

</details>

### 2.2 使用真实机械臂（连接硬件）

本模式会连接真实机械臂并执行实机控制流程。请先确认机械臂已正确供电、通信正常，并保证周围空间安全。

**终端 1：启动硬件驱动（机械臂将回到零位）**

默认使用 **Viola**，请执行：

```bash
ros2 launch viola_moveit_config driver.launch.py
```

如需切换到 **Cello**，请展开下方对应指令：

<details>

<summary>Cello</summary>

```bash
ros2 launch cello_moveit_config driver.launch.py
```

</details>

**终端 2：启动 MoveIt2 实机控制界面**

默认使用 **Viola**，请执行：

```bash
ros2 launch viola_moveit_config actual_robot_demo.launch.py
```

如需切换到 **Cello**，请展开下方对应指令：

<details>

<summary>Cello</summary>

```bash
ros2 launch cello_moveit_config actual_robot_demo.launch.py
```

</details>

完成上述两步后，即可通过 MoveIt2 界面对真实机械臂进行联动控制。

---


以下 **终端 3 / 终端 4** 为按需步骤，仅在需要进行末端位姿读写或话题发送测试时执行。

**末端位姿读写示例（可选）**

**终端 3：启动末端位姿读写示例**

默认使用 **Viola**，请执行：

```bash
ros2 launch viola_moveit_config moveit_write_read.launch.py
```

如需切换到 **Cello**，请展开下方对应指令：

<details>

<summary>Cello</summary>

```bash
ros2 launch cello_moveit_config moveit_write_read.launch.py
```

</details>

**位姿话题发送节点示例（可选）**

请修改文件：

```text
src/arm_moveit_write/src/topic_publisher.cpp
```

```cpp
    // viola
    // dataset1_ = {
    //   {0.35, -0.00, 0.23},       // position
    //   {-0.499, 0.500, -0.500, 0.500}, // orientation
    //   "open"                         // gripper_state
    // };
    // dataset2_ = {
    //   {0.15, -0.00, 0.299},        // position
    //   {0.500, -0.500, 0.500, -0.499},   // orientation
    //   "close"                        // gripper_state
    // };

    // cello
    dataset1_ = {
      {0.278, 0.000, 0.438},       // position
      {-0.506, 0.507, -0.496, 0.491}, // orientation
      "open"                         // gripper_state
    };
    dataset2_ = {
      {0.479, -0.000, 0.369},        // position
      {-0.506, 0.507, -0.496, 0.491}, // orientation
      "close"                        // gripper_state
    };

```

仅在需要发布自定义位姿话题时执行终端 4。

**终端 4：启动位姿话题发送节点**

```bash
colcon build
source install/setup.sh
ros2 run arm_moveit_write topic_publisher 
```

## 3. MoveIt2 Gazebo 仿真机械臂

> [!TIP]
>
> 关闭 Gazebo 图形界面后，建议在终端执行 `pkill -9 -f gazebo` 指令，确保相关进程完全退出。
> 运行示例前，请先关闭其他正在运行的节点。

安装 Gazebo：

```bash
sudo apt install gazebo
sudo apt install ros-humble-moveit*
```

**终端 1：启动 Gazebo 图形界面**

默认使用 **Viola**，请执行：

```bash
ros2 launch viola_gazebo viola_gazebo.launch.py
```

如需切换到 **Cello**，请展开下方对应指令：

<details>

<summary>Cello</summary>

```bash
ros2 launch cello_gazebo cello_gazebo.launch.py
```

</details>

**终端 2：启动 MoveIt2 界面**

默认使用 **Viola**，请执行：

```bash
ros2 launch viola_moveit_config gazebo_demo.launch.py
```

如需切换到 **Cello**，请展开下方对应指令：

<details>

<summary>Cello</summary>

```bash
ros2 launch cello_moveit_config gazebo_demo.launch.py
```

</details>

## 4. 机械臂示教模式

> [!TIP]
> 需要重新录制轨迹时，可删除 `record-test` 文件夹，或改用新的数据集名称（如 `record-test1`）。

**终端 1：启动手臂硬件驱动（示教模式）**

```bash
ros2 run robo_driver driver --ros-args -p lock:='disable'
```

**终端 2：记录手臂轨迹**

按下回车开始录制，再按下回车结束录制。可通过 `dataset` 参数指定保存路径。

```bash
ros2 run ros2_bag_recorder bag_recorder --ros-args -p dataset:=star/record-test
```

**终端 3：重播运行轨迹**

```bash
ros2 bag play ./star/record-test
```

## 5. FAQ

如果 RViz2 界面出现频闪，可尝试执行以下指令：

  ```bash
  export QT_AUTO_SCREEN_SCALE_FACTOR=0
  ```
<!-- markdownlint-enable MD033 -->
