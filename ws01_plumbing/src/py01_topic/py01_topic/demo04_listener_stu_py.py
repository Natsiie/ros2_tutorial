"""    
    需求：
    流程：
        1.导包；
        2.初始化ROS2客户端；
        3.自定义节点类；
            3-1 创建订阅方
            3-2 解析订阅到的学生信息
        4.调用spin函数,并传入节点对象；
        5.资源释放。


"""
#1.导包；
import rclpy
from rclpy.node import Node
from base_interfaces_demo.msg import Student


# 3.自定义节点类；
class diy_msgs_listener_node(Node):
    def __init__(self):
        super().__init__("diy_msgs_listener_node_py")
        # 3-1 创建订阅方
        self.subscription = self.create_subscription(Student,"chatter_stu",self.do_cb,10)

        # 3-2 解析订阅到的学生信息
    def do_cb(self,stu):
        self.get_logger().info("订阅的学生信息：name = %s,age = %d,height = %.2f" % (stu.name,stu.age,stu.height))



def main():
    #2.初始化ROS2客户端;
    rclpy.init()
    #4.调用spin函数,并传入节点对象;
    rclpy.spin(diy_msgs_listener_node())
    #5.资源释放。
    rclpy.shutdown()

if __name__=='__main__':
    main()