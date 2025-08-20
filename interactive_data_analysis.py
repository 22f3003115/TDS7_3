# 22f3003115@ds.study.iitm.ac.in   <-- Email ID as required

import marimo

__generated_with__ = "0.7.0"
app = marimo.App()


# -------------------------------
# Cell 1: Import data and create raw dataset
# -------------------------------
@app.cell
def raw_data():
    import numpy as np
    import pandas as pd

    # Simulated dataset
    np.random.seed(42)
    df = pd.DataFrame({
        "X": np.linspace(0, 100, 200),
        "Y": np.linspace(0, 100, 200) * 0.5 + np.random.normal(0, 5, 200)
    })
    df
    return df


# -------------------------------
# Cell 2: Interactive filter on X variable
# (depends on raw_data)
# -------------------------------
@app.cell
def filter_widget(mo):
    slider = mo.ui.slider(0, 100, 10, label="Minimum X value")
    slider
    return slider


@app.cell
def filtered_data(df, filter_widget):
    # Filtering based on slider input
    filtered = df[df["X"] >= filter_widget.value]
    filtered
    return filtered


# -------------------------------
# Cell 3: Visualization
# (depends on filtered_data)
# -------------------------------
@app.cell
def plot(filtered_data, mo):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.scatter(filtered_data["X"], filtered_data["Y"], alpha=0.7)
    ax.set_title("Scatter plot of X vs Y (filtered)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    mo.pyplot(fig)


# -------------------------------
# Cell 4: Dynamic markdown explanation
# (depends on filter_widget)
# -------------------------------
@app.cell
def explanation(mo, filter_widget, filtered_data):
    mo.md(f"""
    ### Analysis Summary
    - Minimum X chosen: **{filter_widget.value}**
    - Remaining data points: **{len(filtered_data)}**

    This demonstrates how filtering affects the dataset and the observed relationship
    between **X** and **Y**.
    """)


if __name__ == "__main__":
    app.run()
