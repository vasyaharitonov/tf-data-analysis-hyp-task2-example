import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp


chat_id = 291445198

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    return cramervonmises_2samp(x, y).pvalue < alpha
