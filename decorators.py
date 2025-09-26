# class Calc:#parent,super,or base calss
#     def add (self,a,b):
#         return a + b

# # class AdvCalc:
#     # def add(self,a,b):
#     #     return a + b

# # class AdvCalc(Calc):
# #     pass

# # adv1 =AdvaCalc()
# # adv1.add(2,3)

# class AdvCalc(Calc):#child class,sub,derived
#     def find_log(self,num):
#         return num/5

# adv1 =AdvaCalc()
# adv1.add(2,3)

# c1 =Calc()
# c1.find_log()#error

# #types of inheritance
# #Multilevel inheritance
# #Multiple Inheritance
# #hierarche inheritence
# one parent one child->single 
# a->b->c#Multilevel inheritance
# one child class can inherit multiple parent classes#Multiple Inheritance
# one parent calss multiple child classes#hierarchical

# hybrid inheritence
# class A:
#     pass
# class B(A):
#     pass
# class D:
#     pass
# class c(B,D):
#     pass

# method -overriding
# class Calc:#parent
#     company = "CASIO"
#     def __init__(self,id,manf_date):
#         self.id = id
#         self.manf_date=manf_date
#     def add(self,a,b):
#         return a+b

#     def mul(self,a,b):
#         return a*b


# class AdvCalc(Calc):#child
#        def __init__(self,id,manf_date,cmp_power):
#         super().__init__(id,manf_date)
#         self.cmp_power = cmp_power
#         print("child class constructor called")

#         def find_log(self,num):
#             return num/5

#         def add(self,a,b):
#             # super().add(a,b)
#             print("child class add called") 
#             return a + b           

# adv1=AdvCalc(1,'15-sept',20)
# print(adv1.add(2,3))
# print(adv1.company)


# in inheritence we can inheritance  methods,var
# in case of var class /static can inheritance
# to call constractor of parent and utilize it in child with some new attributes we use 
# super()._init_(id,manf_date)
##interview question
# method resolution order(.mro()/.__mro__)=> eg balayya,ntr ->lion tiger liger(tiger,lion)

# class Lion():
# def hunt(self):
#     print("balayya is hunting")
# def roar(self):
#     print("balayya is roaring")    

# class Tiger():
# def hunt(self):
#     print("ntr is hunting") 

    # def roar(self):
    #     print("ntr is roaring")


# class Liger(Tiger,Lion):
#     pass

# l1=Liger()
# l1.hunt()
# l1.roar()
# print(Liger.mro())
# print(Liger.__mro__)

class Car:
    def __init__(self,model,brand):
        self.model1= model
        self.brand1 = brand
    def show(self):
        print(f"{self.model1},{self.brand1}")    
c1 =Car("Swift","Maruthi suzuki")     
c1.show()
c2=Car("x","y")
c2.show()

class Student:
    school_name =" Dhruva"           #class variable
    def __init__(self,name,rol_no):
        self.name1=name               # instance variable
        self.rol_no1=rol_no
     
    def method(self):
        local_var = "x"              #local variable
        print(local_var)
s1 =Student("sri",23)  
print(s1.name1)    

class Student:
    school_name =" Dhruva"           #class variable
    def __init__(self,name,rol_no):
        self.name1=name               # instance variable
        self.rol_no1=rol_no

    @classmethod
    def  class_method(cls,new_name):
        cls.school_name = new_name 
        print("new school name assigned")  

    def instance_method(self,marks):
        self.marks=marks
        print(f"{self.school_name},{self.name1},{self.rol_no1},{self.marks}")

    def method(self):
        local_var = "x"              #local variable
        print(local_var)
    @staticmethod    
    def static_method(a,b):
        print(a+b)    
    
s1 =Student("sri",23)  
print(s1.name1)  

s1.instance_method(55)
Student.class_method("ACE") 
print(s1.school_name)
Student.static_method(2,3)

#single inheritance

class Parent:
    def p(self):
        print("parent")
class Child(Parent):
    def c(self):
        
        print("child") 
obj = Child()
obj.p()             

#multilevel inheritance
# class Grand_parent:
#     def gp(self):
#         print("grand parent")
#     def A(self):
#         print("none")    
# class Parent(Grand_parent):
#     def p(self):
#         print("parent")
# class Child(Parent):
#     def c(self):
#         print("child") 
# c1 = Child()
# c1.p()
# c1.A()

#multiple inheritance
# class P:
#     def p(self):
#         print("parent")
# class F:
#     def f(self):
#         print("father")
# class M:
#     def m(self):
#         print("mother")
# class Child(P,M,F):
#     def child(self):
#         print("child")

# obj = Child()
# obj.m()




    


