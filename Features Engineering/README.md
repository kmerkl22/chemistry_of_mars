This folder contains the following files:
1. selecting_prominent_ratios.ipynb. This file augments the train_labels and val_labels csv files with additional columns corresponding to features, as follows. It first chooses the 5 mass-to-charge ratios that are the most prominent in each sample, and for each of them it records peak renormalized abundance, temperature at which this happens, and sum of mean and std dev of the renormalized abundance.
2. scatter_plots.ipynb. This file contains scatter plots of the various features based on the files created in SelectingProminentRatios.ipynb.
3. temp_bin_cuve_area.ipynb: In this file we create a dictionary whose keys are sample names and its entries are dataframes. Each dataframe has rows corresponding to temperature intervals and columns corresponding to mass-to-charge ratios. Then each entry is the integral of the renormalized abundance curve for the given ratio, over the temperature interval.
4. temp_bins_array_PCA.ipynb: In this file we perform Principal Component Analysis to the dataframes constructed in TempBinsCurveArea.ipynb
5.
6.
7. temp_bins_array_PCA.ipynb. This notebook performs PCA
8. temp_bin_PCA_output.csv. This is a csv file where for each sample one does PCA the dataframe corresponding to it as in 3. above, then arranges the resulting matrix into a long row.
9. As in 8. but for the validation files

