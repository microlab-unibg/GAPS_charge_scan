import os as os
import numpy as np
import pandas as pd
from pathlib import Path as path
import glob

from plot_config import *
from erf_function import *
from charge_scan_noinj import charge_scan_noinj
from charge_scan import charge_scan
from threshold_scan import threshold_scan
from compute_par_inj import get_parasitic_injection

root_filepath = r"C:\Users\ghisl\Downloads\charge_scan_layer_3\*"
leaf_filepath = r"data\ChargeScan_fast.dat"
leaf_filepath_out = r"output"

all_folders = glob.glob(root_filepath)

print(all_folders)

for folder in all_folders:
    filename_chargescan = os.path.join(folder, leaf_filepath)
    output_folder_filepath = os.path.join(folder, leaf_filepath_out)
    print(filename_chargescan)
    print(output_folder_filepath)

    # Read data from file
    data = pd.read_csv(
        filename_chargescan,
        comment="#",
        sep="\t",
        header=None,
    )

    ch_min = 0
    ch_max = 31
    deactivate_thr = 30
    deactivate_enc = 10
    excl_channels = []

    # Configuration
    conv_factor = 0.841
    channels = range(ch_min, ch_max + 1)
    channels = np.setdiff1d(channels, excl_channels)

    # Determine if charge scan or threshold scan
    n_events = data.iloc[0][2]
    threshold_col = data.iloc[:, 0]
    threshold_col = threshold_col.to_numpy()
    thr_unique = np.unique(threshold_col)
    charge_scan_flag = True

    # Charge scan without removal of parasitic injection
    # Always done
    (xmin, xmax) = charge_scan(
        data,
        channels,
        conv_factor,
        output_folder_filepath,
        deactivate_thr,
        deactivate_enc,
    )
