This package is built as a submission to Assignment 1.
Submitted by:
Siya Khosla (102303742)

Definition
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making (MCDM) method used to rank alternatives by identifying the option that is closest to the ideal solution and farthest from the worst (negative ideal) solution.

Web Application
This package can also be used as a WebApp
Installation
Use the Python package manager pip to install the package:


 Usage


where:
data.csv → Input dataset


1,1,1,1,1 → Weights assigned to each criterion


+,+,-,+,+ → Impacts for each criterion (+ for maximization, - for minimization)


result.csv → Output file to store the results

       Example
  Input Dataset (data.csv)

Weights: 1,1,1,1,1
Impacts: +,+,+,-,+


Output after applying TOPSIS (result.csv)

Notes
The package handles the following:
Correct number of parameters (input file, weights, impacts, output file)
Appropriate error messages for invalid inputs
Handling of File Not Found exception
Input file must contain three or more columns
From second to last columns must contain numeric values only
Number of weights, impacts and criteria columns must be the same
Impacts must be either + or -
Weights and impacts must be separated by commas
