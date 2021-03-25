---
description: Determines whether the certificate has a private key associated with it. The method determines this by checking whether the CERT\_KEY\_PROV\_INFO\_PROP\_ID property is present.
ms.assetid: 80478956-1ed7-4c25-9ae3-d7176649e6d7
title: ICertificate2::HasPrivateKey method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate.HasPrivateKey
- ICertificate2.HasPrivateKey
- ICertificate.HasPrivateKey
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificate2::HasPrivateKey method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](/previous-versions/windows/embedded/hh424017(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **HasPrivateKey** method determines whether the [*certificate*](../secgloss/c-gly.md) has a [*private key*](../secgloss/p-gly.md) associated with it. The method determines this by checking whether the CERT\_KEY\_PROV\_INFO\_PROP\_ID property is present.

## Syntax


```VB
Certificate.HasPrivateKey()
```



## Parameters

This method has no parameters.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrivateKey.Open**](privatekey-open.md)
</dt> <dt>

[Cryptography Objects](cryptography-objects.md)
</dt> <dt>

[**Certificate**](certificate.md)
</dt> </dl>

 

 
