class Error:
    def __init__(self):
        self.num_list = []

    def input_num(self):
        value = None
        while True:
            value = input(f"input numbers or 'stop' to exit - ")
            if value == 'stop':
                print(*self.num_list, sep = '\n')
                return
            try:
                int(value)
                self.num_list.append(value)
            except:
                print(f"Недопустимое значение")
                
try_except = Error()
try_except.input_num()