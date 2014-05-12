# -*- coding: utf-8 -*-

import sklearn
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ra.serializers.DecisionTreeSerializer import DecisionTreeSerializer
  
 
#Dependent variables (Each element in X is an array of dependent variable values)
X = [[28,	39.60,	27.20,	67.43,	44.57,	0.00],[29,	38.91,	27.09,	72.29,	43.86,	0.97],
[30,	33.09,	23.09,	92.43,	66.57,	6.00],[31,	30.51,	23.80,	86.57,	65.86,	1.46],
[32,	34.26,	24.91,	80.86,	57.43,	0.17],[33,	39.31,	27.11,	69.00,	43.86,	0.97],
[34,	35.09,	24.14,	86.57,	59.29,	5.00],[35,	31.94,	23.46,	90.43,	67.00,	2.46],
[36,	32.44,	24.46,	83.00,	56.29,	0.00],[37,	30.79,	23.40,	90.86,	70.43,	4.46],
[38,	30.00,	22.63,	88.14,	72.14,	0.77],[39,	29.66,	22.83,	93.00,	64.43,	11.89],
[40,	30.97,	22.14,	100.00,	68.14,	29.06],[41,	28.54,	22.66,	96.14,	71.43,	5.77],
[28,	28.37,	22.11,	99.14,	76.86,	8.26],[29,	30.17,	22.06,	94.29,	63.71,	1.89],
[30,	30.41,	22.09,	89.57,	71.57,	9.53],[31,	32.01,	22.50,	85.43,	54.00,	1.74],
[32,	39.60,	27.20,	67.43,	44.57,	0.00],[33,	38.91,	27.09,	72.29,	43.86,	0.97],
[34,	33.09,	23.09,	92.43,	66.57,	6.00],[35,	30.51,	23.80,	86.57,	65.86,	1.46],
[36,	34.26,	24.91,	80.86,	57.43,	0.17],
[37,	39.31,	27.11,	69.00,	43.86,	0.97],
[38,	35.09,	24.14,	86.57,	59.29,	5.00],
[39,	31.94,	23.46,	90.43,	67.00,	2.46],
[40,	32.44,	24.46,	83.00,	56.29,	0.00],
[41,	30.79,	23.40,	90.86,	70.43,	4.46],
[28,	21.29,	13.86,	47.14,	27.57,	4.86],
[37,	28.43,	20.14,	67.43,	44.57,	0.33],
[38,	31.64,	22.71,	87.14,	58.43,	2.63],
[39,	31.79,	22.86,	89.43,	55.57,	1.29],
[40,	30.14,	22.29,	91.29,	74.00,	13.43],
[41,	28.79,	21.43,	89.86,	70.29,	6.23],
[28,	30.21,	21.57,	91.00,	66.71,	3.83],
[29,	31.00,	22.00,	89.29,	67.14,	1.17],
[30,	31.14,	22.00,	91.14,	62.71,	0.00],
[31,	33.00,	21.86,	88.00,	50.43,	0.00],
[38,	22.9,	14.1,	35.4,	17.0,	0.5]]

 
#Target variables
Y = [13.6,
16.5,
12.4,
14.6,
14.6,
16.5,
13.3,
28.1,
13.5,
15.0,
17.7,
13.7,
22.0,
20.0,
13.9,
18.0,
20.0,
12.8,
6.8,
14.3,
10.9,
19.0,
23.7,
20.7,
8.3,
6.1,
11.2,
48.1,
37.44,
35.02,
31.75,
32.28,
48.52,
34.01,
47.52,
33.75,
23.81,
36.55,
24.9]

@api_view(['GET'])
def dtree(request): 
  #Dependent variable names in the order they appear in every element in X
  fnames= { 0:"Std.Week",1:"Max T °C",2:"Min T°C",3:"RH (%)",4:"MAI %", 5:"Rainfall (mm in the week)"}
  clf = sklearn.tree.DecisionTreeRegressor()
  clf = clf.fit(X,Y)
  treejson = DecisionTreeSerializer(clf,feature_names=fnames)
  return Response(treejson)


@api_view(['GET'])
def sunburst(request):
  fnames= { 0:"Std.Week",1:"Max T °C",2:"Min T°C",3:"RH (%)",4:"MAI %", 5:"Rainfall (mm in the week)"}
  clf = sklearn.tree.DecisionTreeRegressor()
  clf = clf.fit(X,Y)
  treejson = DecisionTreeSerializer(clf,feature_names=fnames,sunburst=True)
  return Response(treejson)  