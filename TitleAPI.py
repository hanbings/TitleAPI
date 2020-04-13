# -*- coding: utf-8 -*-

# title轮子
# title <玩家> clear（移除屏幕标题）
def clear_title(server, playerName):
    server.execute("title" + " " + playerName + " " + "clear")


# title <玩家> reset（将各选项复位至默认值）
def reset_title(server, playerName):
    server.execute("title" + " " + playerName + " " + "reset")


# title <玩家> title <JSON文本标题>（将文字显示为主标题）
def seed_title(server, playerName, message):
    server.execute("title" + " " + playerName + " " + "title" + " " + "{\"text\":\"" + message + "\"}")


# title <玩家> subtitle <JSON文本标题>（将文字显示为副标题）
def seed_subtitle(server, playerName, subMessage):
    server.execute("title" + " " + playerName + " " + "subtitle" + " " + "{\"text\":\"" + subMessage + "\"}")


# title <玩家> actionbar <JSON文本标题>（在快捷栏上方显示的标题）
def seed_actionbar(server, playerName, message):
    server.execute("title" + " " + playerName + " " + "actionbar" + " " + "{\"text\":\"" + message + "\"}")


# title <玩家> times <渐入> <保持> <渐出>（设置渐入、保持和渐出的持续时间）
def times_title(server, playerName, inToTitleTime, outToTitleTime, holdTitleTime):
    server.execute("title" + " " + playerName + " " + "time" + " " + inToTitleTime + " " + outToTitleTime + " "
                   + holdTitleTime)


# 封装带颜色的标题（在屏幕中间显示）
def seed_color_title(server, playerName, message, color):
    server.execute(
        "title" + " " + playerName + " " + "title" + " " + "{\"text\":\"" + message + "\",\"color\":\"" + color + "\"}")


# 封装带子标题的标题（在屏幕中间显示）
def seed_sub_title(server, playerName, message, subMessage):
    server.execute("title" + " " + playerName + " " + "subtitle" + " " + "{\"text\":\"" + subMessage + "\"}")
    server.execute("title" + " " + playerName + " " + "title" + " " + "{\"text\":\"" + message + "\"}")


# 封装带颜色和子标题的标题（在屏幕中间显示）
def seed_color_sub_title(server, playerName, message, subMessage, color, subColor):
    server.execute("title" + " " + playerName + " " + "subtitle" + " " + "{\"text\":\"" + subMessage + "\",\"color\":\""
                   + subColor + "\"}")
    server.execute("title" + " " + playerName + " " + "title" + " " + "{\"text\":\"" + message + "\",\"color\":\""
                   + color + "\"}")