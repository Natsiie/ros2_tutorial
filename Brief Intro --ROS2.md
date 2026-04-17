# Brief Intro --ROS2

## subject first -- install ROS2

https://blog.csdn.net/jianlai_/article/details/123545130?ops_request_misc=elastic_search_misc&request_id=fd4b24925bf762befd8c11f40cf83a8e&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-123545130-null-null.142^v102^pc_search_result_base4&utm_term=%E9%B1%BC%E5%90%B9&spm=1018.2226.3001.4187|

**ros2版本选择为humble**

（小乌龟测试）

```c
ros2 pkg executables turtlesim		
```

终端一：

```c
ros2 run turtlesim turtlesim_node		
```

终端二：

```c
ros2 run turtlesim turtle_teleop_key
```



配置环境：

QQ

vscode + 插件库（汉化，ros拓展 ctrl+p ; ext install ms-iot.vscode-ros,cmake_tools）

git库（sudo installl apt git）



## why?



###  The UAV

#### <img src="/home/lulu/文档/rc导航参考资料/ego-planner/pictures/title.gif" alt="title" style="zoom: 200%;" />



![sim_demo](/home/lulu/文档/rc导航参考资料/ego-planner/pictures/sim_demo.gif)



<img src="/home/lulu/文档/rc导航参考资料/ego-planner/pictures/outdoor.gif" alt="outdoor" style="zoom: 200%;" />



<img src="/home/lulu/文档/rc导航参考资料/ego-planner/pictures/indoor.gif" alt="indoor" style="zoom:200%;" />

### **quadruped robot**（四足机器人）

https://www.bilibili.com/video/BV1MrqzBEET8/?spm_id_from=333.1387.homepage.video_card.click&vd_source=74d17ae72c31a281ba10b070b597d5c6



https://www.bilibili.com/video/BV1nVXPByEvd/?spm_id_from=333.337.search-card.all.click&vd_source=74d17ae72c31a281ba10b070b597d5c6



https://www.bilibili.com/video/BV12JxuzDErs?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2479604-9kkcc.1775230497754.452&vd_source=74d17ae72c31a281ba10b070b597d5c6

//四足自主导航探索



### The Sentry(robomaster 的哨兵)

https://www.bilibili.com/video/BV1cXoEYzEd6/?spm_id_from=333.1387.homepage.video_card.click&vd_source=74d17ae72c31a281ba10b070b597d5c6

//SCURM



https://www.bilibili.com/video/BV1zSH5eHEK2/?spm_id_from=333.337.search-card.all.click&vd_source=74d17ae72c31a281ba10b070b597d5c6

//哨兵仿真





### **humanoid robot**(人型机器人)

https://www.bilibili.com/video/BV1qrbrzqE7c?spm_id_from=333.788.recommend_more_video.-1&trackid=web_related_0.router-related-2479604-s7xkd.1775230761651.431&vd_source=74d17ae72c31a281ba10b070b597d5c6

//运动模拟

https://www.bilibili.com/video/BV1nbsdzMEoz?spm_id_from=333.788.recommend_more_video.-1&trackid=web_related_0.router-related-2479604-fc7wt.1775231121956.177&vd_source=74d17ae72c31a281ba10b070b597d5c6

//“机乐净土”



### 毕设

https://www.bilibili.com/video/BV1WUcgzWE8n/?spm_id_from=333.1387.homepage.video_card.click&vd_source=74d17ae72c31a281ba10b070b597d5c6







## How to Re-implement the project  above?



###  SLAM 

**--- S ( Simultaneous) 同时的**

**--- L（Localization）定位**

**--- A （And）**

**--- M  (Mapping)建图**



**--- 同时定位与地图构建**



--- 普通建图：

#在这里加一个雷达实时扫图演示



--- 彩色建图 ：

https://www.bilibili.com/video/BV1Ezxge7EEi/?vd_source=74d17ae72c31a281ba10b070b597d5c6

//港大 fast_livo2

![截图 2026-01-31 11-15-45](/home/lulu/图片/截图/截图 2026-01-31 11-15-45.png)

--- 有什么用？

![输入图片说明](https://foruda.gitee.com/images/1762334522335989547/5d969618_506465.png)



![输入图片说明](https://foruda.gitee.com/images/1762334566135971259/f7f68883_506465.png)

（可用于3d游戏里面的真实场景复刻）

### 仿真模拟

//Pb_simulation

![2024.5.11RMUL动态避障2](/home/lulu/pb_rmsimulation/.docs/2024.5.11RMUL动态避障2.gif)

//插播ego_planner_swarm仿真演示









### 强化学习（BTW： 很吃电脑配置！！！Check if you are satisfied the requirement:

https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html；实在想玩可以租云端服务器：教程link

https://www.bilibili.com/video/BV1fTwvzHEBw/?spm_id_from=333.337.search-card.all.click&vd_source=74d17ae72c31a281ba10b070b597d5c6

）



https://www.bilibili.com/video/BV1iG4y1d7i3/?spm_id_from=333.337.search-card.all.click&vd_source=74d17ae72c31a281ba10b070b597d5c6

(Issac Gym 里的四足训练展示)









## What is ROS2





![feb9ce3a793aa9c2856c447714fa4b52](/home/lulu/图片/feb9ce3a793aa9c2856c447714fa4b52.png)







<img src="/home/lulu/下载/ROS 2 架构总览.png" alt="ROS 2 架构总览" style="zoom:80%;" />







## What is our Project Assignment?



--- Must Do:

​	1.过一边ros2教程：

​	Gundasmart：https://space.bilibili.com/687639149/lists/1972553?type=season

​	赵虚左：https://www.bilibili.com/video/BV1VB4y137ys?spm_id_from=333.788.videopod.sections&vd_source=74d17ae72c31a281ba10b070b597d5c6

（要求：知道最起码的一个ros2文件执行流程是怎么走的 ，多个ros2文件怎么同时启动）

​	2.复现fast_lio2,完成扫图，定位功能。（暑假之后回来小组之后轮着使用，小组只有两个mid_360...）

--- **challenge**：

​	暑假：(如果你感兴趣)复现pb_simulation的仿真项目  ————完整经历一遍slam流程，从建图，定位，到实时全自动地形探索

​	8-10月份：和电控配合，完成雷达小车全自动自主导航探索的实机部署





## How to learn

--- learn through the " **Training**"（NO）



**--- through the video (self - taught)**

**--- try to reproduce the github project you are interested**

**--- Be free to use AI**

**--- Don't Be Panic !!! Once there are github project , then means somebody must already succeeded.Other can means WE CAN!!!**

**--- Ask questiones if there are .**

**--- Daily study,dont worried that you are out of time**



## Resource (if you want something else , you can  do the sereach on bilibili then github)

### Ros2学习文档

https://gitee.com/gwmunan/ros2/wikis/pages?sort_id=9276391&doc_id=4855084

https://github.com/muziing/ROS2_Learning.git

### Ego_planner_swarm 

https://github.com/ZJU-FAST-Lab/ego-planner-swarm.git (make sure ros2 version)

### *pb_nav_simulation*

https://gitee.com/SMBU-POLARBEAR/pb_rm_simulation.git

### scurm_nav_ws

https://github.com/PolarisXQ/SCURM_Nav_Tutorial

https://github.com/PolarisXQ/SCURM_SentryNavigation.git

### fast_livo2

https://github.com/davidakhihiero/FAST-LIVO2-ROS2.git

https://github.com/TommyBrownson/FAST-Calib_Ros2.git //相机雷达标定包

https://blog.csdn.net/qq_62275910/article/details/151625713?spm=1001.2014.3001.5506 //复现教程

### legged_gym---四足训练学习（warning : issac gym 不支持50系及以上的显卡）

https://www.bilibili.com/video/BV1bBCcBtEnw/?spm_id_from=333.337.search-card.all.click&vd_source=74d17ae72c31a281ba10b070b597d5c6

https://github.com/LocoWiki/LocoWiki 







