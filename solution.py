import pandas as pd
import math
df=pd.read_csv('logger.txt', sep=' ',header=None,names=['eater_id','foodmenu_id'])
duplicate=df[df.duplicated()]
if len(duplicate) !=0:
    errstr="Found eater_id with the same foodmenu_id more than once"
    raise TypeError(errstr)
else:
    df1=df.groupby(["foodmenu_id"]).count().sort_values(["eater_id"], ascending=False).rename(columns={"eater_id" : "Sum of eaters"}).reset_index().head(3)
    print(df1['foodmenu_id'].to_string(index=False))
