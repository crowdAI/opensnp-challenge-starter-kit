# opensnp-challenge-starter-kit
![CrowdAI-Logo](https://camo.githubusercontent.com/5b7dd96dce88e193221d0d2e5b07118fc44dc7d4/68747470733a2f2f7777772e63726f776461692e6f72672f6173736574732f63726f776461695f6c6f676f5f736d696c652d653835653532653032663839343933653335356331343539643034303964653835396330613233396637623137376664373337333164636139636266363166622e737667)

Starter kit for getting started in the [CrowdAI OpenSNP Challenge](https://www.crowdai.org/challenges/opensnp-height-prediction).

# Installation
```
git clone https://github.com/spMohanty/opensnp-challenge-starter-kit
cd opensnp-challenge-starter-kit
pip install -r requirements.txt
pip install -U crowdai
```

# Data download and preparation
Download all the files from the [CrowdAI Dataset page](https://www.crowdai.org/challenges/opensnp-height-prediction/dataset_files),
and put them in the `data/` folder. Then :
```
cd data/
gunzip *.gz
```

**NOTE**: You might not need to download all the files, or even use all the files to come up with your predictions. It is recommended to use the `subset_cm_train.npy` and `train_heights.npy` to train your model, and use `subset_cm_test.npy` to make the predictions.

# Basic Usage

```
import crowdai
challenge = crowdai.Challenge("OpenSNPChallenge2017", "YOUR_CROWDAI_API_KEY_HERE")

data = ... #a list of 137 predicted heights for all the 137 corresponding data points in the test set
challenge.submit(data)
challenge.disconnect()
```

# Submit Random Predictions
```
python random_predict.py --api_key=<<YOUR_CROWDAI_API_KEY_HERE>>
```

# Predictions by Linear Regression
```
python linear_regression_predict.py --api_key=<<YOUR_CROWDAI_API_KEY_HERE>>
```

# Predictions by Support Vector Regression
```
python svr_predict.py --api_key=<<YOUR_CROWDAI_API_KEY_HERE>>
```

# Author
S.P. Mohanty <sharada.mohanty@epfl.ch>
