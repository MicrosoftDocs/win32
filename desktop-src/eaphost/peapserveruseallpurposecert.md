---
title: PeapServerUseAllPurposeCert
description: The PeapServerUseAllPurposeCert registry key determines if all-purpose certificates are used for PEAP authentication.
ms.assetid: e239fb88-4bf3-49b6-a95c-67a8c060a50d
ms.topic: article
ms.date: 05/31/2018
---

# PeapServerUseAllPurposeCert

The PeapServerUseAllPurposeCert registry key determines if all-purpose certificates are used for PEAP authentication.

## Registry Entry

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\PPP\EAP\25
   PeapServerUseAllPurposeCert = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value        | Description                                                                                                      |
|--------------|------------------------------------------------------------------------------------------------------------------|
| 1            | All-purpose certificates in the client's or server's certificate store are selected for PEAP authentication.     |
| Other values | All-purpose certificates in the client's or server's certificate store are not selected for PEAP authentication. |



 

If this registry value is not present, all-purpose certificates in the client's or server's certificate store are selected for PEAP authentication.

## Related topics

<dl> <dt>

[EAPHost Registry Settings](eaphost-registry-settings.md)
</dt> </dl>

 

 




