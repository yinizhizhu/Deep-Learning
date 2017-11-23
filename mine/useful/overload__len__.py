class test__:
    def __init__(self):
        self.list = []
        for i in xrange(100):
            self.list.append(i)

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return len(self.list)

tmp = test__()
print len(tmp)
print tmp[0]