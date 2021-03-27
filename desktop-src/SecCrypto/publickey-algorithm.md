---
description: The Algorithm property retrieves the OID object that identifies the algorithm used by the public key. This is the default property.
ms.assetid: f804ac4b-6a33-4f25-950b-6b6838bcc638
title: PublicKey.Algorithm property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PublicKey.Algorithm
api_type:
- COM
api_location:
- Capicom.dll
---

# PublicKey.Algorithm property

\[The **Algorithm** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PublicKey Property**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2.publickey?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **Algorithm** property retrieves the [**OID**](oid.md) object that identifies the algorithm used by the public key. This is the default property.

## Syntax


```VB
PublicKey.Algorithm As OID
```



## Property value

The [**OID**](oid.md) object that identifies the algorithm used by the public key.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PublicKey**](publickey.md)
</dt> </dl>

 

 
