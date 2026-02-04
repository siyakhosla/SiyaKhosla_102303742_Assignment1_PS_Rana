This package is built as a submission to **Assignment 1**

Submitted by: Siya Khosla(102303735)

---

##  Definition

**TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making (MCDM) method used to rank alternatives by selecting the option that is closest to the ideal solution and farthest from the worst (negative ideal) solution.

---

##  Web Application

You can access the deployed website here:  
[Click here to open the website](https://tourmaline-panda-0febac.netlify.app/)



---

##  Installation

Use the package manager **pip** to install the package:

```bash
pip install Topsis-Siya Khosla-102303742
```

---

##  Usage

```bash
topsis data.csv 1,1,1,1,1 +,+,-,+,+ result.csv
```

### Where:

- `data.csv` → Input file  
- `Weights` → Weights assigned to each criterion  
- `Impacts` → Optimization type for each criterion  
  - `+` → Maximize  
  - `-` → Minimize  
- `result.csv` → Output file to store results  

---

##  Example

###  Input Dataset (`data.csv`)

| Fund Name | P1 | P2 | P3 | P4 | P5 |
|----------|----|----|----|----|----|
| M1 | 0.72 | 0.54 | 4.1 | 43.2 | 12.05 |
| M2 | 0.69 | 0.51 | 3.6 | 59.8 | 15.92 |
| M3 | 0.67 | 0.44 | 5.0 | 62.1 | 17.10 |
| M4 | 0.78 | 0.61 | 3.9 | 41.4 | 11.80 |
| M5 | 0.83 | 0.68 | 5.4 | 39.6 | 11.35 |
| M6 | 0.80 | 0.65 | 5.6 | 55.9 | 15.88 |
| M7 | 0.86 | 0.74 | 6.5 | 52.3 | 14.70 |
| M8 | 0.92 | 0.85 | 5.7 | 66.2 | 18.30 |

**Weights:**
```
1,1,1,1,1
```

**Impacts:**
```
+,+,-,+,+
```

---

###  Output After Applying TOPSIS (`result.csv`)

| Fund Name | P1 | P2 | P3 | P4 | P5 | Topsis Score | Rank |
|----------|----|----|----|----|----|--------------|------|
| M1 | 0.72 | 0.54 | 4.1 | 43.2 | 12.05 | 0.5104539221 | 4 |
| M2 | 0.69 | 0.51 | 3.6 | 59.8 | 15.92 | 0.2630880959 | 8 |
| M3 | 0.67 | 0.44 | 5.0 | 62.1 | 17.10 | 0.3036022644 | 7 |
| M4 | 0.78 | 0.61 | 3.9 | 41.4 | 11.80 | 0.5516228388 | 3 |
| M5 | 0.83 | 0.68 | 5.4 | 39.6 | 11.35 | 0.6583723311 | 1 |
| M6 | 0.80 | 0.65 | 5.6 | 55.9 | 15.88 | 0.4956641039 | 5 |
| M7 | 0.86 | 0.74 | 6.5 | 52.3 | 14.70 | 0.6298813640 | 2 |
| M8 | 0.92 | 0.85 | 5.7 | 66.2 | 18.30 | 0.4851147686 | 6 |

---

##  Notes

The package handles the following:

- Correct number of parameters (input file, weights, impacts, output file)
- Appropriate error messages for invalid inputs
- Handling of File Not Found exception
- Input file must contain three or more columns
- From second column onward, values must be numeric
- Number of weights, impacts, and criteria columns must be equal
- Impacts must be either `+` or `-`
- Weights and impacts must be comma-separated
