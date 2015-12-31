import getopt
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import sys

def get_single_feature(feature, data):
    num_features = len(data[0])
    if feature > num_features:
        print 'Invalid input; feature {0} is out of bounds'.format(feature)
        return
    single_feature_data = []
    for point in data:
        if len(point) is not num_features:
            print 'Invalid input; control point {0} has {1} features \
                   instead of {2}'.format(point, len(point), num_features)
            return
        single_feature_data.append(point[feature])
    return single_feature_data 
    

# Generates random data points from N(0, 1)
# e.g.
# [[0.6, ..., 0.1],
# [0.1, ..., -0.2],
# ...,
# [0.0, ..., -0.3]]
def generate_random_data(num_points=100, num_features=30, avg=69.1, std=2.7):
    data_points = []
    for i in range(0, num_points):
        data_point = []
        for feature in range(0, num_features):
            data_point.append(np.random.normal(avg, std))
        data_points.append(data_point)
    return data_points

# Given a list of N data points with the same number of features
# returns the indexes of the features found in Treatment but not Placebo
# with p < 0.05
def find_significant_features(control_data, treatment_data, pval=0.05):
    num_points = len(treatment_data)
    num_features = len(treatment_data[0])
    significant_features = []
    threshold = st.norm.ppf(1 - pval)
    if num_points is 0 or num_features is 0:
        print 'Invalid input; {0} points with {1} \
               features'.format(num_points, num_features)
        return
    for current_feature in range(0, num_features):
        # Get estimate of population mean
        current_feature_control = get_single_feature(current_feature,
                                                     control_data)
        population_mean = np.mean(current_feature_control)
        # Get t statistic of treatment data
        current_feature_treatment = get_single_feature(current_feature,
                                                       treatment_data)
        treatment_mean = np.mean(current_feature_treatment)
        stdev = np.std(current_feature_treatment)
        t_statistic = (treatment_mean-population_mean) / (stdev/ \
                                                          math.sqrt(num_points))
        # Check if treatment data is significant on this feature
        if t_statistic > threshold:
            significant_features.append(current_feature)
    return significant_features
