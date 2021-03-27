---
description: Retrieves a hexadecimal string that contains the SHA-1 hash of the certificate.
ms.assetid: 6fd6f3ba-f7a9-43a3-a8da-8fd826649a92
title: Certificate.Thumbprint property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate.Thumbprint
api_type:
- COM
api_location:
- Capicom.dll
---

# Certificate.Thumbprint property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](/previous-versions/windows/embedded/hh424017(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **Thumbprint** property retrieves a hexadecimal string that contains the [*SHA-1*](../secgloss/s-gly.md) hash of the certificate.

This property is read-only.

## Syntax


```VB
Certificate.Thumbprint As String
```



## Property value

A hexadecimal string that contains the SHA-1 hash of the certificate.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Certificate**](certificate.md)
</dt> </dl>

 

 
