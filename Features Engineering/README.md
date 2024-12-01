This folder contains the following files:
- DictAreasTrain.pickle: A dictionary whose keys are samples and its entries are dataframes with areas under curves grouped by temperature bin

- DictAreasVal.pickle: Same as above, but for the validation samples

- preprocess.py: a function that preprocesses dataframes, created during EDA

- scatter_plots.ipynb. This file contains scatter plots of the various features based on the files created in selecting_prominent_ratios.ipynb.

- selecting_prominent_ratios.ipynb. This file augments the train_labels and val_labels csv files with additional columns corresponding to features, as follows. It first chooses the 5 mass-to-charge ratios that are the most prominent in each sample, and for each of them it records peak renormalized abundance, temperature at which this happens, and sum of mean and std dev of the renormalized abundance.

- temp_bin_PCA_output.csv. This is a csv file where for each sample one does PCA on the dataframe stored for it in DictAreasTrain.pickle, then arranges the resulting matrix into a long row.

- temp_bin_val_PCA_output.csv: Same as above, but for validation files

- temp_bins_array_PCA.ipynb: In this file we create a dataframe where each row corresponds to area measurements for each sample, grouped by temperature bin and mass to charge ratio. Then we perform PCA for each temperature bin separately and produce the files train_features_temp_bin_PCA.csv and val_features_temp_bin_PCA.csv.

- temp_bins_curve_area_PCA.ipynb: PCA on the file temp_bins_curve_area.ipynb.

- temp_bins_curve_area.ipynb: In this file we create a dictionary whose keys are sample names and its entries are dataframes. Each dataframe has rows corresponding to temperature intervals and columns corresponding to mass-to-charge ratios. Then each entry is the integral of the renormalized abundance curve for the given ratio, over the temperature interval.

- train_features_temp_bin_PCA: In this file one does pca on the columns corresponding to each temperature bin and keeps 3.

- val_features_temp_bin_PCA: same as in above but for validation samples


