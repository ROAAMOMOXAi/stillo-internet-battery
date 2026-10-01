# Simulator

The initial simulator is deliberately dependency-light and deterministic.

Inputs describe:

- contact duration;
- physical capacity;
- charge efficiency;
- redemption capacity;
- outage duration;
- optional credit expiry.

Outputs are numerical and reproducible.

The simulator is intentionally separate from any particular network simulator. A future adapter can map contact opportunities from The ONE or another simulator into the same experiment model.
