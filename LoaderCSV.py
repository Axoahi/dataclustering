import pandas as pd;

# We must specify ";" delimiter with our dataset (the default delimitr is "," and it gives us problems)
rawturbdata = pd.read_csv("C:/Users/Buba/OneDrive/LucentiaLab/DemoClustering141218/CopiaDatosMATLAB.csv", delimiter=";");

print(rawturbdata);