import numpy as np
import statistics as st

def mean(lst):
    return (sum(lst)/len(lst))

def median(lst):
    lst = np.sort(lst)
    n = len(lst)
    floor = int(np.floor((n + 1) / 2))
    ceil = int(np.ceil((n + 1) / 2))
    median = 0.5 * (lst[floor - 1] + lst[ceil - 1])
    return median

def mode(lst):
    lst = np.sort(lst)
    return (st.mode(lst))

def geom_mean(lst):
    lst = np.sort(lst)
    n = len(lst)
    product = lst[0]
    for i in lst[1:]:
        product *= i
    geom_mean = product ** (1 / n)
    return (geom_mean)

def harmonic_mean(lst):
    lst = np.sort(lst)
    n = len(lst)
    numerator = (1 / lst[0])
    for i in lst[1:]:
        numerator += (1 / i)
    harmonic_mean = 1 / (numerator / n)
    return (harmonic_mean)

def arithmetic_geom_mean(lst):
    lst = np.sort(lst)
    ahg_arithmetic_mean = mean(lst)
    ahg_geom_mean = geom_mean(lst)
    arithmetic_geom_mean = (ahg_arithmetic_mean + ahg_geom_mean) / 2
    return (arithmetic_geom_mean)

def arithmetic_harmonic_geom_mean(lst):
    lst = np.sort(lst)
    ahg_arithmetic_mean = mean(lst)
    ahg_geom_mean = geom_mean(lst)
    ahg_harmonic_mean = harmonic_mean(lst)
    arithmetic_harmonic_geom_mean = (ahg_arithmetic_mean + ahg_geom_mean + ahg_harmonic_mean) / 3
    return (arithmetic_harmonic_geom_mean)

def variance(lst):
    variance = st.variance(lst)
    return (variance)

def pvariance(lst):
    pvariance = st.pvariance(lst)
    return (pvariance)

def std(lst):
    std = st.stdev(lst)
    return (std)

def pstd(lst):
    pstd = st.pstdev(lst)
    return (pstd)

def mad_mean(lst):
    lst = np.sort(lst)
    n = len(lst)
    mu = mean(lst)
    numerator = np.abs(lst[0] - mu)
    for i in lst[1:]:
        numerator += np.abs(i - mu)
    mad_mean = numerator / n
    return (mad_mean)

def mad_median(lst):
    lst = np.sort(lst)
    n = len(lst)
    mu = median(lst)
    numerator = np.abs(lst[0] - mu)
    for i in lst[1:]:
        numerator += np.abs(i - mu)
    mad_median = numerator / n
    return (mad_median)

def mad_mode(lst):
    lst = np.sort(lst)
    n = len(lst)
    mu = mode(lst)
    numerator = np.abs(lst[0] - mu)
    for i in lst[1:]:
        numerator += np.abs(i - mu)
    mad_mode = numerator / n
    return (mad_mode)

def mpad(lst, p, mu):
    lst = np.sort(lst)
    n = len(lst)
    numerator = np.abs(lst[0] - mu) ** p
    for i in lst[1:]:
        numerator += np.abs(i - mu) ** p
    mpad = numerator / n
    return (mpad)

def iqr(lst):
    lst = np.sort(lst)
    n = len(lst)
    lq_floor = int(np.floor((n + 1) / 4)) - 1
    lq_ceil = int(np.ceil((n + 1) / 4)) - 1
    lq = 1/2 * (lst[lq_floor] + lst[lq_ceil])
    uq_floor = int(np.floor((3 * (n + 1)) / 4)) - 1
    uq_ceil = int(np.ceil((3 * (n + 1)) / 4)) - 1
    uq = 1/2 * (lst[uq_floor] + lst[uq_ceil])
    return (lq, uq)

def quartile_based_skewness(lst):
    lq, uq = iqr(lst)
    mq = median(lst)
    quartile_based_skewness = (uq + lq - (2 * mq)) / (uq - lq)
    return (quartile_based_skewness)

def pearson_first_skewness(lst):
    p_mean = mean(lst)
    p_mode = mode(lst)
    p_std = std(lst)
    pearson_first_skewness = (p_mean - p_mode) / p_std
    return (pearson_first_skewness)

def pearson_second_skewness(lst):
    p_mean = mean(lst)
    p_median = median(lst)
    p_std = std(lst)
    pearson_second_skewness = (3 * (p_mean - p_median)) / p_std
    return (pearson_second_skewness)

def groeneveld_meedens_coef(lst):
    p_mean = mean(lst)
    p_median = median(lst)
    p_mad_median = mad_median(lst)
    groeneveld_meedens_coef = (p_mean - p_median) / p_mad_median
    return (groeneveld_meedens_coef)

def pearson_moment_coef(lst):
    lst = np.sort(lst)
    n = len(lst)
    mu = mean(lst)
    p_std = std(lst)
    numerator = (lst[0] - mu) ** 3
    for i in lst[1:]:
        numerator += (i - mu) ** 3
    denominator = (p_std ** 3) * n
    pearson_moment_coef = numerator / denominator
    return (pearson_moment_coef)

def kurtosis(lst):
    lst = np.sort(lst)
    n = len(lst)
    mu = mean(lst)
    p_std = std(lst)
    numerator = (lst[0] - mu) ** 4
    for i in lst[1:]:
        numerator += (i - mu) ** 4
    denominator = (p_std ** 4) * n
    kurtosis = numerator / denominator
    return (kurtosis)

def p_degree_standard_coef(lst, p, mu):
    lst = np.sort(lst)
    n = len(lst)
    p_std = std(lst)
    numerator = (lst[0] - mu) ** p
    for i in lst[1:]:
        numerator += (i - mu) ** p
    denominator = (p_std ** p) * n
    p_degree_standard_coef = numerator / denominator
    return (p_degree_standard_coef)