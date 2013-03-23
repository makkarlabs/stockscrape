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
from OptionChain import get_options_data
get_options_data('26APR2013','USDINR')
```
params - expiry date, currency symbol(default - USDINR)
