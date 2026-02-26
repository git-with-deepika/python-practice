class student:
    name='deepika'
    # constructor is automatically called when we create an object.. by givingproperty or argument
    def __init__(self,location):
        self.location=location

# here we have created oject
obj1=student('delhi')
# here we have accessed the object's attribute
print(obj1.location)  

obj2=student('jaipur')
print(obj2.location)
print(obj2.name)


class teacher:
    def __init__(self,exp,name,domain):
        self.exp=exp
        self.name=name
        self.domain=domain

new=teacher(2,'ram','science')
print(new.exp)
print(new.name)
print(new.domain)        


# self keyword is used to show the current object or instance
class House:
  color='blue'
  room=5
  # constructor is automatically called when the object is created
  def __init__(self):
    print("init function is called")
    print(self)


House()



class Student:
   collage='IIT'
   def __init__(self,name,location):
      self.name=name
      self.location=location
   
   def display(self):
      print(f'name of student: {self.name}')
      print(f'student location: {self.location}')
      print(f'collage name : {self.collage}')

obj3=Student('radhika','delhi')
obj3.display()    



class employee:
  company='infosys'
  def __init__(self,name,location,department,salary):
    self.name=name
    self.location=location
    self.department=department
    self.salary=salary

  def display(self):
    print(f'detalis of employee: name: {self.name} , location : {self.location} , department :{self.department} , salary :{self.salary} , company: {self.company}')



emp1=employee('deepika','jaipur','testing',50000)
emp2=employee('simran','delhi','coding',6000)
emp1.display()
emp2.display()




class writer:
  writer_name='j.s. kelvin'
  def __init__(self,title,publish_date):
    self.title=title
    self.publish_date=publish_date

  def display(self):
    print(f' title :{self.title} , publish date :{self.publish_date} , writer name: {self.writer_name}')




wr1=writer('One day' ,'25-dec-2025')
wr2=writer('Happiness' ,'2-nov-2024')

wr1.display()
wr2.display()


# INHERTANCE
# single inheritance
class teacher:
   def __init__(self,name,subject):
      self.name=name
      self.subject=subject

class class_teacher(teacher):
   def __init__(self,name,subject,section):
      super().__init__(name,subject)
      self.section=section
   
   def display(self):
      print(f'Name of teacher: {self.name} ')
      print(f'subject: {self.subject}') 
      print(f'section: {self.section}')      


teacher_obj=class_teacher('karan','computer','A')      
teacher_obj.display()


