---
description: Returns a BasicConstraints object that represents the basic constraints extension of the certificate.
ms.assetid: cc4e566a-5f68-4e28-9397-39f22a71e45b
title: ICertificate2::BasicConstraints method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate.BasicConstraints
- ICertificate2.BasicConstraints
- ICertificate.BasicConstraints
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificate2::BasicConstraints method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **BasicConstraints** method returns a [**BasicConstraints**](basicconstraints.md) object that represents the basic constraints extension of the certificate.

## Syntax


```VB
Certificate.BasicConstraints()
```



## Parameters

This method has no parameters.

## Return value

The [**BasicConstraints**](basicconstraints.md) object that represents the basic constraints extension of the certificate.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
