import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 291445198

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    return anderson_ksamp([x, y])[2] < alpha
