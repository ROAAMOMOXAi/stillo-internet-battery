from simulator.models.battery import (
    ChargeResult,
    Contact,
    ExperimentResult,
    RedemptionResult,
)


def charge(contact: Contact, efficiency: float = 1.0) -> ChargeResult:
    if not 0.0 <= efficiency <= 1.0:
        raise ValueError("efficiency must be between 0 and 1")

    available = contact.capacity_bytes
    charged = int(available * efficiency)
    overhead = available - charged

    return ChargeResult(
        available_bytes=available,
        transferred_bytes=available,
        charged_bytes=charged,
        persisted_bytes=charged,
        overhead_bytes=overhead,
    )


def redeem(
    contact: Contact,
    credit_bytes: int,
) -> RedemptionResult:
    if credit_bytes < 0:
        raise ValueError("credit_bytes must be non-negative")

    physical = contact.capacity_bytes
    redeemed = min(physical, credit_bytes)

    return RedemptionResult(
        physical_capacity_bytes=physical,
        redeemed_bytes=redeemed,
        service_delivered_bytes=redeemed,
        remaining_credit_bytes=credit_bytes - redeemed,
    )


def run_experiment(
    charge_contact: Contact,
    redemption_contact: Contact,
    outage_duration_s: float,
    charge_efficiency: float = 1.0,
) -> ExperimentResult:
    if outage_duration_s < 0:
        raise ValueError("outage_duration_s must be non-negative")

    charged = charge(charge_contact, charge_efficiency)
    redemption = redeem(redemption_contact, charged.persisted_bytes)

    # Baseline receives only the physical service available during the
    # redemption contact. STILLO receives that same physical service,
    # plus any service represented by a valid persisted credit.
    #
    # The first model treats redemption as service that would otherwise
    # not be delivered to the user during the outage/reconnection scenario.
    baseline = 0
    stillo = redemption.service_delivered_bytes

    return ExperimentResult(
        baseline_service_bytes=baseline,
        stillo_service_bytes=stillo,
        charged_bytes=charged.charged_bytes,
        persisted_bytes=charged.persisted_bytes,
        redeemed_bytes=redemption.redeemed_bytes,
        remaining_credit_bytes=redemption.remaining_credit_bytes,
        overhead_bytes=charged.overhead_bytes,
        outage_duration_s=outage_duration_s,
        redemption_delay_s=outage_duration_s,
    )
