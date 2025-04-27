class Television:
    '''
    Television class that controls the remote control of the TV.
    '''
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        define variables status, muted volume and channel
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self)-> None:
        '''
        turn the TV on or off.
        '''
        self.__status = not self.__status

    def mute(self)-> None:
        '''
        Mute and unmute the TV
        '''
        if self.__status:
            self.__muted = not self.__muted


    def channel_down(self)-> None:
        '''
        Decrease the TV channel
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -=1
            else:
                self.__channel = Television.MAX_CHANNEL

    def channel_up(self)-> None:
        '''
        Increase the TV channel
        '''
        if self.__status:
            if self.__channel != Television.MAX_CHANNEL:
                self.__channel +=1
            else:
                self.__channel = Television.MIN_CHANNEL


    def volume_up(self)-> None:
        '''
        Lower the TV volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume +=1

    def volume_down(self)-> None:
        '''
        Increase the TV volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self)-> str:
        '''
        Give TV status
        :return: Power, Channel and Volume status.
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'