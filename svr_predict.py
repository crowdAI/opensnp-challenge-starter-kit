import crowdai
import argparse
from sklearn.svm import SVR
import numpy as np

parser = argparse.ArgumentParser(description='Submit the result to crowdAI')
parser.add_argument('--api_key', dest='api_key', action='store', required=True)
args = parser.parse_args()

# Create the challenge object by authentication with crowdAI with your API_KEY
challenge = crowdai.Challenge("OpenSNPChallenge2017", args.api_key)

#Load training data
x_train = np.load("data/subset_cm_train.npy")
y_train = np.load("data/train_heights.npy")

x_test = np.load("data/subset_cm_test.npy")

#Replace nan values in the training and testing set with an arbitrary number
inds = np.where(np.isnan(x_train))
x_train[inds] = -100
inds = np.where(np.isnan(x_test))
x_test[inds] = -100


# Instantiate a linear model
clf = SVR(C=1.0, epsilon=0.2)
clf.fit(x_train, y_train)

# Predict the heights for the test set
heights = clf.predict(x_test)

#Convert heights from np.array to a list (to ensure it is JSON serializable)
heights = heights.tolist()

challenge.submit(heights)
challenge.disconnect()
