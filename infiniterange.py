class infinite_range:
    def __init__(self, start: int = 0, step: int = 1):
        self.__start = start
        self.__step = step
        self._current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        val = self._current
        self._current += self.__step
        return val
    
    def __repr__(self):
        return f"{type(self).__name__}(start={self.__start}, step={self.__step})"
    
    def __str__(self):
        return f"<{type(self).__name__} start={self.__start} step={self.__step}>"
