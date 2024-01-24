---
description: Retrieves the name of the cryptographic service provider (CSP).
ms.assetid: b06d2839-0eaa-4f3f-99f7-d77e001fe4ea
title: PrivateKey.ProviderName property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PrivateKey.ProviderName
api_type:
- COM
api_location:
- Capicom.dll
---

# PrivateKey.ProviderName property

\[The **ProviderName** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PrivateKey Property**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2.privatekey) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **ProviderName** property retrieves the name of the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

## Syntax


```VB
PrivateKey.ProviderName As String
```



## Property value

A string that contains the name of the CSP.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrivateKey**](privatekey.md)
</dt> </dl>

 

 
