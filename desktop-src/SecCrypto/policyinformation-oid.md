---
description: Retrieves the policy's OID. This is the default property.
ms.assetid: c78bbbcb-befd-491c-afbd-80c3ba124d29
title: PolicyInformation.OID property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PolicyInformation.OID
api_type:
- COM
api_location:
- Capicom.dll
---

# PolicyInformation.OID property

\[The **OID** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509extension) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process policy information in the Certificate policies extension.\]

The **OID** property retrieves the policy's OID. This is the default property.

## Syntax


```VB
PolicyInformation.OID As OID
```



## Property value

The policy's object identifier as an [**OID**](oid.md) object.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PolicyInformation**](policyinformation.md)
</dt> </dl>

 

 
