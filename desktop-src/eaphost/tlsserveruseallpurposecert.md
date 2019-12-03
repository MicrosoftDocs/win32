---
title: TlsServerUseAllPurposeCert
description: The TlsServerUseAllPurposeCert registry key determines if all-purpose certificates are used for EAP-TLS authentication.
ms.assetid: a672cecb-6bba-4ba6-b362-f6d5a220184b
ms.topic: article
ms.date: 05/31/2018
---

# TlsServerUseAllPurposeCert

The TlsServerUseAllPurposeCert registry key determines if all-purpose certificates are used for EAP-TLS authentication.

## Registry Entry

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\PPP\EAP\13
   TlsServerUseAllPurposeCert = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value        | Description                                                                                                      |
|--------------|------------------------------------------------------------------------------------------------------------------|
| 1            | All-purpose certificates in the client's or server's certificate store are selected for PEAP authentication.     |
| Other values | All-purpose certificates in the client's or server's certificate store are not selected for PEAP authentication. |



 

If this registry value is not present, all-purpose certificates in the client's or server's certificate store are selected for EAP-TLS authentication.

## Related topics

<dl> <dt>

[EAPHost Registry Settings](eaphost-registry-settings.md)
</dt> </dl>

 

 




