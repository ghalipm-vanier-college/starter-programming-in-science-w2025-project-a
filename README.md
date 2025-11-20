-- # starter-programming-in-science-w2025-project-a

# Programming in Science – Project  
This project focuses on using **NumPy, Pandas, Matplotlib, 3D plotting, animation**, and matrix operations used in scientific computing.

Where plots or animations are required, the auto-tests verify only that the functions run without errors.  
**Students must include screenshots of plots/animations in their submission.**

---

#  Questions

## (10%) Plot a Polynomial Using NumPy (`np.linspace`)
Generate x-values in [-10, 10], compute  
\$[
y = 3x^3 - 2x^2 + x - 5
\$]
and plot the function.

Example:
```python
plot_polynomial()
```

---

## 2️⃣ (10%) Compare Functions Using `np.arange`

Use `np.arange(-10, 10, 0.02)` to compute:

* \$[ y_1 = x^2 \$]
* \$[ y_2 = e^{-x}\sin(x) \$]

Plot both curves together.

Example:

```python
plot_compare_functions()
```

---

## 3️⃣ (10%) Read Array From `.txt` and Plot

Read a space-separated `.txt` file into a NumPy array and plot it.

Example:

```python
plot_array_from_txt("data/array_sample.txt")
```

---

## 4️⃣ (10%) Monthly Temperature Plot (CSV + Pandas)

Read a CSV file of `Month, Temperature` and plot as a line graph.

Example:

```python
plot_monthly_temperature("data/temperature.csv")
```

---

## 5️⃣ (10%) Scatter Plot from CSV

Read two numerical columns from CSV and create a scatter plot.

Example:

```python
plot_scatter_from_csv("data/scatter.csv")
```

---

## 6️⃣ (10%) Heatmap from a 2D Numeric File

Load a 2D matrix from `.txt` or `.csv` and display a heatmap.

Example:

```python
plot_heatmap("data/matrix.txt")
```

---

## 7️⃣ (10%) Check Matrix Invertibility

Read a matrix from `.txt`, compute determinant, return True/False.

Example:

```python
is_invertible("data/invertible.txt")
```

---

## 8️⃣ (10%) Check Whether Two Matrices Are Orthogonal

Two matrices A and B are orthogonal if:
\$[
A^T B \approx 0
\$]

Example:

```python
are_orthogonal(A, B)
```

---

## 9️⃣ (10%) 3D Surface Plot

Let x and y be in (-5, 5). Compute
\$[
z = \sqrt{x^2 + y^2}
\$]
Use `meshgrid` and plot a 3D surface.

Example:

```python
plot_surface()
```

---

## 🔟 (10%) Animation of a Moving Point

Let step size (h = 0.01).
Animate a point moving along:
\$[
y = \sin(x)
\$]

Example:

```python
animate_sine_wave()
```

---

# ▶ Run Tests

```
pytest
```

---
