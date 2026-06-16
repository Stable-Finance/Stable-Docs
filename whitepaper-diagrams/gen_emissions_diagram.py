"""Generate the RATES emissions / total-supply chart.

Model (RATES Whitepaper v0.1, Section 5.2):
  - Genesis supply S0 = 1.0B
  - Year-n emission rate r_n = 0.12 * 0.88**(n-1)   (12% in Y1, decaying at 0.88)
  - Emission base does NOT compound: E_n = r_n * S0
  - Cumulative supply S(t) = 2 - 0.88**t   (so S(0)=1.0B, S(10)=1.72B, S(inf)=2.0B)
  - Cumulative emissions sum to exactly 1B, capping total supply at exactly 2.0B.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Stable brand palette (trystable.co/brand)
EMIT = "#413218"   # annual emission rate — brand dark brown
SUPP = "#b38533"   # cumulative supply — brand gold/bronze
DARK = "#413218"   # text — brand dark brown
GRAY = "#7c6f58"   # subtitle / asymptote — brand taupe
CREAM = "#f0e8db"  # brand cream (background tint)

t = np.linspace(0, 25, 500)
rate = np.where(t < 1, 0.12, 0.12 * 0.88 ** (t - 1)) * 100   # percent
supply = 2 - 0.88 ** t                                       # billions

fig, ax1 = plt.subplots(figsize=(7.2, 4.4), dpi=110)
ax2 = ax1.twinx()

# --- emission rate (left axis, %) ---
ax1.plot(t, rate, color=EMIT, lw=2.4, zorder=3)
ax1.set_ylim(0, 13)
ax1.set_yticks([0, 3, 6, 9, 12])
ax1.set_yticklabels(["0%", "3%", "6%", "9%", "12%"], color=DARK, fontsize=9)
ax1.set_ylabel("Annual emission rate", color=DARK, fontsize=10)
ax1.set_xlim(0, 25)
ax1.set_xticks([0, 5, 10, 15, 20, 25])
ax1.set_xticklabels(["Year 0", "5", "10", "15", "20", "25"], color=DARK, fontsize=9)
ax1.set_xlabel("Year", color=DARK, fontsize=10)

# --- cumulative supply (right axis, B; ticks hidden, scaled to match layout) ---
ax2.plot(t, supply, color=SUPP, lw=2.4, zorder=3)
ax2.set_ylim(0.42, 2.85)
ax2.axhline(2.0, color=GRAY, ls=(0, (5, 4)), lw=1.1, zorder=1)
ax2.set_yticks([])

# --- annotations ---
ax1.annotate("Year 1: 12%", xy=(1, 12), xytext=(1.4, 11.9),
             color=DARK, fontsize=9, va="center")
ax1.annotate("Year 10: 3.80%", xy=(10, 3.8), xytext=(10.4, 4.1),
             color=DARK, fontsize=9, va="center")
ax2.annotate("Supply at TGE: 1.0B", xy=(0, 1.0), xytext=(0.4, 0.93),
             color=DARK, fontsize=9, va="center")
ax2.annotate("Year 10: 1.72B", xy=(10, 1.72), xytext=(10.4, 1.60),
             color=DARK, fontsize=9, va="center")
ax2.text(25.3, 2.0, "2.0B supply\nasymptote", color=GRAY, fontsize=9,
         va="center", ha="left")

# --- title / subtitle ---
ax1.text(0.0, 1.13, "RATES emissions and total supply trajectory",
         transform=ax1.transAxes, color=DARK, fontsize=13, fontweight="bold")
ax1.text(0.0, 1.05, "Annual rate decays at 0.88 ratio; cumulative supply asymptotes at 2.0B",
         transform=ax1.transAxes, color=GRAY, fontsize=9.5)

# --- legend ---
handles = [Line2D([0], [0], color=EMIT, lw=2.4, label="Annual emission rate"),
           Line2D([0], [0], color=SUPP, lw=2.4, label="Cumulative supply")]
ax1.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.13),
           ncol=2, frameon=False, fontsize=9.5)

for ax in (ax1, ax2):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
ax1.spines["left"].set_color("#cdbfa6")
ax1.spines["bottom"].set_color("#cdbfa6")
ax1.tick_params(colors="#cdbfa6")

fig.subplots_adjust(left=0.10, right=0.84, top=0.82, bottom=0.16)

for out in ["whitepaper-diagrams/emissions_diagram.png",
            ".gitbook/assets/emissions_diagram.png"]:
    fig.savefig(out, dpi=110, facecolor="white")
    print("wrote", out)
