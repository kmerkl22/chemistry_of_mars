# For more details see EDS.ipynb

from sklearn.preprocessing import minmax_scale

def drop_non_int_and_He(df):
    """
    This function takes in a dataframe with a column named m/z and returns a new dataframe where all entries 
    with non-integer value of m/z have been removed, as well as all entries corresponding to m/z equal to 4 or larger than 100

    """
    df2 = df
    df2 = df2[df2['m/z'].transform(round) == df2['m/z']]
    df2 = df2[df2['m/z']<100]
    df2 = df2[df2['m/z'] != 4]
    return df2



def subtract_min(df):    
    """ This function takes in a dataframe with columns named m/z and
        abundance and transforms by subtracting 
        the minimal value of abundance, corresponding 
        to each m/z

        This function does not keep a copy of the original dataframe, it transforms it instead
    """

    df["abundance_minsub"] = df.groupby(["m/z"])["abundance"].transform(
        lambda x: (x - x.min())
    )
    return df



def scale_to_zero_one(df):
    """
    scales the abundances by the formula (x-x_min)/(x_max-x_min)
    It does not create a copy of the original dataframe, it transforms it.
    """
    df['zero_one_rescale'] = minmax_scale(df['abundance_minsub'])
    assert (df['zero_one_rescale'].max()<=1)
    return df


def preprocess(df):
    """
    Combines the procedures above. 
    The first function applied to df above creates and returns a copy of its input, whereas the other two
    modify the input. So at the end, the original dataframe stays unchanged
    """
    return scale_to_zero_one(subtract_min(drop_non_int_and_He(df)))

