# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 18:20:23 2020

@author: helle
"""

import numpy as np
from scipy.integrate import solve_ivp

from parameters_1 import *  # basic scenario (all parameters)
from index import *
from functions import *
from differential_equations import *
from solve_function import *



# basic
#modelEbola(t_iso = 1000)
#modelEbola()
#modelEbola(k=1)
#modelEbola(k=2)
#modelEbola(k=3)


# longer
#modelEbola(days=2000, t_iso=1000)
#modelEbola(days=2000)
#modelEbola(days=2000, k=1)
#modelEbola(days=2000, k=2)
#modelEbola(days=2000, k=3)

# with control over traceback
#modelEbola(days=2000,f_tb=0, k=0)
#modelEbola(days=2000,f_tb=0.2, k=0)
#modelEbola(days=2000,f_tb=0.4, k=0)
#modelEbola(days=2000,f_tb=0.6, k=0)
#modelEbola(days=2000,f_tb=0.8, k=0)
#modelEbola(days=2000,f_tb=1, k=0)

#modelEbola(days=2000,f_tb=0, k=3)
#modelEbola(days=2000,f_tb=0.2, k=3)
#modelEbola(days=2000,f_tb=0.4, k=3)
#modelEbola(days=2000,f_tb=0.6, k=3)
#modelEbola(days=2000,f_tb=0.8, k=3)
#modelEbola(days=2000,f_tb=1, k=3)

#modelEbola(days=2000,f_tb=1, k=3, qmax=0)
#modelEbola(days=2000,f_tb=1, k=3, qmax=500)
#modelEbola(days=2000,f_tb=1, k=3, qmax=1000)
#modelEbola(days=2000,f_tb=1, k=3, qmax=2000)
#modelEbola(days=2000,f_tb=1, k=3, qmax=4000)

modelEbola(days=1000,f_tb=1, qmax=10000, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1, t_iso = 1000)
modelEbola(days=1000,f_tb=1, qmax=10000, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1, k=0)
modelEbola(days=1000,f_tb=1, qmax=10000, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1, k=1)
modelEbola(days=1000,f_tb=1, qmax=10000, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1, k=2)
modelEbola(days=1000,f_tb=1, qmax=10000, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1, k=3)





# to compare to poster: 1 Erlang stage
#modelEbola(days=2000,f_tb=1, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1,t_iso=2000)
#modelEbola(days=2000,f_tb=1, k=0, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1)
#modelEbola(days=2000,f_tb=1, k=1, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1)
#modelEbola(days=2000,f_tb=1, k=2, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1)
#modelEbola(days=2000,f_tb=1, k=3, NE = 1, NP = 1, NIp = 1, NIh = 1, NIi = 1)




