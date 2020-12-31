# -*- coding: utf-8 -*-

import pyomo.environ as pe

def CirclePacking(size):
    
    model = pe.AbstractModel()
    model.n = pe.Param(within=pe.NonNegativeIntegers)
    
    model.I = pe.RangeSet(1,model.n)
    model.J = pe.RangeSet(1,model.n)
    
    model.x = pe.Var(model.I, bounds=(0,1))
    model.y = pe.Var(model.I, bounds=(0,1))
    model.r = pe.Var(domain=pe.NonNegativeReals)
    
    # on a vu des méthodes permettant de déterminer le minimum
    # mais on cherche max r ce qui revient à chercher min -r
    model.obj = pe.Objective(expr = - model.r ) 
    
    def constraint_rule(m,i,j):
        # return the expression for the constraint for i and j if i != j
        return ( (m.x[i] - m.x[j])^2 + (m.y[i] - m.y[j])^2 for j in m.J if j != i ) >= m.r^2
    
    model.constraint = pe.Constraint(model.I, rule = constraint_rule ) 
    
    model.n = size
    
    return model.create_instance()