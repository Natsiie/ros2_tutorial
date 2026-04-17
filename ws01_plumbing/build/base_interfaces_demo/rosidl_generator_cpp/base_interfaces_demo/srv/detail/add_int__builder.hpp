// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from base_interfaces_demo:srv/AddInt.idl
// generated code does not contain a copyright notice

#ifndef BASE_INTERFACES_DEMO__SRV__DETAIL__ADD_INT__BUILDER_HPP_
#define BASE_INTERFACES_DEMO__SRV__DETAIL__ADD_INT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "base_interfaces_demo/srv/detail/add_int__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace base_interfaces_demo
{

namespace srv
{

namespace builder
{

class Init_AddInt_Request_num2
{
public:
  explicit Init_AddInt_Request_num2(::base_interfaces_demo::srv::AddInt_Request & msg)
  : msg_(msg)
  {}
  ::base_interfaces_demo::srv::AddInt_Request num2(::base_interfaces_demo::srv::AddInt_Request::_num2_type arg)
  {
    msg_.num2 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::base_interfaces_demo::srv::AddInt_Request msg_;
};

class Init_AddInt_Request_num1
{
public:
  Init_AddInt_Request_num1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddInt_Request_num2 num1(::base_interfaces_demo::srv::AddInt_Request::_num1_type arg)
  {
    msg_.num1 = std::move(arg);
    return Init_AddInt_Request_num2(msg_);
  }

private:
  ::base_interfaces_demo::srv::AddInt_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::base_interfaces_demo::srv::AddInt_Request>()
{
  return base_interfaces_demo::srv::builder::Init_AddInt_Request_num1();
}

}  // namespace base_interfaces_demo


namespace base_interfaces_demo
{

namespace srv
{

namespace builder
{

class Init_AddInt_Response_sum
{
public:
  Init_AddInt_Response_sum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::base_interfaces_demo::srv::AddInt_Response sum(::base_interfaces_demo::srv::AddInt_Response::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::base_interfaces_demo::srv::AddInt_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::base_interfaces_demo::srv::AddInt_Response>()
{
  return base_interfaces_demo::srv::builder::Init_AddInt_Response_sum();
}

}  // namespace base_interfaces_demo

#endif  // BASE_INTERFACES_DEMO__SRV__DETAIL__ADD_INT__BUILDER_HPP_
