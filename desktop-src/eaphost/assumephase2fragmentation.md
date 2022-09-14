---
title: AssumePhase2Fragmentation
description: The AssumePhase2Fragmentation registry key determines if the server and client assume phase 2 fragmentation.
ms.assetid: 3d6ececf-8871-4038-9706-4da57857d25a
ms.topic: article
ms.date: 05/31/2018
---

# AssumePhase2Fragmentation

The AssumePhase2Fragmentation registry key determines if the server and client assume phase 2 fragmentation.

## Registry Entry

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\PPP\EAP\25
   AssumePhase2Fragmentation = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value   | Description                                                                                                  |
|---------|--------------------------------------------------------------------------------------------------------------|
| 0       | Server and client assume the other party is not capable of phase 2 fragmentation during PEAP authentication. |
| nonzero | Server and client assume the other party is capable of phase 2 fragmentation during PEAP authentication.     |



 

If this registry value is not present, the server and client assume the other party is capable of phase 2 fragmentation during PEAP authentication.

## Related topics

<dl> <dt>

[EAPHost Registry Settings](eaphost-registry-settings.md)
</dt> </dl>

 

 




