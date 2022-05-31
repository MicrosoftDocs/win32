---
description: Retrieves the value of the public key.
ms.assetid: d9846ebe-44df-4ee0-8f15-cc96883d9d53
title: PublicKey.EncodedKey property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PublicKey.EncodedKey
api_type:
- COM
api_location:
- Capicom.dll
---

# PublicKey.EncodedKey property

\[The **EncodedKey** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PublicKey Property**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2.publickey?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **EncodedKey** property retrieves the value of the public key.

## Syntax


```VB
PublicKey.EncodedKey As EncodedData
```



## Property value

An [**EncodedData**](encodeddata.md) object that provides access to the value of the public key.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PublicKey**](publickey.md)
</dt> </dl>

 

 
