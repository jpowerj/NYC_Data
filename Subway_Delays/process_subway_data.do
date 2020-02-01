clear
set more off

import delimited "./IncomeMedians.csv"

drop if line == "7" | line == "L"

graph twoway (lfitci ontime_2017 median_income_2011) (scatter ontime_2017 median_income_2011, mlabel(line)), xtitle("Median Income of Stops, 2011") ytitle("On-Time Percentage, 2017")
