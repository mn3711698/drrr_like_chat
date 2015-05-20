# -*- coding: utf-8 -*-


class Room(object):
    """
    房间对象
    """

    id = None              # id
    name = None         # 房间名称
    limit_num = 0    # 人数上限
    room_type = None    # 房间类型
    now_num = 0      # 当前房间里的人数
    now_list = []     # 当前房间里的人
    message_list = [] # 消息列表
    host_user = None         # 房主

    def __init__(self, name=None, limit_num=None, host_user=None):
        self.name = name
        self.limit_num = limit_num
        self.host_user = host_user

