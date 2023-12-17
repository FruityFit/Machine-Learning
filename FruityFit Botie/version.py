import json
import numpy as np
import tensorflow as tf
import nltk
import requests
import urllib.parse
import sys

# Print Python version
print("Python version:", sys.version)
# Print NumPy versio1n
print("NumPy version:", np.__version__)
# Print TensorFlow version
print("TensorFlow version:", tf.__version__)
# Print NLTK version
print("NLTK version:", nltk.__version__)



expected_numpy_version = "1.23.5"
assert np.__version__ == expected_numpy_version, f"Expected NumPy version {expected_numpy_version}, but got {np.__version__}"
# Check TensorFlow version
expected_tf_version = "2.14.0"
assert tf.__version__ == expected_tf_version, f"Expected TensorFlow version {expected_tf_version}, but got {tf.__version__}"
# Check NLTK version
expected_nltk_version = "3.8.1"
assert nltk.__version__ == expected_nltk_version, f"Expected NLTK version {expected_nltk_version}, but got {nltk.__version__}"

print("All versions are as expected.")