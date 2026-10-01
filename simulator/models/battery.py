from dataclasses import dataclass


@dataclass(frozen=True)
class Contact:
    duration_s: float
    capacity_bytes_per_s: float

    @property
    def capacity_bytes(self) -> int:
        return max(0, int(self.duration_s * self.capacity_bytes_per_s))


@dataclass(frozen=True)
class ChargeResult:
    available_bytes: int
    transferred_bytes: int
    charged_bytes: int
    persisted_bytes: int
    overhead_bytes: int


@dataclass(frozen=True)
class RedemptionResult:
    physical_capacity_bytes: int
    redeemed_bytes: int
    service_delivered_bytes: int
    remaining_credit_bytes: int


@dataclass(frozen=True)
class ExperimentResult:
    baseline_service_bytes: int
    stillo_service_bytes: int
    charged_bytes: int
    persisted_bytes: int
    redeemed_bytes: int
    remaining_credit_bytes: int
    overhead_bytes: int
    outage_duration_s: float
    redemption_delay_s: float

    @property
    def service_gain_bytes(self) -> int:
        return self.stillo_service_bytes - self.baseline_service_bytes

    @property
    def efficiency(self) -> float:
        if self.charged_bytes == 0:
            return 0.0
        return self.redeemed_bytes / self.charged_bytes
