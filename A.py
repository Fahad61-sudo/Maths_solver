import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np, sympy as sp, re

class MathSolver:
    def __init__(self, root):
        self.root=root; self.root.title("College Math Solver"); self.root.geometry("500x400")
        self.mode=tk.StringVar(value="calculus")
        self.content=ttk.Frame(root); self.content.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.create_gui(); self.create_calculus()
    def create_gui(self):
        ttk.Label(self.root,text="College Math Solver",font=('Arial',16,'bold')).pack(pady=10)
        f=ttk.Frame(self.root); f.pack(pady=10)
        for text,val in [("Calculus","calculus"),("Linear Algebra","linear_algebra"),("Integral Solver","integral")]:
            ttk.Radiobutton(f,text=text,variable=self.mode,value=val,command=self.switch).pack(side=tk.LEFT,padx=5)
    def switch(self):
        for w in self.content.winfo_children(): w.destroy()
        {"calculus":self.create_calculus,"linear_algebra":self.create_linear,"integral":self.create_integral}[self.mode.get()]()
    def create_calculus(self):
        ttk.Label(self.content,text="Derivative Solver",font=('Arial',12,'bold')).pack(pady=5)
        f=ttk.Frame(self.content); f.pack(pady=10,fill=tk.X)
        ttk.Label(f,text="f(x):").pack(side=tk.LEFT); self.func=ttk.Entry(f,width=30); self.func.pack(side=tk.LEFT,padx=5)
        self.func.insert(0,"x**2 + sin(x)")
        ttk.Button(f,text="Derivative",command=self.derivative).pack(side=tk.LEFT,padx=5)
        self.res=tk.Text(self.content,height=8,width=50); self.res.pack(pady=10,fill=tk.BOTH,expand=True)
    def create_linear(self):
        ttk.Label(self.content,text="Linear Algebra Solver",font=('Arial',12,'bold')).pack(pady=5)
        f=ttk.Frame(self.content); f.pack(pady=10)
        ttk.Label(f,text="Matrix A:").pack(); self.mat=tk.Text(f,height=4,width=40); self.mat.pack(pady=5)
        self.mat.insert("1.0","1,2,3\n4,5,6\n7,8,9")
        ttk.Label(f,text="Vector b:").pack(); self.vec=ttk.Entry(f,width=40); self.vec.pack(pady=5); self.vec.insert(0,"1,2,3")
        ops=[("Det",self.det),("Inv",self.inv),("Solve",self.solve),("Eigen",self.eigen)]
        of=ttk.Frame(f); of.pack(pady=5)
        [ttk.Button(of,text=t,command=c).pack(side=tk.LEFT,padx=2) for t,c in ops]
        self.mres=tk.Text(self.content,height=8,width=50); self.mres.pack(pady=10,fill=tk.BOTH,expand=True)
    def create_integral(self):
        ttk.Label(self.content,text="Integral Solver",font=('Arial',12,'bold')).pack(pady=5)
        f=ttk.Frame(self.content); f.pack(pady=10,fill=tk.X)
        ttk.Label(f,text="f(x):").pack(side=tk.LEFT); self.ifunc=ttk.Entry(f,width=20); self.ifunc.pack(side=tk.LEFT,padx=5); self.ifunc.insert(0,"x**2")
        ttk.Label(f,text="From:").pack(side=tk.LEFT); self.a=ttk.Entry(f,width=5); self.a.pack(side=tk.LEFT,padx=2); self.a.insert(0,"0")
        ttk.Label(f,text="To:").pack(side=tk.LEFT); self.b=ttk.Entry(f,width=5); self.b.pack(side=tk.LEFT,padx=2); self.b.insert(0,"1")
        ttk.Button(f,text="Integrate",command=self.integrate).pack(side=tk.LEFT,padx=10)
        self.ires=tk.Text(self.content,height=10,width=50); self.ires.pack(pady=10,fill=tk.BOTH,expand=True)
    def derivative(self):
        try:
            x=sp.Symbol('x'); f=sp.sympify(self.func.get()); d1=sp.diff(f,x); d2=sp.diff(f,x,2)
            t=f"f(x)={f}\n\nf'(x)={d1}\nSimplified:{sp.simplify(d1)}\n\nf''(x)={d2}"
            self.res.delete(1.0,tk.END); self.res.insert(1.0,t)
        except Exception as e: messagebox.showerror("Error",e)
    def parse_mat(self,t): return np.array([[float(e) for e in re.split(r'[,\s]+',r.strip()) if e] for r in t.strip().split('\n') if r.strip()])
    def parse_vec(self,t): return np.array([float(e) for e in re.split(r'[,\s]+',t.strip()) if e])
    def det(self):
        try:
            A=self.parse_mat(self.mat.get("1.0",tk.END)); d=np.linalg.det(A)
            self.show(self.mres,f"A:\n{A}\nDet={d:.6f}\nInvertible={abs(d)>1e-10}")
        except Exception as e: messagebox.showerror("Error",e)
    def inv(self):
        try:
            A=self.parse_mat(self.mat.get("1.0",tk.END)); d=np.linalg.det(A)
            if abs(d)<1e-10: return messagebox.showwarning("Warning","Singular Matrix")
            I=np.linalg.inv(A); self.show(self.mres,f"A:\n{A}\n\nA⁻¹:\n{I}\n\nA×A⁻¹:\n{np.round(A@I,6)}")
        except Exception as e: messagebox.showerror("Error",e)
    def solve(self):
        try:
            A=self.parse_mat(self.mat.get("1.0",tk.END)); b=self.parse_vec(self.vec.get())
            if A.shape[0]!=len(b): return messagebox.showerror("Error","Dim mismatch")
            x=np.linalg.solve(A,b); self.show(self.mres,f"A:\n{A}\nb:{b}\nx:{x}\nAx:{A@x}")
        except np.linalg.LinAlgError: messagebox.showerror("Error","Singular matrix")
        except Exception as e: messagebox.showerror("Error",e)
    def eigen(self):
        try:
            A=self.parse_mat(self.mat.get("1.0",tk.END)); v,e=np.linalg.eig(A)
            s=f"A:\n{A}\n\nEigenvalues:\n"+'\n'.join([f"λ{i+1}={x:.6f}" for i,x in enumerate(v)])+f"\n\nEigenvectors:\n{e}"
            self.show(self.mres,s)
        except Exception as e: messagebox.showerror("Error",e)
    def integrate(self):
        try:
            x=sp.Symbol('x'); f=sp.sympify(self.ifunc.get()); a,b=float(self.a.get()),float(self.b.get())
            defi=sp.integrate(f,(x,a,b)); indef=sp.integrate(f,x)
            s=f"f(x)={f}\n\n∫f(x)dx={indef}+C\n\nFrom {a} to {b}: {defi}\nValue:{float(defi):.6f}"
            self.show(self.ires,s)
        except Exception as e: messagebox.showerror("Error",e)
    def show(self,box,text): box.delete(1.0,tk.END); box.insert(1.0,text)

if __name__=="__main__":
    r=tk.Tk(); MathSolver(r); r.mainloop()
