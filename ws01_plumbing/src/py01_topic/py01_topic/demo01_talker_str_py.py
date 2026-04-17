"""
    需求：以某个固定频率发送文本“hello world!”,文本后缀编号，每发布一条，编号加一
    流程：
    1.包含头文件
    2.初始化ROS2客户端
    3.自定义节点类
      3-1 创建发布方
      3-2 创建定时器
      3-3 组织并发布消息
    4.调用spin,传入自定义对象指针
    5.释放资源
"""
#包含头文件
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#3.自定义节点类；
class Talker(Node):
    def __init__(self):
        super().__init__("talker_node_py")
        self.get_logger().info("Talker节点已创建！")

        #设置计数器
        self.count = 0

        # 3-1 创建发布方;
        """
        参数：
            1.消息类型；
            2.话题名称；
            3.QOS，队列长度。
        返回值：发布对象。
        """
        self.publisher = self.create_publisher(String,"chatter",10)

    # 3-2 创建定时器;
        self.timer = self.create_timer(1.0,self.on_timer)

    # 3-3 组织并发布消息;
    def on_timer(self):
        message = String()
        message.data = "hello world ! " + str(self.count)
        self.publisher.publish(message)
        self.count += 1
        self.get_logger().info("发布的数据：%s" % message.data)

def main():
    #2.初始化ROS2客户端
    rclpy.init()    

    #4.调用spin,传入自定义对象指针
    rclpy.spin(Talker())

    #5.释放资源
    rclpy.shutdown()



if __name__ == '__main__':
    main()
