---
Description: Retrieves a collection of the policys qualifiers.
ms.assetid: aa5e2225-0a39-40bc-868c-d96f5953edaa
title: PolicyInformation.Qualifiers property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PolicyInformation.Qualifiers property

\[The **Qualifiers** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](T:System.Security.Cryptography.X509Certificates.X509Extension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process policy information in the Certificate policies extension.\]

The **Qualifiers** property retrieves a collection of the policy's qualifiers.

## Syntax


```VB
PolicyInformation.Qualifiers As Qualifiers
```



## Property value

The policy's Certification Practice Statement (CPS) pointer or user notice qualifiers, as a [**Qualifiers**](qualifiers.md) object.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| Header<br/>          | <dl> <dt>Iads.h</dt> </dl>      |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PolicyInformation**](policyinformation.md)
</dt> </dl>

 

 




