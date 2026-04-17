"""
    需求：订阅发布方发布的信息，并在终端输出
    流程：
        1.包含头文件
        2.初始化ROS2客户端；
        3.自定义节点类；
            3-1.创建订约方
            3-2 解析并输出数据
        4.调用spin函数，并传入节点对象指针
        5.资源释放

"""
#包含头文件
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#自定义节点类；
class Listener(Node):
    def __init__(self):
        super().__init__("Lisner_node_py")
        self.get_logger().info("Listener is setup.")
        #3-1 创建订阅方
        """
        参数：数据类型，话题名称，回调函数，QOS(队列长度)
        返回值：返回订阅对象
        """
        self.subscription = self.create_subscription(String,"chatter",self.do_cb,10)
        #3-2 解析并输出数据
    def do_cb(self,msg):
        self.get_logger().info("订阅的数据：%s" % msg.data)



def main():
#初始化
    rclpy.init()

#4.调用spin函数，并传入节点对象指针
    rclpy.spin(Listener()) 

#资源释放
    rclpy.shutdown()



if __name__ == '__main__':
    main()