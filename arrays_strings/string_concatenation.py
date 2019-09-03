class StringConcatenation:
    def __init__(self, orig_str):
        self.current = None
        self.memory = []
        self.orig_str = orig_str
        self.scan()

    def scan(self):
        for char in self.orig_str:
            if self.current is None:
                self.current = char
                self.count = 1
            elif self.current == char:
                self.count += 1
            else:
                self.memory.append(self.current)
                self.memory.append(str(self.count))
                self.current = char
                self.count = 1

        self.memory.append(self.current)
        self.memory.append(str(self.count))

        new_str = "".join(self.memory)
        if len(new_str) >= len(self.orig_str):
            self.new_str = self.orig_str
        else:
            self.new_str = new_str

    def __str__(self):
        return self.new_str


if __name__ == "__main__":
    orig_str = input("Input a string: ")
    print(StringConcatenation(orig_str))
