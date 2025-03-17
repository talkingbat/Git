from tradingview import tvDatafeed,Interval

tv=TvDatafeed

intervals=[Interval.in_1_minute,
Interval.in_5_minute,
Interval.in_15_minute,
Interval.in_30_minute,
Interval.in_1_hour,
Interval.in_4_hour,
Interval.in_daily]

t=tv.get_hist(symbol='nas100',exchange='eightcap',interval=Interval.in_1_hour,n_bars=1000)
print(t)



