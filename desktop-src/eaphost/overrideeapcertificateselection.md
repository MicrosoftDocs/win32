---
title: OverrideEAPCertificateSelection
description: The OverrideEAPCertificateSelection registry key determines whether the client will override the default smart card certificate selection behavior and provide the user with more certificates to choose from.
ms.assetid: 469FECA9-FF2A-46B1-9370-0FF28EF2FB33
ms.topic: article
ms.date: 05/31/2018
---

# OverrideEAPCertificateSelection

The OverrideEAPCertificateSelection registry key determines whether the client will override the default smart card certificate selection behavior and provide the user with more certificates to choose from.

## Registry Entry

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\PPP\EAP\13
   OverrideEAPCertificateSelection = value
```

## Remarks

This is a **REG\_BINARY** value.



| Value | Description                                                                                                                                                                                          |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x000 | Do not override the default behavior.                                                                                                                                                                |
| 0x001 | Choose the last attached certificate from the smart card.                                                                                                                                            |
| 0x010 | Shows all certificates in the certificate selection UI from the smart card.                                                                                                                          |
| 0x100 | Shows all certificates in the certificate selection UI from the registry.                                                                                                                            |
| 0x101 | Shows all certificates in the certificate selection UI from the registry and the last attached certificate from the smart card. Shows the last attached certificate from the smart card as selected. |
| 0x110 | Shows all certificates in the certificate selection UI from the registry and the smart card.                                                                                                         |



 

## Related topics

<dl> <dt>

[EAPHost Registry Settings](eaphost-registry-settings.md)
</dt> </dl>

 

 




