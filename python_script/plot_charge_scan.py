import os as os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plot_config import *

# Configuration
filename = "IT_L4R0M0_Gigi_charge_scan_THR_205_FTH_MX"
ch_min = 24
ch_max = 31

# LaTex interpreter
plt.rcParams.update({"text.usetex": True, "font.family": "serif"})

# Folders
input_folder = "python_script\input"
output_folder = "python_script\output"

# PLOT CONFIGURATION
# Label size
matplotlib.rcParams["axes.labelsize"] = 13
# Tick label size
matplotlib.rcParams["xtick.labelsize"] = 13
matplotlib.rcParams["ytick.labelsize"] = 13
# Figure size
matplotlib.rcParams["figure.figsize"] = 6.4 * 1.3, 4.8 * 1.3

data = pd.read_csv(os.path.join(input_folder, filename + ".dat"), comment="#", sep="\t")
threshold = data.iloc[0][0]
n_events = data.iloc[0][2]
conv_factor = 0.841

channels = range(ch_min, ch_max + 1)
dac_range = np.unique(data.iloc[:, 1])

# All channels in the same plot
plt.clf()
ch_count = 0
for ch in channels:
    ch_data = data[data.iloc[:, 4] == ch]
    inj_range = ch_data.iloc[:, 1]
    events = ch_data.iloc[:, 3]
    inj_range = [inj_i * conv_factor for inj_i in inj_range]
    events = [ev_i / n_events * 100 for ev_i in events]
    plt.plot(
        inj_range,
        events,
        label=str(ch),
        linestyle="--" if ch_count >= len(channels) / 2 and len(channels) > 16 else "-",
    )
    ch_count = ch_count + 1

plt.title(
    r"\textbf{Charge scan (THR: " + str(threshold) + ", " + str(n_events) + " events)}"
)
plt.xlabel("Energy [keV]")
plt.ylabel("Probability [\%]")
num_columns = 1
if len(channels) > 16:
    num_columns = 2
plt.legend(
    title=r"\textbf{Channel}",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    ncol=num_columns,
)
plt.grid()


output_folder_spec = os.path.join(output_folder, filename)
if not os.path.exists(output_folder_spec):
    os.mkdir(output_folder_spec)

allch_filename = os.path.join(
    output_folder_spec,
    "charge_scan_ch"
    + str(ch_min)
    + "-"
    + str(ch_max)
    + "_THR"
    + str(threshold)
    + ".pdf",
)
plt.savefig(allch_filename)
print("Saved: " + allch_filename + "\n")

# Save single channels
output_folder_spec_single = os.path.join(output_folder_spec, "single_channels")
if not os.path.exists(output_folder_spec_single):
    os.mkdir(output_folder_spec_single)

for ch in channels:
    plt.clf()
    ch_data = data[data.iloc[:, 4] == ch]
    inj_range = ch_data.iloc[:, 1]
    events = ch_data.iloc[:, 3]
    inj_range = [inj_i * conv_factor for inj_i in inj_range]
    events = [ev_i / n_events * 100 for ev_i in events]
    plt.plot(inj_range, events)
    plt.title(
        r"\textbf{Charge scan ch. "
        + str(ch)
        + " (THR: "
        + str(threshold)
        + ", "
        + str(n_events)
        + " events)}"
    )
    plt.xlabel("Energy [keV]")
    plt.ylabel("Probability [\%]")
    plt.grid()
    plt.savefig(
        os.path.join(
            output_folder_spec_single,
            "charge_scan_ch" + str(ch) + "_THR_" + str(threshold) + ".pdf",
        )
    )
    print("Saved ch. " + str(ch))