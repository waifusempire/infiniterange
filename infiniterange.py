class infinite_range:
    def __init__(self, start: int = 0, step: int = 1):
        """start: optional<int> = default<0>
step: optional<int> = default<1>"""
        self.__start = start
        self.__step = step
        self.__current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        val = self.__current
        self.__current += self.__step
        return val
    
    def __repr__(self):
        return f"{type(self).__name__}(start={self.__start}, step={self.__step})"
    
    def __str__(self):
        return f"<{type(self).__name__} start={self.__start} step={self.__step}>"
    
    def reset(self):
        "Reset the range to the start value"
        self.__current = self.__start

    @property
    def current(self):
        "The current value"
        return self.__current
    
    @property
    def start(self):
        "The start value"
        return self.__start
    
    @property
    def step(self):
        "How many values should the range skip between iterations"
        return self.__step
    

