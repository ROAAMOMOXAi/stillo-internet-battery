# Model

The first model represents connectivity as a time-bounded opportunity to transfer data.

A STILLO resource is a persistent accounting representation of value captured during that opportunity. It is not stored bandwidth.

The model has two phases:

1. **Charge:** during a contact window, available capacity is measured and a bounded amount is recorded as persistent resource.
2. **Redeem:** during a later contact window, the persisted resource can authorize simulated service, limited by actual physical capacity.

The simulation keeps physical transfer and persistent accounting separate so the experiment cannot accidentally treat a credit as physical bandwidth.
