# coding: utf-8
def echo(value=None):
    print "Excution starts when next() is called for the first time."
    try:
        while True:
            try:
                print "Befor type(value)=",type(value)
                value=(yield value)
                print "After type(value)=",type(value)
            except Exception,e:
                value=e
    finally:
        print "Don't forget to clean up when 'close()'is called"

generator=echo(1)
print generator.next() #1

print "*"*10
print generator.next() #None

print "*"*10
print generator.send(2) #2 yield value
generator.throw(TypeError,"spam")
print generator.close()