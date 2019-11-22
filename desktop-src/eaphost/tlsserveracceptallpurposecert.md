---
title: TlsServerAcceptAllPurposeCert
description: The TlsServerAcceptAllPurposeCert registry key determines if all-purpose certificates are accepted for EAP-TLS authentication.
ms.assetid: F0881397-5D8C-4C8F-8EB5-6D59454C55B7
ms.topic: article
ms.date: 05/31/2018
---

# TlsServerAcceptAllPurposeCert

The TlsServerAcceptAllPurposeCert registry key determines if all-purpose certificates are accepted for EAP-TLS authentication.

## Registry Entry

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\PPP\EAP\13
   TlsServerAcceptAllPurposeCert = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value        | Description                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------------------|
| 1            | Server and client accept all-purpose certificates sent by the other party for EAP-TLS authentication.       |
| Other values | Server and client do not accept all-purpose certificates sent by the other party for EAP-TLS authentication |



 

If this registry value is not present, the server and client accept all-purpose certificates sent by the other party for EAP-TLS authentication.

## Related topics

<dl> <dt>

[EAPHost Registry Settings](eaphost-registry-settings.md)
</dt> </dl>

 

 




