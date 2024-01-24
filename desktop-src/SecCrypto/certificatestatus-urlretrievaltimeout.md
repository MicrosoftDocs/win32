---
description: Sets or retrieves the length of time before a URL is determined to be unreachable.
ms.assetid: f39dafc4-6017-463c-aeee-948b6173862a
title: CertificateStatus.UrlRetrievalTimeout property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CertificateStatus.UrlRetrievalTimeout
api_type:
- COM
api_location:
- Capicom.dll
---

# CertificateStatus.UrlRetrievalTimeout property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ChainStatus Structure**](/dotnet/api/system.security.cryptography.x509certificates.x509chainstatus) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **UrlRetrievalTimeout** property sets or retrieves the length of time before a URL is determined to be unreachable.

## Syntax


```VB
CertificateStatus.UrlRetrievalTimeout As Long
```



## Property value

The number of seconds before a URL is determined to be unreachable.

## Remarks

If this property is not set, the default time-out is 15 seconds.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
