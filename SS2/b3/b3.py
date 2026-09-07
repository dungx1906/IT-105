def calculate_driver_payout(transactions):
    result = {}

    for transaction in transactions:
        driver = transaction["driver_id"]
        status = transaction["status"]

        if driver not in result:
            result[driver] = {
                "successful_orders": 0,
                "held_orders": 0,
                "payout": 0,
                "bonus": 0
            }

        if status == "DELIVERED":
            result[driver]["successful_orders"] += 1
            result[driver]["payout"] += 20000

        elif status == "DISPUTED":
            result[driver]["held_orders"] += 1

    for driver in result:
        if result[driver]["successful_orders"] > 50:
            result[driver]["bonus"] = result[driver]["payout"] * 0.1
            result[driver]["payout"] += result[driver]["bonus"]

    return result