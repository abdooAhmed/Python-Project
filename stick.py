import  numpy as np
import  pandas as ps
dataset = np.genfromtxt('./Data-Visualization-with-Python-master/Lesson01/Activity01/data/normal_distribution.csv',delimiter=',')
dataset1 = ps.read_csv('./Data-Visualization-with-Python-master/Lesson01/Exercise02/data/world_population.csv',index_col=0)

dataset1.pivot(index=["1999"] * len(dataset),columns="Country Code", values="1999")

