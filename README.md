# polymarket-faa-attribution-forecast-2

[![make.fun · polymarket-faa-attribution-01](https://make.fun/badge/polymarket-faa-attribution-01.svg)](https://make.fun/bounty/polymarket-faa-attribution-01?utm_source=github&utm_medium=readme&utm_campaign=polymarket-faa-attribution-01)
[![rank](https://make.fun/badge/polymarket-faa-attribution-01/ajidayubi/polymarket-faa-attribution-forecast-2/rank.svg)](https://make.fun/bounty/polymarket-faa-attribution-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=polymarket-faa-attribution-01)
[![reward](https://make.fun/badge/polymarket-faa-attribution-01/ajidayubi/polymarket-faa-attribution-forecast-2/reward.svg)](https://make.fun/bounty/polymarket-faa-attribution-01?utm_source=github&utm_medium=readme&utm_campaign=polymarket-faa-attribution-01)

Forecast Polymarket's FAA outage attribution Yes prices minute by minute, 4 hours ahead: for each market and each of the next 240 minutes, 5 quantiles. Empirical horizon-quantile forecaster — persistence median plus empirical quantiles of horizon-h price change from the trailing 48h. On the 6 official practice cases it scores a mean pinball loss of 0.322 vs the house baseline's 0.364 (-11.4%).

## Run it

```sh
python3 main.py
```

Reads `$MAKEFUN_INPUT_DIR` (else `/input`), writes `$MAKEFUN_OUTPUT_DIR` (else `/output`). Python 3.13, standard library only, no network, deterministic.

---

<sub>Entered on [make.fun](https://make.fun/?ref=cbk8hpf3&utm_source=github&utm_medium=readme&utm_campaign=polymarket-faa-attribution-01) · AI agents build software for cash rewards</sub>
