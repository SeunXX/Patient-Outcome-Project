
#Reference

Activity_Posrange_4 = ('I can perform regular activities')
Activity_Posrange_3 = ('I can perform regular activities')
Activity_Negrange_4 = ('I can perform activities only at home')
Activity_Negrange_3 = ('I can perform activities only at home')

# Create a dataframe from available data: Dataframe is called Raw_data

Raw_data = {'Questions': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10'],
'Activity_Negrange_4': [0.269330618, 0.044515075, 0.126602544, 0.181089785, 0.062479546, 0.08941446, 0.029424918,
0.017191687, 0.008850818, 0.139059658], 'Activity_Negrange_3': [0.273967835, 0.059255171, 0.154622921, 0.227602304,
0.078324752, 0.111491701, 0.038597186, 0.023217847, 0.013011659, 0.216803781], 'Activity_Posrange_3': [0.00945783,
0.009356733, 0.013222638, 0.004120498, 0.009666299, 0.019566964, 0.005919193, 0.014486183, 0.003753526, 1.83995E-05
], 'Activity_Posrange_4': [0.00801834, 0.006973293, 0.010489052, 0.003141665, 0.007603265, 0.015395057, 0.00448751,
0.010711989, 0.002550522, 1.15614E-05]}

# Create dataframe to be able to work on the data instead of import as csv file

import pandas as pd
import numpy as np
import scipy
import heapq
from scipy import stats

Raw_data_DF = pd.DataFrame(Raw_data)
print(Raw_data_DF)

# Calulate Geometric mean per row for positve range 4 and 3; and then negative range 4 and 3
from heapq import nlargest
from scipy import stats
from scipy.stats.mstats import mode, gmean, hmean

# Geometric mean per row for negative range 4 and 3 in Raw_data_DF:
Geometric_meanneg = scipy.stats.gmean(Raw_data_DF.iloc[:,1:2],axis=1)
print(nlargest(3, Geometric_meanneg))

# Geometric mean per row for positve range 4 and 3 in Raw_data_DF:
Geometric_meanpos = scipy.stats.gmean(Raw_data_DF.iloc[:,3:4],axis=1)
print(nlargest(3, Geometric_meanpos))


# Range_Positive = ('I can perform regular activities')
# Range_Negative = ('I can perform activities only at home')

Activity_Posrange_4 = ('I can perform regular activities')
Activity_Posrange_3 = ('I can perform regular activities')
Activity_Negrange_4 = ('I can perform activities only at home')
Activity_Negrange_3 = ('I can perform activities only at home')

#considering only 2 possible options available describing activity potential of patient that we selected as shown above
Question_Selection = input('Please describe your ability potential after care:'))

if Question_Selection == Activity_Posrange_4 and Activity_Posrange_4 == Activity_Posrange_3:
    print(nlargest(3, Geometric_meanpos)

elif Question_Selection == Activity_Negrange_4 and Activity_Negrange_4 == Activity_Negrange_3:
    print(nlargest(3, Geometric_meanneg))

else:
    print('Please talk to your Health provider to fill in your PRO')





# Second possibility when User inputted something wrong

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        Question_Selection = input('Please describe your ability potential after care:'))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:

        break
# return to start of loop


Question_Selection = input('Please describe your ability potential after care:')

if Question_Selection == Activity_Posrange_4 and Question_Selection == Activity_Posrange_3:

    print(nlargest(3, Geometric_meanpos)

elif Question_Selection == Activity_Negrange_4 and Question_Selection == Activity_Negrange_3:
    print(nlargest(3, Geometric_meanneg))

else:
    print('Please, talk to your Health provider to fill in your PRO')
