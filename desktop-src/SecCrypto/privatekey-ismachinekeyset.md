---
description: Returns a Boolean value that indicates whether the private key belongs to a machine key set.
ms.assetid: ea13ba68-30ae-4aa4-b490-29fd4542c621
title: PrivateKey.IsMachineKeyset method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PrivateKey.IsMachineKeyset
api_type:
- COM
api_location:
- Capicom.dll
---

# PrivateKey.IsMachineKeyset method

\[The **IsMachineKeyset** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PrivateKey Property**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2.privatekey?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **IsMachineKeyset** method returns a Boolean value that indicates whether the private key belongs to a machine key set.

## Syntax


```VB
PrivateKey.IsMachineKeyset()
```



## Parameters

This method has no parameters.

## Return value

If true, the private key belongs to a machine key set.

## Remarks

The return value of this method is dependent on the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) used. This method will return a trustworthy value if a Microsoft CSP is used. If the CSP is not a Microsoft CSP, the return value cannot be trusted to be accurate.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrivateKey**](privatekey.md)
</dt> </dl>

 

 
