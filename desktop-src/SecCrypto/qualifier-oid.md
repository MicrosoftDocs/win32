---
description: Retrieves the object ID of the qualifier.
ms.assetid: 58ec2af7-f085-43bc-8ea8-926cb840abe9
title: Qualifier.OID property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Qualifier.OID
api_type:
- COM
api_location:
- Capicom.dll
---

# Qualifier.OID property

\[The **OID** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509extension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process qualifiers that are part of the policy information in the Certificate Policies extension.\]

The **OID** property retrieves the object ID of the qualifier. This is the default property.

## Syntax


```VB
Qualifier.OID As OID
```



## Property value

An [**OID**](oid.md) object that identifies the qualifier.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Qualifier**](qualifier.md)
</dt> </dl>

 

 
