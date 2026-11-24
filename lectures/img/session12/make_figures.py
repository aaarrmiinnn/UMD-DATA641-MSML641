"""Draws the diagrams used in lectures/session12_frontier_nlp.ipynb.

Run from anywhere:  python lectures/img/session12/make_figures.py
Each function writes one PNG next to this file.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

OUT = Path(__file__).parent

RED, PALE_RED = "#E21833", "#FBDDE1"
BLUE, PALE_BLUE = "#2B6CB0", "#DCE9F7"
GREEN, PALE_GREEN = "#2E8B57", "#DDF1E4"
GOLD, PALE_GOLD = "#B8860B", "#FFF1BF"
INK, GRAY, LIGHT = "#222222", "#8A8A8A", "#EDEDED"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})


def canvas(w=110, h=45):
    """A blank drawing area where 14 units = 1 inch, so shapes keep their proportions.

    Text is sized in points, so a smaller canvas makes the labels read larger on a slide.
    """
    fig, ax = plt.subplots(figsize=(w / 14, h / 14))
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    return fig, ax


def box(ax, x, y, w, h, text="", fc=LIGHT, ec=INK, fs=12, color=INK, lw=1.4, weight="normal", hatch=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.7",
                                fc=fc, ec=ec, lw=lw, hatch=hatch))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=color, weight=weight)


def arrow(ax, x1, y1, x2, y2, color=INK, lw=1.8, rad=0.0, style="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=16,
                                 color=color, lw=lw, connectionstyle=f"arc3,rad={rad}",
                                 shrinkA=0, shrinkB=0))


def label(ax, x, y, text, fs=12, color=INK, ha="center", va="center", weight="normal", style="normal"):
    ax.text(x, y, text, fontsize=fs, color=color, ha=ha, va=va, weight=weight, style=style)


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, facecolor="white", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


# ---------------------------------------------------------------- Part I

def rope():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5))
    step = 20  # degrees of rotation per position
    for ax, (m, n) in zip(axes, [(2, 5), (10, 13)]):
        t = np.linspace(0, 2 * np.pi, 200)
        ax.plot(np.cos(t), np.sin(t), color=LIGHT, lw=2)
        for pos, col, word in [(m, BLUE, "cat"), (n, RED, "sat")]:
            a = np.deg2rad(step * pos)
            ax.annotate("", xy=(np.cos(a), np.sin(a)), xytext=(0, 0),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=2.5, mutation_scale=18))
            ax.text(1.62 * np.cos(a), 1.42 * np.sin(a), f'"{word}"\nposition {pos}',
                    color=col, ha="center", va="center", fontsize=12)
        arc = np.deg2rad(np.linspace(step * m, step * n, 50))
        ax.plot(0.42 * np.cos(arc), 0.42 * np.sin(arc), color=INK, lw=1.5)
        mid = np.deg2rad(step * (m + n) / 2)
        ax.text(0.68 * np.cos(mid), 0.68 * np.sin(mid), "60°", ha="center", va="center", fontsize=12)
        ax.set_xlim(-2.3, 2.3)
        ax.set_ylim(-1.75, 1.75)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(f"Positions {m} and {n}", fontsize=13, weight="bold")
    fig.tight_layout()
    save(fig, "rope.png")


def activations():
    x = np.linspace(-5, 5, 400)
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.plot(x, np.maximum(x, 0), color=GRAY, lw=2.5, label="ReLU: exactly 0 below zero")
    ax.plot(x, x / (1 + np.exp(-x)), color=RED, lw=2.5, label="SiLU: smooth, dips slightly below zero")
    ax.axhline(0, color=INK, lw=0.6)
    ax.axvline(0, color=INK, lw=0.6)
    ax.set_xlabel("input")
    ax.set_ylabel("output")
    ax.set_ylim(-1, 5)
    ax.legend(frameon=False, loc="upper left")
    ax.grid(True, alpha=0.25)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "activations.png")


def gqa():
    fig, ax = canvas(110, 44)
    panels = [("Multi-head (MHA)", 8, "8 K/V sets stored per token"),
              ("Grouped-query (GQA)", 2, "2 K/V sets stored per token\n4x smaller cache"),
              ("Multi-query (MQA)", 1, "1 K/V set stored per token\n8x smaller cache")]
    for p, (title, n_kv, note) in enumerate(panels):
        x0 = 3 + p * 36
        label(ax, x0 + 15.5, 41, title, fs=13, weight="bold")
        qx = [x0 + 1.7 + i * 4 for i in range(8)]
        span = 31 / n_kv
        for g in range(n_kv):
            bx = x0 + g * span + 0.4
            box(ax, bx, 12, span - 0.8, 6, "K, V" if n_kv < 8 else "", fc=PALE_RED, ec=RED, fs=11)
        for i, x in enumerate(qx):
            g = i * n_kv // 8
            ax.plot([x, x0 + g * span + span / 2], [31.2, 18], color=GRAY, lw=1.1, zorder=1)
            ax.add_patch(plt.Circle((x, 32.5), 1.4, fc=PALE_BLUE, ec=BLUE, lw=1.4, zorder=2))
        label(ax, x0 + 15.5, 36.6, "8 query heads", fs=11, color=BLUE)
        label(ax, x0 + 15.5, 6, note, fs=11, color=RED)
    save(fig, "gqa.png")


def moe():
    fig, ax = canvas(112, 46)
    box(ax, 1, 19, 13, 8, "token\nvector", fc=PALE_BLUE, ec=BLUE)
    arrow(ax, 14, 23, 20, 23)
    box(ax, 20, 18, 15, 10, "router\npicks 2 of 8", fc=PALE_GOLD, ec=GOLD)
    active = {2: "0.7", 5: "0.3"}
    for i in range(8):
        y = 41 - i * 5.3
        on = i in active
        box(ax, 50, y - 2, 17, 4.2, f"expert {i + 1}", fc=PALE_RED if on else LIGHT,
            ec=RED if on else GRAY, color=INK if on else GRAY, fs=11)
        if on:
            arrow(ax, 35, 23, 50, y, color=RED)
            arrow(ax, 67, y, 81, 23, color=RED)
            label(ax, 74, y + (2.3 if y > 23 else -2.3) + (23 - y) * 0.42, f"x {active[i]}", fs=11, color=RED)
    box(ax, 81, 18, 14, 10, "add them\nup", fc=PALE_GOLD, ec=GOLD)
    arrow(ax, 95, 23, 100.5, 23)
    label(ax, 102, 23, "output", fs=12, ha="left")
    label(ax, 27.5, 10, "the other 6 experts\nare not run\nfor this token", fs=11, color=GRAY)
    save(fig, "moe.png")


def ssm():
    fig, ax = canvas(112, 42)
    words = ["The", "cat", "sat", "on", "the", "mat"]
    # attention
    label(ax, 26, 39.5, "Attention", fs=13, weight="bold")
    for i, wd in enumerate(words):
        last = i == 5
        box(ax, 2 + i * 8.3, 10, 7, 5.5, wd, fc=PALE_RED if last else LIGHT, ec=RED if last else INK)
    for i in range(5):
        arrow(ax, 2 + 5 * 8.3 + 3.5, 15.5, 2 + i * 8.3 + 3.5, 15.7, color=RED, lw=1.4, rad=0.45)
    label(ax, 26, 4, "The new token looks back at every earlier token.\nMemory grows with the length of the text.", fs=11)
    # state space model
    label(ax, 85, 39.5, "State space model (Mamba)", fs=13, weight="bold")
    for i, wd in enumerate(words):
        x = 61 + i * 8.3
        box(ax, x, 10, 7, 5.5, wd, fc=LIGHT)
        box(ax, x, 24, 7, 5.5, "state", fc=PALE_BLUE, ec=BLUE, fs=10)
        arrow(ax, x + 3.5, 15.5, x + 3.5, 24, color=BLUE, lw=1.4)
        if i < 5:
            arrow(ax, x + 7, 26.75, x + 8.3, 26.75, color=BLUE, lw=1.4)
    label(ax, 85, 4, "Each token updates one state of a fixed size.\nMemory stays the same however long the text is.", fs=11)
    ax.plot([56, 56], [2, 40], color=LIGHT, lw=1.5)
    save(fig, "ssm.png")


# ---------------------------------------------------------------- Part II

def gpu_memory():
    fig, ax = canvas(110, 36)
    box(ax, 2, 20, 28, 11, "Arithmetic units\ndo the multiplying", fc=PALE_BLUE, ec=BLUE)
    box(ax, 39, 20, 24, 11, "On-chip memory\ntiny, very fast", fc=PALE_GREEN, ec=GREEN)
    box(ax, 75, 20, 33, 11, "Main GPU memory\nabout 80 GB, slow", fc=PALE_RED, ec=RED)
    arrow(ax, 30, 25.5, 39, 25.5, color=GREEN, style="<|-|>")
    arrow(ax, 63, 25.5, 75, 25.5, color=RED, lw=3, style="<|-|>")
    label(ax, 34.5, 28.3, "fast", fs=11, color=GREEN)
    label(ax, 69, 28.8, "slow", fs=12, color=RED, weight="bold")
    label(ax, 16, 13.5, "the cook", fs=12, color=GRAY, style="italic")
    label(ax, 51, 13.5, "the counter", fs=12, color=GRAY, style="italic")
    label(ax, 91.5, 13.5, "the pantry down the hall", fs=12, color=GRAY, style="italic")
    label(ax, 55, 5, "The model's weights live in main memory. Every fetch is a walk to the pantry.", fs=12)
    save(fig, "gpu_memory.png")


def busy_waiting():
    fig, ax = plt.subplots(figsize=(8.2, 2.7))
    names = ["Writing the answer, 1 user", "Writing the answer, 64 users at once", "Reading a 2,000-token prompt"]
    vals = [1, 64, 2000]
    cols = [RED, GOLD, GREEN]
    ax.barh(names, [v - 0.5 for v in vals], left=0.5, color=cols, height=0.55)
    for i, v in enumerate(vals):
        ax.text(v * 1.2, i, f"{v:,}", va="center", fontsize=12)
    ax.set_xscale("log")
    ax.set_xlim(0.5, 12000)
    ax.set_xticks([1, 10, 100, 1000])
    ax.set_xticklabels(["1", "10", "100", "1,000"])
    ax.set_xlabel("Multiplications per weight fetched from memory (log scale)")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "busy_waiting.png")


def flash_attention():
    fig, ax = canvas(110, 44)
    n, c = 12, 2.5
    for p, x0 in enumerate([10, 70]):
        for i in range(n):
            for j in range(n):
                tile = p == 1 and 3 <= i < 6 and 6 <= j < 9
                fc = PALE_RED if p == 0 else (RED if tile else "#F6F6F6")
                ax.add_patch(Rectangle((x0 + i * c, 7 + j * c), c, c, fc=fc, ec="white", lw=0.8))
        ax.add_patch(Rectangle((x0, 7), n * c, n * c, fc="none", ec=INK, lw=1.2))
    label(ax, 25, 41, "Standard attention", fs=13, weight="bold")
    label(ax, 85, 41, "Flash Attention", fs=13, weight="bold")
    label(ax, 25, 3, "Whole N x N score matrix is written to\nmain memory, then read back", fs=11)
    label(ax, 85, 3, "One small tile at a time, kept in\nfast on-chip memory", fs=11)
    arrow(ax, 45, 22, 65, 22, color=GRAY)
    label(ax, 55, 25, "same result", fs=11, color=GRAY)
    save(fig, "flash_attention.png")


def multi_gpu():
    fig, ax = canvas(111, 42)
    panels = [("Data parallel", ["whole model\nexamples 1 to 8", "whole model\nexamples 9 to 16", "whole model\nexamples 17 to 24"],
               "Same model on every GPU,\ndifferent examples", False),
              ("Tensor parallel", ["1/3 of every matrix", "1/3 of every matrix", "1/3 of every matrix"],
               "Each big matrix is cut\nacross the GPUs", False),
              ("Pipeline parallel", ["layers 1 to 27", "layers 28 to 54", "layers 55 to 80"],
               "Different layers on\ndifferent GPUs", True)]
    fills = [(PALE_BLUE, BLUE), (PALE_RED, RED), (PALE_GREEN, GREEN)]
    for p, (title, rows, note, chain) in enumerate(panels):
        x0 = 2 + p * 37
        fc, ec = fills[p]
        label(ax, x0 + 16.5, 39.5, title, fs=13, weight="bold")
        for r, text in enumerate(rows):
            y = 28 - r * 9
            box(ax, x0 + 7, y, 26, 6.5, text, fc=fc, ec=ec, fs=10.5)
            label(ax, x0 + 3, y + 3.25, f"GPU {r + 1}", fs=10, color=GRAY)
            if chain and r < 2:
                arrow(ax, x0 + 20, y, x0 + 20, y - 2.5, color=ec)
        label(ax, x0 + 18, 4, note, fs=11)
    save(fig, "multi_gpu.png")


# ---------------------------------------------------------------- Part III

def request_timeline():
    fig, ax = canvas(112, 44)
    label(ax, 6.5, 27, "model\npasses", fs=11, color=GRAY)
    label(ax, 6.5, 12.5, "KV cache", fs=11, color=GRAY)
    box(ax, 14, 22, 28, 10, "PREFILL\nall 2,000 prompt tokens\nin one pass", fc=PALE_GREEN, ec=GREEN, fs=11)
    box(ax, 14, 10, 28, 5, "K and V for 2,000 tokens", fc=PALE_BLUE, ec=BLUE, fs=10.5)
    for i in range(10):
        x = 44 + i * 6.6
        box(ax, x, 22, 5.6, 10, "1", fc=PALE_RED, ec=RED, fs=11)
        box(ax, x, 10, 5.6, 5, "+1", fc=PALE_BLUE, ec=BLUE, fs=10)
    label(ax, 76.5, 35, "DECODE: one new token per pass", fs=12, color=RED, weight="bold")
    # time to first token
    ax.annotate("", xy=(14, 40), xytext=(42, 40), arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1.3))
    label(ax, 28, 42, "time to first token", fs=11)
    ax.annotate("", xy=(44, 40), xytext=(49.6, 40), arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1.3))
    label(ax, 51.5, 40, "time per output token", fs=11, ha="left")
    arrow(ax, 14, 4, 110, 4, color=GRAY, lw=1.3)
    label(ax, 62, 1.8, "time", fs=11, color=GRAY)
    label(ax, 76.5, 18.5, "every decode pass reads the whole cache and adds one entry", fs=10.5, color=BLUE)
    save(fig, "request_timeline.png")


def batching():
    lengths = dict(A=3, B=8, C=5, D=2, E=4, F=6, G=3, H=5, I=4, J=3, K=6, L=2, M=5, N=4, O=3, P=4)
    names = list(lengths)
    cmap = plt.get_cmap("tab20")
    colors = {n: cmap(i % 20) for i, n in enumerate(names)}
    slots, steps = 4, 14

    def static():
        grid = [[None] * steps for _ in range(slots)]
        t, q = 0, 0
        while t < steps and q < len(names):
            group = names[q:q + slots]
            q += slots
            for s, nm in enumerate(group):
                for k in range(lengths[nm]):
                    if t + k < steps:
                        grid[s][t + k] = (nm, k == 0, t + lengths[nm] <= steps)
            t += max(lengths[n] for n in group)
        return grid

    def continuous():
        # requests join in arrival order, whichever slot frees first
        grid = [[None] * steps for _ in range(slots)]
        free_at = [0] * slots
        for nm in names:
            s = min(range(slots), key=lambda i: (free_at[i], i))
            t = free_at[s]
            if t >= steps:
                break
            for k in range(lengths[nm]):
                if t + k < steps:
                    grid[s][t + k] = (nm, k == 0, t + lengths[nm] <= steps)
            free_at[s] = t + lengths[nm]
        return grid

    fig, ax = canvas(112, 34)
    cw, ch = 3.2, 4.2
    for p, (title, grid) in enumerate([("Static batching", static()), ("Continuous batching", continuous())]):
        x0 = 8 + p * 56
        idle = sum(cell is None for row in grid for cell in row)
        done = len({cell[0] for row in grid for cell in row if cell and cell[2]})
        for s in range(slots):
            label(ax, x0 - 1, 24.3 - s * ch, f"slot {s + 1}", fs=9.5, color=GRAY, ha="right")
            for t in range(steps):
                cell = grid[s][t]
                x, y = x0 + t * cw, 22.2 - s * ch
                if cell is None:
                    ax.add_patch(Rectangle((x, y), cw, ch, fc="white", ec=GRAY, lw=0.6, hatch="///"))
                else:
                    ax.add_patch(Rectangle((x, y), cw, ch, fc=colors[cell[0]], ec="white", lw=0.8))
                    if cell[1]:
                        r, g, b = colors[cell[0]][:3]
                        dark = 0.299 * r + 0.587 * g + 0.114 * b < 0.62
                        label(ax, x + cw / 2, y + ch / 2, cell[0], fs=10, weight="bold",
                              color="white" if dark else INK)
        label(ax, x0 + steps * cw / 2, 31.5, title, fs=13, weight="bold")
        label(ax, x0 + steps * cw / 2, 28.3, f"{idle} of {slots * steps} slot-steps idle, {done} requests finished",
              fs=11, color=RED if p == 0 else GREEN)
        arrow(ax, x0, 7.5, x0 + steps * cw, 7.5, color=GRAY, lw=1.2)
        label(ax, x0 + steps * cw / 2, 5.3, "decode steps", fs=10.5, color=GRAY)
    ax.add_patch(Rectangle((40, 0.3), 3, 2.6, fc="white", ec=GRAY, lw=0.6, hatch="///"))
    label(ax, 44.5, 1.6, "idle GPU slot.  Each letter is one user's request.", fs=10.5, ha="left", color=GRAY)
    save(fig, "batching.png")


def paged():
    fig, ax = canvas(110, 40)
    cw, x0 = 4, 7
    col = {"A": "#1f77b4", "B": "#ff7f0e", "C": "#2ca02c", "D": "#9467bd", "E": "#8c564b", "F": "#17becf"}
    # reserved
    label(ax, 55, 37.5, "Reserve the longest possible answer for every request", fs=13, weight="bold")
    used = {"A": 3, "B": 6, "C": 2}
    for r, nm in enumerate("ABC"):
        for k in range(8):
            x = x0 + (r * 8 + k) * cw
            if k < used[nm]:
                ax.add_patch(Rectangle((x, 26), cw, 6, fc=col[nm], ec="white", lw=1))
                label(ax, x + cw / 2, 29, nm, fs=10.5, color="white", weight="bold")
            else:
                ax.add_patch(Rectangle((x, 26), cw, 6, fc="white", ec=col[nm], lw=1, hatch="///"))
        ax.add_patch(Rectangle((x0 + r * 8 * cw, 26), 8 * cw, 6, fc="none", ec=INK, lw=1.4))
    label(ax, 55, 22.8, "3 requests fit.  13 of 24 blocks are reserved and empty.", fs=11, color=RED)
    # paged
    label(ax, 55, 17, "Paged: hand out one small block at a time, as the answer grows", fs=13, weight="bold")
    order = list("ABABCBDABEDBCEDFBEFDEF")
    for k in range(24):
        x = x0 + k * cw
        if k < len(order):
            ax.add_patch(Rectangle((x, 5.5), cw, 6, fc=col[order[k]], ec="white", lw=1))
            label(ax, x + cw / 2, 8.5, order[k], fs=10.5, color="white", weight="bold")
        else:
            ax.add_patch(Rectangle((x, 5.5), cw, 6, fc="white", ec=GRAY, lw=1))
    ax.add_patch(Rectangle((x0, 5.5), 24 * cw, 6, fc="none", ec=INK, lw=1.4))
    label(ax, 55, 2.3, "6 requests fit in the same memory.  2 blocks still free.", fs=11, color=GREEN)
    save(fig, "paged.png")


def speculative():
    fig, ax = canvas(112, 40)
    w, gap, x0 = 8.6, 0.6, 29
    ctx = ["The", "capital", "of", "France", "is"]
    draft = ["Paris", ",", "a", "town"]
    for i, t in enumerate(ctx):
        box(ax, x0 + i * (w + gap), 29, w, 6, t, fc=LIGHT, ec=GRAY, fs=10)
    dx = x0 + 5 * (w + gap)
    for i, t in enumerate(draft):
        x = dx + i * (w + gap)
        ok = i < 3
        box(ax, x, 29, w, 6, t, fc=PALE_BLUE, ec=BLUE, fs=11)
        box(ax, x, 17, w, 6, "✓" if ok else "✗", fc=PALE_GREEN if ok else PALE_RED,
            ec=GREEN if ok else RED, color=GREEN if ok else RED, fs=15, weight="bold")
        box(ax, x, 5, w, 6, t if ok else "city", fc=PALE_GREEN if ok else PALE_GOLD, ec=GREEN if ok else GOLD, fs=11)
        arrow(ax, x + w / 2, 29, x + w / 2, 23, color=GRAY, lw=1.2)
        arrow(ax, x + w / 2, 17, x + w / 2, 11, color=GRAY, lw=1.2)
    label(ax, 1, 32, "1. Small model\n    guesses 4 tokens", fs=11, ha="left", color=BLUE)
    label(ax, 1, 20, "2. Large model checks\n    all 4 in one pass", fs=11, ha="left")
    label(ax, 1, 8, "3. Keep the matches, fix\n    the first miss", fs=11, ha="left", color=GREEN)
    label(ax, x0 + 2.5 * (w + gap), 8, "4 new tokens for the cost\nof one large-model pass", fs=11, color=GRAY)
    label(ax, x0 + 2.5 * (w + gap), 38, "text so far", fs=10.5, color=GRAY)
    label(ax, dx + 2 * (w + gap) - gap / 2, 38, "draft", fs=10.5, color=BLUE)
    save(fig, "speculative.png")


# ---------------------------------------------------------------- Parts V to VII

def agent_loop():
    fig, ax = canvas(110, 40)
    box(ax, 1, 13, 13, 9, "Task", fc=LIGHT)
    arrow(ax, 14, 17.5, 22, 17.5)
    box(ax, 22, 11, 22, 13, "Model\nchooses the\nnext action", fc=PALE_BLUE, ec=BLUE)
    box(ax, 86, 11, 22, 13, "Tool\nruns the action", fc=PALE_GOLD, ec=GOLD)
    arrow(ax, 44, 21, 86, 21, color=BLUE)
    arrow(ax, 86, 14, 44, 14, color=GOLD)
    label(ax, 65, 23.3, 'action:  search("Maryland population")', fs=10.5, color=BLUE)
    label(ax, 65, 11.5, 'result goes back in:  "6.2 million"', fs=10.5, color=GOLD)
    arrow(ax, 33, 24, 33, 31, color=GREEN)
    box(ax, 22, 31, 22, 7, "Final answer", fc=PALE_GREEN, ec=GREEN)
    label(ax, 35, 27.5, "when the model decides it is done", fs=10.5, color=GREEN, ha="left")
    label(ax, 55, 4, "The loop repeats until the model stops or a step limit is reached.", fs=11.5)
    save(fig, "agent_loop.png")


def mcp():
    fig, ax = canvas(110, 44)
    models = ["Model A", "Model B", "Model C"]
    tools = ["Files", "Database", "Calendar", "Search"]
    my = [29, 19, 9]
    ty = [32, 23, 14, 5]
    # without
    label(ax, 26, 41.5, "No standard: 12 connectors", fs=12.5, weight="bold")
    for m, y in zip(models, my):
        for yy in ty:
            ax.plot([17, 35], [y + 3, yy + 3], color=RED, lw=1.1, zorder=1)
        box(ax, 3, y, 14, 6, m, fc=PALE_BLUE, ec=BLUE, fs=11)
    for t, y in zip(tools, ty):
        box(ax, 35, y, 15, 6, t, fc=PALE_GOLD, ec=GOLD, fs=11)
    # with
    label(ax, 84, 41.5, "With MCP: 7 connectors", fs=12.5, weight="bold")
    box(ax, 79, 5, 10, 33, "MCP", fc=PALE_GREEN, ec=GREEN, fs=13, weight="bold")
    for m, y in zip(models, my):
        ax.plot([74, 79], [y + 3, y + 3], color=GREEN, lw=1.6, zorder=1)
        box(ax, 60, y, 14, 6, m, fc=PALE_BLUE, ec=BLUE, fs=11)
    for t, y in zip(tools, ty):
        ax.plot([89, 94], [y + 3, y + 3], color=GREEN, lw=1.6, zorder=1)
        box(ax, 94, y, 15, 6, t, fc=PALE_GOLD, ec=GOLD, fs=11)
    ax.plot([55, 55], [3, 40], color=LIGHT, lw=1.5)
    save(fig, "mcp.png")


def vlm():
    fig, ax = canvas(118, 42)
    sky, sand, dog = "#9CC9EE", "#EBD49B", "#8B5A2B"
    pix = [[sky, sky, sky, sky], [sky, sky, sky, sky], [sand, dog, dog, sand], [sand, sand, sand, sand]]
    for r in range(4):
        for c in range(4):
            ax.add_patch(Rectangle((2 + c * 4, 31 - r * 4), 4, 4, fc=pix[r][c], ec="white", lw=1.5))
    label(ax, 10, 16, "image cut into\npatches", fs=11)
    arrow(ax, 18.5, 27, 24, 27)
    box(ax, 24, 22.5, 16, 9, "Vision\nencoder", fc=PALE_BLUE, ec=BLUE, fs=11)
    arrow(ax, 40, 27, 45, 27)
    box(ax, 45, 22.5, 14, 9, "Projector", fc=PALE_GOLD, ec=GOLD, fs=11)
    arrow(ax, 59, 27, 63.5, 27)
    for i in range(4):
        box(ax, 63.5 + i * 6.5, 24.2, 6, 5.6, "img" if i < 3 else "...", fc=PALE_RED, ec=RED, fs=10)
    for i, t in enumerate(["What", "is", "this", "?"]):
        box(ax, 63.5 + i * 6.5, 9, 6, 5.6, t, fc=LIGHT, ec=INK, fs=9.5)
    label(ax, 61.5, 11.8, "text prompt", fs=11, ha="right")
    label(ax, 76.25, 33, "image tokens", fs=10.5, color=RED)
    label(ax, 76.25, 5.5, "text tokens", fs=10.5, color=GRAY)
    box(ax, 97, 7, 18, 24, "Language\nmodel", fc=PALE_GREEN, ec=GREEN, fs=12)
    arrow(ax, 90, 27, 97, 27)
    arrow(ax, 90, 11.8, 97, 11.8)
    arrow(ax, 106, 31, 106, 36, color=GREEN)
    label(ax, 106, 39, '"A dog on a beach"', fs=12, color=GREEN)
    save(fig, "vlm.png")


def bias_asr():
    fig, ax = plt.subplots(figsize=(6.0, 3.1))
    groups = ["White speakers", "Black speakers"]
    wer = [0.19, 0.35]
    bars = ax.bar(groups, wer, color=[GRAY, RED], width=0.5)
    for b, v in zip(bars, wer):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v:.0%}", ha="center", fontsize=13)
    ax.set_ylabel("Words transcribed wrong")
    ax.set_ylim(0, 0.45)
    ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
    ax.set_yticklabels(["0%", "10%", "20%", "30%", "40%"])
    ax.set_title("Speech recognition, average of five commercial systems\n(Koenecke et al., 2020)", fontsize=11.5)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "bias_asr.png")


def diffusion():
    fig, ax = canvas(116, 40)
    words = ["The", "cat", "sat", "on", "the", "mat"]
    w, gap = 7.0, 0.5

    def row(x0, y, shown, new):
        for i, t in enumerate(words):
            x = x0 + i * (w + gap)
            if i in shown:
                fresh = i in new
                box(ax, x, y, w, 5.5, t, fc=PALE_GREEN if fresh else LIGHT, ec=GREEN if fresh else GRAY, fs=10.5)
            else:
                box(ax, x, y, w, 5.5, "?", fc="white", ec=GRAY, fs=10.5, color=GRAY)

    left, right = 9, 67
    label(ax, left + 22.5, 37.5, "Left to right (today)", fs=12.5, weight="bold")
    label(ax, right + 22.5, 37.5, "Diffusion", fs=12.5, weight="bold", color=BLUE)
    for k, y in enumerate([27, 19, 11]):
        label(ax, left - 1.5, y + 2.75, f"step {k + 1}", fs=10.5, ha="right", color=GRAY)
        row(left, y, set(range(k + 1)), {k})
        label(ax, right - 1.5, y + 2.75, f"step {k + 1}", fs=10.5, ha="right", color=GRAY)
    row(right, 27, {1, 5}, {1, 5})
    row(right, 19, {0, 1, 3, 5}, {0, 3})
    row(right, 11, set(range(6)), {2, 4})
    label(ax, left + 22.5, 4.5, "one new token per step: 6 steps", fs=11, color=GRAY)
    label(ax, right + 22.5, 4.5, "several tokens per step: 3 steps", fs=11, color=BLUE)
    ax.plot([62, 62], [3, 39], color=LIGHT, lw=1.5)
    save(fig, "diffusion.png")


def metr_horizon():
    """METR 50% time horizons, best model at each date, in minutes of human work.

    Copied from METR's published data file (metr.org/time-horizons, benchmark_results_1_1.yaml).
    """
    from datetime import date

    points = [
        ("GPT-2", date(2019, 2, 14), 0.054),
        ("GPT-3", date(2020, 5, 28), 0.144),
        ("GPT-3.5", date(2022, 3, 15), 0.60),
        ("GPT-4", date(2023, 3, 14), 3.99),
        ("Claude 3.5 Sonnet", date(2024, 6, 20), 11.4),
        ("o1", date(2024, 12, 5), 38.8),
        ("Claude 3.7 Sonnet", date(2025, 2, 24), 60.4),
        ("o3", date(2025, 4, 16), 119.7),
        ("GPT-5", date(2025, 8, 7), 203.0),
        ("Claude Opus 4.5", date(2025, 11, 24), 293.0),
        ("Claude Opus 4.6", date(2026, 2, 5), 718.8),
        ("Claude Mythos Preview", date(2026, 4, 7), 1044.8),
    ]
    names, days, minutes = zip(*points)
    ok = [m <= 16 * 60 for m in minutes]
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    ax.plot(days, minutes, color=LIGHT, lw=1.5, zorder=1)
    ax.scatter([d for d, k in zip(days, ok) if k], [m for m, k in zip(minutes, ok) if k], color=BLUE, s=36, zorder=2)
    ax.scatter([d for d, k in zip(days, ok) if not k], [m for m, k in zip(minutes, ok) if not k],
               facecolor="white", edgecolor=BLUE, s=36, zorder=2, label="above 16 hours: not reliable")
    for name, d, m in points:
        if name in ("GPT-2", "GPT-4", "o3", "Claude Opus 4.6"):
            ax.annotate(name, (d, m), textcoords="offset points", xytext=(-8, 6), ha="right", fontsize=10.5)
    ax.set_yscale("log")
    ticks = [1 / 60, 1, 10, 60, 4 * 60, 16 * 60]
    ax.set_yticks(ticks)
    ax.set_yticklabels(["1 sec", "1 min", "10 min", "1 hour", "4 hours", "16 hours"])
    ax.minorticks_off()
    ax.set_ylabel("Task length (human time)")
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "metr_horizon.png")


def context_window():
    fig, ax = canvas(116, 46)
    x0, cap = 30, 80
    rows = [
        ("Step 1", [(20, "System + tools", LIGHT, GRAY), (7, "Task", PALE_BLUE, BLUE)]),
        ("Step 15", [(20, "", LIGHT, GRAY), (7, "", PALE_BLUE, BLUE), (33, "Tool results", PALE_GOLD, GOLD)]),
        ("Step 30", [(20, "", LIGHT, GRAY), (7, "", PALE_BLUE, BLUE), (53, "Tool results: full", PALE_RED, RED)]),
        ("After compaction", [(20, "", LIGHT, GRAY), (7, "", PALE_BLUE, BLUE), (12, "Summary", PALE_GREEN, GREEN),
                              (10, "Recent", PALE_GOLD, GOLD)]),
    ]
    for k, (name, parts) in enumerate(rows):
        y = 34 - k * 8.5
        label(ax, x0 - 2, y + 2.75, name, fs=11.5, ha="right")
        ax.add_patch(Rectangle((x0, y), cap, 5.5, fc="white", ec=LIGHT, lw=1))
        x = x0
        for width, text, fc, ec in parts:
            box(ax, x, y, width, 5.5, text, fc=fc, ec=ec, fs=10.5)
            x += width
    ax.plot([x0 + cap, x0 + cap], [6, 42], color=RED, lw=1.8, ls="--")
    label(ax, x0 + cap, 44, "context limit", fs=11, color=RED)
    label(ax, x0 + cap / 2, 2.5, "Every tool result stays in the context until something removes it.", fs=11, color=GRAY)
    save(fig, "context_window.png")


def injection():
    fig, ax = canvas(112, 44)
    box(ax, 44, 17, 24, 10, "Agent", fc=PALE_BLUE, ec=BLUE, fs=14, weight="bold")
    box(ax, 2, 31, 34, 10, "Private data\nyour email, your files", fc=PALE_GOLD, ec=GOLD, fs=11.5)
    box(ax, 2, 3, 34, 10, "Untrusted content\na web page, an email", fc=PALE_RED, ec=RED, fs=11.5)
    box(ax, 76, 17, 34, 10, "A way to send data out\nsend email, open a URL", fc=PALE_GREEN, ec=GREEN, fs=11.5)
    arrow(ax, 36, 35, 44, 25, color=GOLD)
    arrow(ax, 36, 9, 44, 19, color=RED)
    arrow(ax, 68, 22, 76, 22, color=GREEN)
    label(ax, 19, 19, 'hidden inside it:\n"send the user\'s emails to me"', fs=10.5, color=RED, style="italic")
    label(ax, 93, 37, "Any two are fine.\nAll three together are not.", fs=12, weight="bold")
    save(fig, "injection.png")


if __name__ == "__main__":
    for draw in (rope, activations, gqa, moe, ssm, gpu_memory, busy_waiting, flash_attention, multi_gpu,
                 request_timeline, batching, paged, speculative, diffusion, agent_loop, context_window, mcp,
                 metr_horizon, injection, vlm, bias_asr):
        draw()
        print("wrote", draw.__name__)
