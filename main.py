import pandas as pd
pdDataFrame = pd.read_csv("data.csv")
pdDataFrame1=pd.read_csv("music_recommendations.csv")
result=pd.concat([pdDataFrame, pdDataFrame1])
print(result)