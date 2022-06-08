---
description: Retrieves the parameters of the public key algorithm.
ms.assetid: 1d12f72e-0144-4b7b-b468-d2f35bf253d3
title: PublicKey.EncodedParameters property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PublicKey.EncodedParameters
api_type:
- COM
api_location:
- Capicom.dll
---

# PublicKey.EncodedParameters property

\[The **EncodedParameters** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PublicKey Property**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2.publickey) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **EncodedParameters** property retrieves the parameters of the public key algorithm.

## Syntax


```VB
PublicKey.EncodedParameters As EncodedData
```



## Property value

An [**EncodedData**](encodeddata.md) object that provides access to the parameters of the public key algorithm.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PublicKey**](publickey.md)
</dt> </dl>

 

 
