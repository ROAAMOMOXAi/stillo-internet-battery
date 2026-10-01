import unittest

from simulator.models.battery import Contact
from simulator.scenarios.charge_redeem import charge, redeem, run_experiment


class ChargeRedeemTests(unittest.TestCase):
    def test_charge_persists_expected_amount(self):
        result = charge(Contact(10, 100), efficiency=0.8)
        self.assertEqual(result.available_bytes, 1000)
        self.assertEqual(result.persisted_bytes, 800)
        self.assertEqual(result.overhead_bytes, 200)

    def test_redeem_is_limited_by_physical_capacity(self):
        result = redeem(Contact(5, 100), 800)
        self.assertEqual(result.redeemed_bytes, 500)
        self.assertEqual(result.remaining_credit_bytes, 300)

    def test_end_to_end_experiment(self):
        result = run_experiment(
            Contact(10, 100),
            Contact(5, 100),
            outage_duration_s=30,
            charge_efficiency=0.8,
        )
        self.assertEqual(result.persisted_bytes, 800)
        self.assertEqual(result.redeemed_bytes, 500)
        self.assertEqual(result.stillo_service_bytes, 500)
        self.assertEqual(result.baseline_service_bytes, 0)


if __name__ == "__main__":
    unittest.main()
