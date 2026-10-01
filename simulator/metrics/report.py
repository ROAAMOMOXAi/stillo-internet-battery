from dataclasses import asdict
from simulator.models.battery import ExperimentResult


def as_metrics(result: ExperimentResult) -> dict[str, int | float]:
    metrics = asdict(result)
    metrics["service_gain_bytes"] = result.service_gain_bytes
    metrics["efficiency"] = result.efficiency
    return metrics
