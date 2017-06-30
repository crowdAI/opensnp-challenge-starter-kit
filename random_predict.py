#!/usr/bin/env python

import crowdai

import random
import argparse

parser = argparse.ArgumentParser(description='Submit the result to crowdAI')
parser.add_argument('--api_key', dest='api_key', action='store', required=True)
args = parser.parse_args()

# Create the challenge object by authentication with crowdAI with your API_KEY
challenge = crowdai.Challenge("OpenSNPChallenge2017", args.api_key)

# Create a list of 137 randomly predicted heights
data = [random.randint(150, 200) for x in range(137)]

# Submit to crowdAI
challenge.submit(data)
challenge.disconnect()
