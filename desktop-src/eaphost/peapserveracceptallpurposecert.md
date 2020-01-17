---
title: PeapServerAcceptAllPurposeCert
description: The PeapServerAcceptAllPurposeCert registry key determines if all-purpose certificates are accepted for PEAP authentication.
ms.assetid: 59C58459-7735-4733-9F95-646864802D70
ms.topic: article
ms.date: 05/31/2018
---

# PeapServerAcceptAllPurposeCert

The PeapServerAcceptAllPurposeCert registry key determines if all-purpose certificates are accepted for PEAP authentication.

## Registry Entry

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\PPP\EAP\25
   PeapServerAcceptAllPurposeCert = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value        | Description                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------------------|
| 1            | Server and client accept all-purpose certificates sent by the other party for EAP-TLS authentication.       |
| Other values | Server and client do not accept all-purpose certificates sent by the other party for EAP-TLS authentication |



 

If this registry value is not present, the server and client accept all-purpose certificates sent by the other party for PEAP authentication.

## Related topics

<dl> <dt>

[EAPHost Registry Settings](eaphost-registry-settings.md)
</dt> </dl>

 

 




