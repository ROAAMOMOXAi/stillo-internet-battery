# Architecture

## Experimental loop

OBSERVE → CHARGE → DISCONNECT → PERSIST → RECONNECT → REDEEM → MEASURE → COMPARE

## Layers

- **Network model:** temporary connectivity opportunities and physical capacity.
- **STILLO resource model:** persistent representation created from an observed opportunity.
- **Persistence:** durable state surviving the simulated outage.
- **Redemption:** conversion of persistent state into simulated service during a later connection.
- **Metrics:** numerical comparison of baseline and STILLO outcomes.

The first implementation must remain modular so a dedicated network simulator can replace the initial model later.
