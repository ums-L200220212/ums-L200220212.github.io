from metaflow import FlowSpec, step
class Helloworld(FlowSpec):
    @step
    def start(self):
        """starting point"""
        print("this is the start of the step")
        self.next(self.hello)
    def hello(self):
        """processing hello"""
        print ("hello world")
        self.next(self.end)
    def end(self):
        """end of the process"""
        print ("this is the end of the step")
if __name__=='__main__':
    Helloworld()