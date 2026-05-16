#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "common/mail/order-reminder-html.php": [
        "Html::encode($agent_name)",
        "Html::encode($order->order_uuid)",
    ],
    "common/mail/maintenance-announcement-html.php": [
        "Html::encode($agent->agent_name)",
    ],
}

for rel_path, required in checks.items():
    source = (ROOT / rel_path).read_text()
    for needle in required:
        if needle not in source:
            raise SystemExit(f"{rel_path} is missing {needle}")

forbidden = {
    "common/mail/order-reminder-html.php": [
        "Dear <?= $agent_name ?>",
        "Order #<?= $order->order_uuid ?>",
    ],
    "common/mail/maintenance-announcement-html.php": [
        "Hello <?= $agent->agent_name ?>",
    ],
}

for rel_path, raw_patterns in forbidden.items():
    source = (ROOT / rel_path).read_text()
    for pattern in raw_patterns:
        if pattern in source:
            raise SystemExit(f"{rel_path} still renders raw value: {pattern}")

print("order reminder and maintenance email escaping checks passed")
