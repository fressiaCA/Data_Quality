import profile
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
#install
#pip install pandas-profiling[notebook]

#to generate df
df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])

#to generate the report
profile = ProfileReport(df, title="ProfilingReport")
profile.to_file("your_report.html")   