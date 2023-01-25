#!/usr/bin/env python
# coding: utf-8

# In[20]:



class Employee:


    
    no_of_employees = 0

    def __init__(self, name, family_name, salary, department):
        self.name = name
        self.family_name = family_name
        self.salary = salary
        self.department = department
        Employee.no_of_employees += 1

    @staticmethod
    def average_salary(employees):
       
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.no_of_employees


class FulltimeEmployee(Employee):
   

    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def full_time_benefits(self):
        print("Few benefits as full time employee.")


def main():
    employees = []
    fte1 = FulltimeEmployee("sneha", "kusuma", 50000, "software")
    fte1.full_time_benefits()
    employees.append(fte1)
    fte2 = FulltimeEmployee("mahi", "pulagam", 180000, "civil engineering")
    employees.append(fte2)
    emp1 = Employee("ramya", "vengal", 160000, "automobile")
    employees.append(emp1)
    emp2 = Employee("deepika", "thota", 135000, "engineering")
    employees.append(emp2)
    print("Average salary:", FulltimeEmployee.average_salary(employees))


if __name__ == "__main__":
    main()


# In[25]:


import numpy as np
a = np.arange(1,21)
print(a)
b = a.reshape(4, 5)
print(b)
#c = b.replace(max(axis=1), 0)

c = b.max(axis=1)

#row_maxes = c.max(axis=1).reshape(-1, 1)
#c[:] = np.where(c == row_maxes, 0, 1)

print(c)


# In[ ]:




