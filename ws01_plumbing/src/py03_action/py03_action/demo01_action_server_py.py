"""    
    需求：编写动作服务端，解析客户端提交的数字，遍历该数字并累加求和，最终结果响应回客户端，且请求响应过程中需要生成连续反馈。
    流程：
        1.导包；
        2.初始化ROS2客户端；
        3.自定义节点类；
            3-1创建动作服务端对象；
            3-2处理提交的目标值(回调函数) ---  默认实现
            3-3处理取消请求 --- 默认实现
            3-4生成连续反馈与最终响应(回调函数)
        4.调用spin函数,并传入节点对象；
        5.资源释放。


"""
#1.导包；
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from base_interfaces_demo.action import Progress
import time

# 3.自定义节点类；
class ProgressActionServer(Node):
    def __init__(self):
        super().__init__("progress_action_server_node_py")
        self.get_logger().info("服务端创建成功！")
        #3.1 创建动作服务端对象
        #node，action_type，action_name，excute_callback,
        self.server = ActionServer(
            self,
            Progress,
            "get_sum",
            self.excute_callback
        )
    # 生成连续反馈与最终响应（回调函数）
    def excute_callback(self,goal_handle):
        #1.连续反馈
        num = goal_handle.request.num
        sum = 0
        for i in range(1,num+1):
            sum += i
            feedback = Progress.Feedback()
            feedback.progress = i / num
            goal_handle.publish_feedback(feedback)
            self.get_logger().info("连续反馈：%.2f" %feedback.progress)
            time.sleep(1.0)
        
        #2.响应最终结果
        goal_handle.succeed()
        result = Progress.Result()
        result.sum = sum

        self.get_logger().info("最后结果：%d" %result.sum)
        return result

def main():
    #2.初始化ROS2客户端;
    rclpy.init()
    #4.调用spin函数,并传入节点对象;
    rclpy.spin(ProgressActionServer())
    #5.资源释放。
    rclpy.shutdown()

if __name__=='__main__':
    main()