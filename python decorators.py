def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for using this function")
    return mfx
@greet
def hello():
    print("hello world")
# @greet
# def add(a,b):
#     print(a +b)

hello()
# add(1,2)