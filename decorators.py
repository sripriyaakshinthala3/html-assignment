class Calc:#parent,super,or base calss
    def add (self,a,b):
        return a + b

# class AdvCalc:
    # def add(self,a,b):
    #     return a + b

# class AdvCalc(Calc):
#     pass

# adv1 =AdvaCalc()
# adv1.add(2,3)

class AdvCalc(Calc):#child class,sub,derived
    def find_log(self,num):
        return num/5

adv1 =AdvaCalc()
adv1.add(2,3)

c1 =Calc()
c1.find_log()#error

#types of inheritance
#Multilevel inheritance
#Multiple Inheritance
#hierarche inheritence
one parent one child->single 
a->b->c#Multilevel inheritance
one child class can inherit multiple parent classes#Multiple Inheritance
one parent calss multiple child classes#hierarchical

# hybrid inheritence
# class A:
#     pass
# class B(A):
#     pass
# class D:
#     pass
# class c(B,D):
#     pass
