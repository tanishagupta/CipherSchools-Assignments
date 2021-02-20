class StackPushPop:
    def StackPush(self,arr):
        self.a=input()
        for i in range(len(arr)):
            if self.a not in arr:
                # pushing elements
                arr.append(self.a)
            else:
                continue
        print(arr)


    def StackPop(self,arr):
        self.b=input()
        for i in range(len(arr)):
            if self.b in arr:
                # popping elements
                arr.remove(self.b)
            else:
                continue
        print(arr)

arr=["a","b","C","d"]
obj = StackPushPop()
obj.StackPush(arr)
obj.StackPop(arr)


