<h1 align="center" style="font-weight: bold;">Atividade Prática 02 - Processamento Digital de Imagens</h1>

<p align="center">
    <b>This repository contains the implementation of an academic activity of the discipline "Digital Image Processing" (UFPI - 2025.1). The objective is to apply different enhancement and filtering techniques in digital images, using the Python programming language.</b>
</p>

<h2 id="started">🚀 Getting started</h2>

<h3>Prerequisites</h3>

Prerequisites to run this project:

- [Python](https://www.python.org/)
- [Git 2](https://git-scm.com/downloads)

<h3>libraries</h3>

```bash
pip install opencv-python
pip install numpy
pip install matplotlib
```

<h3>Cloning</h3>

```bash
git clone https://github.com/SamuelFortes/Tarefa-de-PDI.git
```

## 📚 Activity Description

<h3>The activity is divided into two main parts:</h3>

### 1. Processing the `lena_gray.bmp` image

The following techniques were applied:

- **Laplacian Filter** – Edge detection by second derivative.
- **Unsharp Masking** – Sharpening mask based on the subtraction of the smoothed image.
- **Highboost Filtering** – Enhancement with reinforcement of details, controlled by an `A` factor.

- **Edge detection with:**
- **Prewitt filter**
- **Sobel filter**
- Visual comparison between the two methods

### 2. Filtering the image `lena_ruido.bmp`

Different **smoothing masks** were applied:

- Filter with 3x3 mask weighted by (1/5)
- Filter with standard 3x3 mean (1/9)
- Filter with centered weights (1/32)
- Filter with centered weights (1/8)
- **Median Filter** (reference for comparison)

## 🧠 Formulas and Concepts

### 🔹 Laplacian Filter
- Laplacian = d²f/dx² + d²f/dy²

### 🔹 Unsharp Masking
- Unsharp = f(x, y) + α * (f(x, y) - f_smoothed(x, y))

### 🔹 Highboost Filtering
- Highboost = f(x, y) + (A - 1) * (f(x, y) - f_smoothed(x, y))

### 🔹 Edge Detection (Prewitt and Sobel)
- Convolutional masks applied in the X and Y directions to compute local gradients.


<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
