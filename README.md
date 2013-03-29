stockscrape
===========
API that provides Futures and Options data by scraping the NSE website

Futures

```python
from Futures import get_futures_data
get_futures_data('USDINR')
```

params - Currency symbol

Options

```python
from OptionChain import get_options_data, get_options_dates
#To get Options Data for a given expiry date
get_options_data('26APR2013')
#To get the 4 possible expiry dates
get_options_dates()
```
params - expiry date



