---
description: The Result property retrieves a value that indicates whether the certificate is valid. This is the default property.
ms.assetid: b1edfbde-9d54-4e9c-ba9b-33e4c354c23f
title: CertificateStatus.Result property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CertificateStatus.Result
api_type:
- COM
api_location:
- Capicom.dll
---

# CertificateStatus.Result property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ChainStatus Structure**](/dotnet/api/system.security.cryptography.x509certificates.x509chainstatus?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **Result** property retrieves a value that indicates whether the certificate is valid. This is the default property.

## Syntax


```VB
CertificateStatus.Result As Boolean
```



## Property value

If **true**, the certificate is valid. The certificate's validity is checked using the current setting of the [**CheckFlag**](certificatestatus-checkflag.md) property and the various policy settings.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
