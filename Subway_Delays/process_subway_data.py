import pandas as pd

if __name__ == "__main__":
  income_df = pd.read_csv("./SubwayIncome.csv")
  income_groups = income_df.groupby("line")
  medians = income_groups["income2011"].median()
  medians.to_csv("./IncomeMedians.csv")
  
  ontime_df = pd.read_csv("./SubwayOnTime.csv")
  print(ontime_df.head())