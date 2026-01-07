def outer():
    print("outer jn statment")

def inner():
    print("inner function")
    inner()
    inner()
    inner()


outer()
inner()
  
  
