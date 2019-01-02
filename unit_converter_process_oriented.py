#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# unit_converter_process_oriented.py
# 面向过程的万能单位转换器
# 操作方法：输入要转换的表达式。随时输入exit可退出。
# author: Binghan


import re


__author__ = "吴秉翰"

KEYWORD_OPTION = "option"
KEYWORD_UNIT = "unit"
KEYWORD_EXPRESSION = "expression"


def show_welcome():
    """ 显示欢迎词 """
    print("欢迎使用万能单位转换器")
    print(f"作者：{__author__}")


def show_help(scope="all"):
    """ 显示软件操作方法 """
    help_dict = {KEYWORD_OPTION: ["程序选项：",
                                  "  --e, exit：退出程序",
                                  "  --h, help：查看本帮助文档",
                                  "  --o, option：查看所有程序选项",
                                  "  --u, unit：查看所有可转换的单位类型",
                                  "  --p, expression：查看所有可转换的单位"],
                 KEYWORD_UNIT: ["可转换的单位：",
                                "   温度类：",
                                "        C 摄氏度",
                                "        F 华氏度",
                                "        K 开尔文",
                                "   长度类：",
                                "       mm 毫米",
                                "       cm 厘米",
                                "        m 米",
                                "       km 千米",
                                "     inch 英寸",
                                "     foot 英尺",
                                "     yard 码",
                                "     mile 英里",
                                "   货币类：",
                                "      CNY 人民币",
                                "      USD 美元",
                                "      EUR 欧元",
                                "      JPY 日元"],
                 KEYWORD_EXPRESSION: ["表达式语法：",
                                      "[待转换数值+]待转换单位 [转换符] [目标单位]",
                                      "   可接受的转换符为 -> 和 to, 也可省略转换符",
                                      "   无待转换数值时，将显示转换公式",
                                      "   无目标单位时，将输出默认推荐转换的目标",
                                      "例：",
                                      "   '18inch -> mm' 将18英寸转换为毫米",
                                      "   '18inch mm' 将18英寸转换为毫米，省略转换符",
                                      "   'inch -> mm' 将显示英寸转换为毫米的公式：" +
                                      "1inch = 2.54cm",
                                      "   'inch -> ' 或 'inch' 显示英寸转换为" +
                                      "默认推荐单位毫米的公式",
                                      "默认推荐转换关系：",
                                      "   长度：为不同制式单位中的同量级单位",
                                      "   温度：摄氏度转为华氏度，其他温度转为摄氏度",
                                      "   货币：人民币转为美元，其他币种转为人民币"]}
    if scope == "all":
        scope = [KEYWORD_OPTION, KEYWORD_UNIT, KEYWORD_EXPRESSION]
    else:
        scope = [scope]

    for key in scope:
        for sentence in help_dict[key]:
            print(sentence)
    print()


def show_result():
    """ 显示转换结果 """
    pass


def show_closing():
    """ 显示结束语 """
    print("程序退出，谢谢使用，再见～")


def get_user_input(tips="", in_line_tips=""):
    """ 获取用户输入 """
    print(tips)
    user_in = input(in_line_tips).strip()
    return user_in


def convert_temperature():
    """ 进行温度单位转换 """
    pass


def convert_lenth():
    """ 进行长度单位转换 """
    pass


def convert_currency():
    """ 进行货币单位转换 """
    pass


def expression_handler(user_input):
    """ 解析用户输入 """
    words = user_input.split()
    return words


def convert(expression_code):
    """ 读取解析好的用户输入，执行转换 """
    pass


def main():
    """ 主程序入口函数 """
    """
        使用方法：
    """

    # 定义提示类字符常量
    input_tips_control = "输入待转换表达式或程序选项"
    in_line_tips_control = "请输入: "

    show_welcome()
    show_help("option")
    while True:
        # 获取用户输入的表达式
        user_in = get_user_input(tips=(input_tips_control),
                                 in_line_tips=(in_line_tips_control))
        if user_in == "--e" or user_in == "exit":
            break
        elif user_in == "--h" or user_in == "help":
            show_help()
            continue
        elif user_in == "--o" or user_in == "option":
            show_help(scope=KEYWORD_OPTION)
            continue
        elif user_in == "--u" or user_in == "unit":
            show_help(scope=KEYWORD_UNIT)
            continue
        elif user_in == "--p" or user_in == "expression":
            show_help(scope=KEYWORD_EXPRESSION)
            continue

        # To do: 根据用户输入的单位类型，提示用户输入待转换表达式
        expression_code = expression_handler(user_in)
        # To do: 语法异常处理
        convert(expression_code)

    show_closing()

if __name__ == '__main__':
    main()
