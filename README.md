# GuYueTutorial

ROS 2 Humble 学习练习代码，跟随古月居的 [ROS 2 入门 21 讲](https://github.com/guyuehome/ros2_21_tutorials) 边学边写。

每个文件夹是一个 ROS 2 包。环境：Ubuntu 22.04 + ROS 2 Humble（Docker）。

## 使用

```bash
mkdir -p ~/guyue_ws && cd ~/guyue_ws
git clone https://github.com/liuchenxu-uppsala/GuYueTutorial.git src
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

`learning_interface`（自定义 msg / srv / action）来自古月居原仓库。
