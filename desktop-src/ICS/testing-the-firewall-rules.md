---
title: Testing the Firewall Rules
description: The following checklist covers the recommendations that your test team should adopt in its test code.
ms.assetid: '82531de2-57e9-44ed-a7ac-2a244965bfd2'
---

# Testing the Firewall Rules

The following checklist covers the recommendations that your test team should adopt in its test code.

-   Testing the firewall integration should include complete end-to-end product tests.
-   Ensure that the firewall service is running: disabling or stopping the firewall service is not a supported scenario because the firewall provides Windows Service Hardening support.
-   Ensure that the firewall is turned ON before starting the tests.
-   Ensure that the test code does not:
    -   Add firewall rules on behalf of the product being tested.
    -   Add its own rules.
-   Ensure that the product is plumbing the firewall rules properly during setup.
    -   Take a snapshot of the firewall policy before installing the product using the firewall APIs.

        For an example that enumerates firewall rules, see [Enumerating Firewall Rules](enumerating-firewall-rules.md). For an example that enumerates firewall rules matching a specific group string, see [Enumerating Firewall Rules with a Matching Group String](enumerating-firewall-rules-with-a-matching-group-string.md). For an example that checks if a firewall rule is enabled, see [Checking if a Rule is Enabled](checking-if-a-rule-is-enabled.md).

    -   Install the product.
    -   Take another snapshot of the firewall policy after the product has been installed separately.
    -   Validate that the difference between the two snapshots matches the reference firewall policy.
    -   Uninstall the product.
    -   Validate that the firewall rules have been completely removed for the product only.

-   If the product has various deployment scenarios requiring enabling different firewall groups, ensure that these groups are properly enabled/disabled as each scenario is tested.

## Testing firewall rules for regressions

You should leverage the reference firewall policy that you have created to check that successive builds of the product comply with it. Testing for firewall rule regressions is an important part of the product development cycle which can have serious consequences if not observed, such as the following:

-   Increased attack surface to the product
-   Increased attack surface to server itself
-   Broken network connectivity or features

 

 




