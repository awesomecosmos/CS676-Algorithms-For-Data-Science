import numpy as np
import pandas as pd

def min_value_location(df):
    row_idx_of_min_values_in_df = df.idxmin(axis=0,numeric_only=True).values.tolist()
    col_idx_of_min_values_in_df = df.idxmin(axis=1,numeric_only=True).values.tolist()
    lst_of_min_values_in_df = df.min(numeric_only=True).values.tolist()
    min_value = min(lst_of_min_values_in_df)
    idx_of_min_value = lst_of_min_values_in_df.index(min_value)
    idx_of_min_row_in_df = row_idx_of_min_values_in_df[idx_of_min_value]
    idx_of_min_col_in_df = col_idx_of_min_values_in_df[idx_of_min_value]
    new_cluster_location = [idx_of_min_row_in_df,int(idx_of_min_col_in_df)]
    return new_cluster_location, min_value

def l1(given_point,x,y):
    # Function to determine Manhattan distance, L1.
    d_l1 = []
    d = len(x) # assumes len(x) = len(y)
    for i in range(d):
        d_sum = (given_point[0] - x[i]) + (given_point[1] - y[i])
        d_l1.append(d_sum)
    return d_l1

def l2(given_point,x,y):
    # Function to determine Euclidean distance, L2.
    d_l2 = []
    d = len(x) # assumes len(x) = len(y)
    for i in range(d):
        d_sum = np.sqrt(((given_point[0] - x[i]) ** 2) + ((given_point[1] - y[i]) ** 2))
        d_l2.append(d_sum)
    return d_l2

def l3(given_point, x, y, p):
    # Function to determine Minkowski distance, L3.
    d_l3 = []
    d = len(x) # assumes len(x) = len(y)
    for i in range(d):
        d_sum = (((given_point[0] - x[i]) ** p) + ((given_point[1] - y[i]) ** p)) ** (1 / p)
        d_l3.append(d_sum)
    return d_l3

# step 1: initialize df
def initialize_cluster(df, distance_measure='l2'):
    df2 = []
    for i in range(len(df)):
        given_point = df.iloc[i]

        if distance_measure == 'l2':
            df2.append(l2(given_point,df['x'],df['y']))
        else:
            # dummy clause for now
            df2.append(l2(given_point,df['x'],df['y']))

    df3 = pd.DataFrame(df2)
    # df3 = df3.drop(0, axis=1)
    blank_value = pd.NA
    df3[0] = blank_value
    # for i in range(1,len(df3)):
    for i in range(len(df3)):
        df3.loc[i:,i] = blank_value
    df3.drop(4,axis=0,inplace=True) # generatlize this [-1]

    return df3

def complete_linkage(df1):
    return df1.max()

def old_cluster(df1, new_cluster):
    # df2 = df1.iloc[[new_cluster[0],new_cluster[1]],:]
    df2 = df1.loc[[new_cluster[0],new_cluster[1]],:]
    
    # df2.drop(new_cluster[1],axis=1,inplace=True)
    df2.drop(new_cluster[0],axis=1,inplace=True)

    df1.drop([new_cluster[0]+1,new_cluster[1]+1],axis=1,inplace=True)
    df1.drop(new_cluster,axis=0,inplace=True)
    return df1, df2

def clustering_iteration(df1, linkage_type='complete'):
    new_cluster, min_value = min_value_location(df1)
    df1, df2 = old_cluster(df1, new_cluster)

    df1[df1.columns[-1]+1] = pd.Series()
    df1 = df1.concat(pd.Series(name=df1.index[-1]+1), ignore_index=False)

    if linkage_type == 'complete':
        df1[df1.columns[-1]] = complete_linkage(df2)
    else:
        # dummy clause for now
        df1[df1.columns[-1]] = complete_linkage(df2)

    return df1