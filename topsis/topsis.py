import sys
import pandas as pd
import numpy as np
import os

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <inputfile> <weights> <impacts> <outputfile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights_input = sys.argv[2]
    impacts_input = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.exists(input_file):
        print("Error: Input file not found")
        sys.exit(1)

    try:
        df = pd.read_csv(input_file)
    except:
        print("Error: Unable to read input file")
        sys.exit(1)

    if df.shape[1] < 3:
        print("Error: Input file must contain three or more columns")
        sys.exit(1)

    data = df.iloc[:, 1:]

    try:
        data = data.astype(float)
    except:
        print("Error: Criteria columns must be numeric")
        sys.exit(1)

    weights = weights_input.split(',')
    impacts = impacts_input.split(',')

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        print("Error: Number of weights, impacts and criteria columns must be same")
        sys.exit(1)

    try:
        weights = np.array(weights, dtype=float)
    except:
        print("Error: Weights must be numeric")
        sys.exit(1)

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be + or -")
            sys.exit(1)

    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    d_plus = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_minus = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    denom = d_plus + d_minus
    denom[denom == 0] = 1e-10

    score = d_minus / denom

    df["Topsis Score"] = score
    df["Rank"] = score.rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully")

if __name__ == "__main__":
    main()
