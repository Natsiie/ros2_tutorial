import rclpy
from rclpy.node import Node

class MyNode(Node):
	def __init__(self):
		super().__init__("hello_world_class_py_node")
		self.get_logger().info("hello world!")

def main():
	rclpy.init()
	node=MyNode()
	rclpy.spin(node)
	rclpy.shutdown()


if __name__ =="__init__":
	main()