#a class is a blueprint or template of somthing we want to create 
#it defines what an object will have 
class HelloWorld:

#def - is a function definition keyword
#__init__ - constractor (special method / dunder method/ magic method )
#self- reference to current object
#all together is called a method name Constructoor Method 
    def __init__(self):
        print("Hello,World")

#for this part there is a proper term called User-defined Function
#meaing a funtion that controls program flow or we can also think this like this this is the main control room of a program
def main():
    obj = HelloWorld()

#__name__ - special built-in variable 
#"__main__"- execution context 
if __name__=="__main__":
    main()