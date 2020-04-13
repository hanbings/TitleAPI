# TitleAPI -- 针对MCDR封装的Title命令

| 方法                                                         | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| clear_title(server, playerName)                              | title <玩家> clear 的封装 移除屏幕标题                       |
| reset_title(server, playerName)                              | title <玩家> reset 的封装 将各选项复位至默认值               |
| seed_title(server, playerName, message)                      | title <玩家> title <JSON文本标题> 的封装 将文字显示为主标题  |
| seed_subtitle(server, playerName, subMessage)                | title <玩家> subtitle <JSON文本标题> 的封装 将文字显示为副标题 |
| seed_actionbar(server, playerName, message)                  | title <玩家> actionbar <JSON文本标题> 的封装 在快捷栏上方显示的标题 |
| times_title(server, playerName, inToTitleTime, outToTitleTime, holdTitleTime) | title <玩家> times <渐入> <保持> <渐出> 的封装 设置渐入、保持和渐出的持续时间 |
| seed_color_title(server, playerName, message, color)         | 带全句颜色的主标题                                           |
| seed_sub_title(server, playerName, message, subMessage)      | 使用此方法子标题和主标题一起发送                             |
| seed_color_sub_title(server, playerName, message, subMessage, color, subColor) | 使用此方法可设置主和子的颜色，并且一起发送                   |

**注意**：

*§颜色符号在以上方法皆可使用* 

*只发送子标题不发生主标题将不会将子标题单独显示，而是会缓存到下一次使用主标题时发送，且将会被设置了子标题的主标题覆盖*