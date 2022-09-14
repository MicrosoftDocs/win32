---
title: BypassNegotiation
description: The BypassNegotiation registry key determines if capabilities negotiation between the server and client occurs or if pre-configured settings are used.
ms.assetid: 51e21e9c-d6cb-454b-9584-3f48d76a649a
ms.topic: article
ms.date: 05/31/2018
---

# BypassNegotiation

The BypassNegotiation registry key determines if capabilities negotiation between the server and client occurs or if pre-configured settings are used.

## Registry Entry

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\PPP\EAP\25
   BypassNegotiation = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value   | Description                                                                                                                                                                                          |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0       | Server and client negotiate EAP capabilities.                                                                                                                                                        |
| nonzero | Server and client do not negotiate EAP capabilities. Server and client use the [AssumePhase2Fragmentation](assumephase2fragmentation.md) registry key value to find the other party's capabilities. |



 

If this registry value is not present, the server and client negotiate EAP capabilities..

## Related topics

<dl> <dt>

[EAPHost Registry Settings](eaphost-registry-settings.md)
</dt> </dl>

 

 




