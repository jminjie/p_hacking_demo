import getopt
import numpy as np
import sys
import util

def parse_input(argv):
    num_points = 5000
    num_features = 100
    try:
        opts, args = getopt.getopt(argv, "p:f:", ['points=', 'features='])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
    for o, a in opts:
        if o in ['-p', '--points']:
            num_points = int(a)
        elif o in ['-f', '--features']:
            num_features = int(a)
            if num_features > 256:
                print 'At most 256 features are allowed'
                num_features = 256
        else:
            print 'Unhandled option ' + o

    print 'num_points={0}\nnum_features={1}'.format(num_points, num_features)
    return num_points, num_features
    

def main(argv):
    # Parse command line arguments
    num_points, num_features = parse_input(argv)
    treatment_data = util.generate_random_data(num_points, num_features)
    control_data = util.generate_random_data(num_points, num_features)
    significant_features = util.find_significant_features(control_data, \
                                                     treatment_data, 0.01)
    print 'Significant features:', significant_features
    if len(significant_features) is 0:
        return

    max_diff = 0
    max_diff_feature = -1
    max_diff_population_mean = 0
    max_diff_treatment_mean = 0
    for feature in significant_features:
        feature_in_control = util.get_single_feature(feature, control_data)
        population_mean = np.mean(feature_in_control)
        feature_in_treatment = util.get_single_feature(feature, treatment_data)
        treatment_mean = np.mean(feature_in_treatment)
        print 'Feature {0}\n\tmean population: {1}\n\tmean treated: {2}'.format( \
                                    feature, population_mean, treatment_mean)
        diff = abs(population_mean - treatment_mean)
        if diff > max_diff:
            max_diff = diff
            max_diff_feature = feature
            max_diff_population_mean = population_mean
            max_diff_treatment_mean = treatment_mean

    print 'Maximum effect found in feature {0}:\nmean population: {1}\nmean treated: {2}' \
            .format(max_diff_feature, max_diff_population_mean, max_diff_treatment_mean)   

if __name__ == '__main__':
    main(sys.argv[1:])
