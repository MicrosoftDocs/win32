---
title: License Protection
description: Use the License Protection APIs to register and validate protected license keys, with an expiration date, on a Windows device.
ms.topic: reference
ms.date: 10/06/2026
---

# License Protection

<!-- SME review: confirm this summary accurately describes the scenario/use case for these APIs. -->
Use the License Protection APIs to register a license key with an associated expiration date, and later validate that the key is still protected and within its validity period.

## In this section

### Functions

| Topic | Description |
|--|--|
| [**RegisterLicenseKeyWithExpiration**](/windows/desktop/api/licenseprotection/nf-licenseprotection-registerlicensekeywithexpiration) | Registers a license key and associates an expiration date with it. |
| [**ValidateLicenseKeyProtection**](/windows/desktop/api/licenseprotection/nf-licenseprotection-validatelicensekeyprotection) | Validates a license key that was previously registered and returns its validity period and protection status. |

### Enumerations

| Topic | Description |
|--|--|
| [**LicenseProtectionStatus**](/windows/desktop/api/licenseprotection/ne-licenseprotection-licenseprotectionstatus) | Describes the protection state of a license key. |

<!--
Open questions for SME:
- Is there any public-use requirement/eligibility (e.g. must be a signed/Store app, specific capability, or account requirement) callers should be aware of before calling these APIs? John's 9/28 notes said "I don't know of any 'public-use requirements'" — confirming there are none to document, or pointing us to someone who'd know, would let us finalize this page.
- Should this page link to a related conceptual topic (e.g. an existing licensing/DRM overview) for context, or do these APIs stand alone?
-->
