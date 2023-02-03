# GAPS charge scan analysis tool

## Python CLI (Command Line Interface)

This implementation allows to compute **charge scan** or **threshold scan** data acquired via the manual test tab of the GAPS_ModuleTester.py script or via the beckend DAQ.

Charge scan data file **must** be compliant to the following configuration:

```
# Event data block #1
# Threshold DAC Events  Triggered   CH#
205 0   1000    0   0
[...]
205 0   1000    0   31
```

### Download

Download the [latest release](https://github.com/lucaghislo/GAPS_charge_scan/releases/) suitable for you operating system (Windows or Linux).

### Usage

Once launched, the script requires to input the **complete filepath** of the necessary files required to compute the charge scan (or threshold scan). The filepath can be supplied either sorrounded by single ('') or double ("") quotation marks, but can also be written without.

#### Charge scan (or threshold scan) filepath

The first file required is the one produced by either the manual test tab of the GAPS_ModuleTester.py Python script or the main GAPS beckend DAQ. In case of threshold scan, the currently only supported file configuration is the one produced by the manual test of the  GAPS_ModuleTester.py script.

```
*** GAPS CHARGE SCAN TOOL v1.0 ***

    Charge or threshold scan filepath: C:\path\charge_threshold_scan_dummy.txt
```

#### Channel range

Next, the user is required to input the first and last channel for which the script should compute the charge scan. The minimum accepted value is **0** and the maximum is **31**.

```
                        First channel: 0
                         Last channel: 31                  
```

#### Excluded channels

Next, a list of excluded channels can be supplied. This can be done by listing the channels to be excluded separated by commas (with or without spacing). In case no channel needs to be removed, leave it blank.

```
 Excluded channels (comma separated): 7, 8, 9
```

In case all specified channels need to be analysed, leave the space blank and press enter.

```
 Excluded channels (comma separated):
```

#### Output folder

The user is required to input the path of the folder where the results will be stored.

```
               Output folder filepath: C:\path\output_folder  
```

#### Parasitic injection compensation

Next, the user can decide to compensate the parasitic injection (**y**) or not (**n**). In case the user decides not to not compensate it, computation starts and the results are stored in the specified output path.

```
Compensate parasitic injection? (y/n): n

CHARGE SCAN

Working on it, be patient...
```

In case parasitic injection has to be compensated, the user is required to specify the **pedestal** and **transfer function** filepaths for the module under test. These two files can be found in the data/ folder of the automated test performed on the module.

```
Compensate parasitic injection? (y/n): y
```

The two required files are **Pedestals.dat** and **TransferFunction.dat** obtained after computing the automated test with the specific MATLAB or Python script.

```
         Pedestal from automated test: C:\path\Pedestals.dat
Transfer function from automated test: C:\path\TransferFunction.dat
```

Next, the peaking time at which the charge scan has been performed has to be specified. The only acceptable values range from **0** to **7**. After that, charge scan is computed and the results are stored in the specified output path.

```
                Peaking time (0 to 7): 5

CHARGE SCAN

Working on it, be patient...
```

### Results

Results are stored in the specified output path. In case the user decided not to compensate the parasitic injection, the output folder is organised as follows:

```
output_folder/
├── ENC_THR/
│   ├── ch#-#_ENC.pdf
│   ├── ch#-#_THR_ENC.dat
│   ├── ch#-#_THR_hist.pdf
│   └── ch#-#_THR_plot.pdf
├── single_channels/
│   ├── data/
│   │   ├── ch_#_THR_###.dat
│   │   ├── [...]
│   │   └── ch_#_THR_###.dat
│   └── plots/
│       ├── charge_scan_ch#_THR_###.pdf
│       ├── [...]
│       └── charge_scan_ch#_THR_###.pdf
└── charge_scan_ch#-#.pdf
```

In case parasitic injection has been compensated, the script adds the compensated version of every file listed above, identifiable by the "_inj" notation added to every filename.

#### Output folder content

Results are organised as follows

- `charge_scan_ch#-#.pdf` and `charge_scan_ch#-#_inj.pdf`: charge scan overview with and without parasitic injection compensation.

![charge_scan_ch0-31_1](https://user-images.githubusercontent.com/36998696/216655868-975075dc-7042-490b-b2ba-c0783e3aaa2d.png)

- `single_channels/data/ch_#_THR_###.dat` and `single_channels/data/ch_#_THR_###_inj.dat`: raw charge scan data with and without parasitic injection compensation for channel #. First column is the energy [keV] and the second column is the trigger probability [%].

```
   0.000000 0.000000
   0.841000 0.000000
   [...]
   251.459000   100.000000
   252.300000   100.000000
```

- `single_channels/plots/charge_scan_ch#_THR_###.pdf` and `single_channels/plots/charge_scan_ch#_THR_###_inj.pdf`: raw charge scan data with and without parasitic injection compensation for channel #.

![charge_scan_ch0_THR_205_1](https://user-images.githubusercontent.com/36998696/216658156-3af2fe82-0a2f-48aa-a78c-fee9abf448a8.png)

- `ENC_THR/ch#-#_ENC.pdf` and `ENC_THR/ch#-#_ENC_inj.pdf`: estimated ENC plot for all channels in specified range, with and without parasitic injection compensation.

(image here)

- `ENC_THR/ch#-#_ENC.dat` and `ENC_THR/ch#-#_ENC_inj.dat`: estimated threshold and ENC values for all channels in specified range, with and without parasitic injection compensation. The first column is the channel, second column is the threshold [keV] and the third column is the ENC [keV].

```
0   69.736702     5.965096
[...]
31  112.185906    4.861941
```

- `ENC_THR/ch#-#_THR_hist.pdf` and `ENC_THR/ch#-#_THR_hist_inj.pdf`: estimated threshold histogram for all channels in specified range, with and without parasitic injection compensation.

(image here)

- `ENC_THR/ch#-#_THR_plot.pdf` and `ENC_THR/ch#-#_THR_hist_plot.pdf`: estimated threshold histogram for all channels in specified range, with and without parasitic injection compensation.

(image here)
