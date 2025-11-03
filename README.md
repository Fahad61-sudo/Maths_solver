# 🧮 College Math Solver

**College Math Solver** is a Python-based desktop application built with **Tkinter**, **NumPy**, and **SymPy**.  
It is designed to help students quickly solve **Calculus**, **Linear Algebra**, and **Integration** problems through an intuitive and interactive interface.  
This project was developed as part of a **Hackathon** submission.

---

## 🚀 Features

### 🧠 1. Calculus Mode
- Compute **first** and **second derivatives**.
- Simplify expressions symbolically.
- Supports trigonometric, exponential, and polynomial functions.

### 🧩 2. Linear Algebra Mode
- Compute **Determinant**, **Inverse**, and **Eigenvalues/Eigenvectors**.
- Solve systems of linear equations \(Ax = b\).
- Auto-checks for **singular matrices**.

### ∫ 3. Integral Solver
- Perform **definite** and **indefinite** integration.
- Symbolic and numeric evaluation using **SymPy**.
- Supports variable limits and complex expressions.

---

## 🖥️ User Interface

The app is divided into three modes (accessible via radio buttons):

| Mode | Functionality |
|------|----------------|
| **Calculus** | Derivatives and simplifications |
| **Linear Algebra** | Matrix and vector computations |
| **Integral Solver** | Definite and indefinite integrals |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries Used:**
  - `tkinter` → GUI framework
  - `numpy` → Numerical linear algebra
  - `sympy` → Symbolic mathematics
  - `re` → Input parsing and cleanup

---

## 🧩 Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/Fahad61-sudo/Maths_solver.git
cd Maths_solver
```

### 2. Install dependencies
Make sure you have Python 3.x installed.  
Then install required packages:
```bash
pip install numpy sympy
```

### 3. Run the application
```bash
python maths_solver.py
```

---

## 🧠 Example Use Cases

### Example 1 — Derivative
Input:  
`x**2 + sin(x)`  
Output:  
```
f'(x) = 2*x + cos(x)
f''(x) = -sin(x) + 2
```

### Example 2 — Linear System
Matrix A:
```
1,2,3
4,5,6
7,8,9
```
Vector b:  
`1,2,3`

Output:
```
Singular matrix (no unique solution)
```

---

## 🏆 Hackathon Theme

This project demonstrates how **mathematical problem solving** can be made more **accessible and interactive** through Python.  
It encourages students to **visualize core mathematical operations** with an easy GUI.

---

## 👨‍💻 Author

**Fahad Ibrar**  
📧 [ibrarfahad29@gmail.com](mailto:ibrarfahad29@gmail.com)  
🌐 [GitHub - Fahad61-sudo](https://github.com/Fahad61-sudo)

---

## 📜 License

This project is released under the **MIT License**.  
You are free to use, modify, and distribute it with proper attribution.

---

> _“Mathematics is not about numbers, equations, or algorithms: it’s about understanding.”_
