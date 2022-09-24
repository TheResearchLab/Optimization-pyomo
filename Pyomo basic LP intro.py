# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 17:33:42 2022

@author: Aaron
"""
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

#decision variables
model = pyo.ConcreteModel()
model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))

x = model.x
y = model.y

# Constraints
model.C1 = pyo.Constraint(expr=-x+2*y<=8)
model.C2 = pyo.Constraint(expr=2*x+y<=14)
model.C3 = pyo.Constraint(expr=2*x-y<=10)

#Objectives
model.obj = pyo.Objective(expr=x+y, sense=maximize)

# Error Before the Try Except
# TimeoutExpired: Command '['C:\\glpk-4.65\\w64\\glpsol.exe', '--version']' timed out after 1 seconds
# https://stackoverflow.com/questions/42736963/how-to-skip-subprocess-timeout

try:
    opt = SolverFactory('glpk')
except subprocess.TimeoutExpired:
    pass

opt.solve(model)

model.pprint()
x_value = pyo.value(x)
y_value = pyo.value(y)

print("x= ",x_value)
print("y= ",y_value)