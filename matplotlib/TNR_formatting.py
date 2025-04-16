## to use 'times new roman' font on subscrpt, kegend, and text

# sudo apt-get install texlive-fonts-extra

# sudo apt install texlive texlive-latex-extra texlive-fonts-recommended dvipng


#example 01
import matplotlib.pyplot as plt
import matplotlib as mpl

# Configure matplotlib to use LaTeX with Times New Roman
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
})

# Example plot with subscript
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1], label=r'$T_{\mathrm{subscript}}$')
ax.set_xlabel(r'$x_{\mathrm{axis}}$')
ax.set_ylabel(r'N$_C$N$_{\mathrm{C}}$x$_{DT\mathrm{Taxis}}$')

ax.text(0.5, 0.5, r'$A_{\mathrm{text}}$')
ax.legend()

plt.show()


#example 02
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True, 'font.size': 25, 
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "text.latex.preamble": r"""
        \usepackage{amsmath}
        \renewcommand{\rmdefault}{ptm}  % Use Times (ptm) instead of EC fonts
        \renewcommand{\sfdefault}{phv}
    """,
})

# Example usage
fig, ax = plt.subplots(figsize=(8,6))
ax.plot([0, 1], [0, 1], label=r'N$_C$T$T_{\mathrm{test}}$' )
ax.set_xlabel(r'N$_C$N$_{\mathrm{C}}$x$_{DT\mathrm{Taxis}}$')
ax.set_ylabel(r't/$\tau_{DT\mathrm{Daxis}}$')

ax.text(0.5, 0.5, 'Pe = 100')
plt.legend()
plt.show()


#example 03
import matplotlib.pyplot as plt
import matplotlib as mpl

# Configure matplotlib to use LaTeX with Times New Roman
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    'font.size': 14,
    'axes.labelsize': 16,
    'axes.titlesize': 8,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'lines.linewidth': 1.0,
    'axes.linewidth': 0.7,
    'xtick.major.width': 0.7,
    'ytick.major.width': 0.7,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
    'figure.dpi': 800,
    'figure.constrained_layout.use': True,
    'figure.constrained_layout.h_pad': 0.1,
    'figure.constrained_layout.w_pad': 0.1
})

# Example plot with subscript
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1], label=r'$T_{\mathrm{subscript}}$')
ax.set_xlabel(r'$x_{\mathrm{axis}}$')
ax.set_ylabel(r'N$_C$N$_{\mathrm{C}}$x$_{DT\mathbf{Taxis}}$')

ax.text(0.5, 0.5, r'$A_{\mathrm{text}}$')
ax.legend()

plt.show()
