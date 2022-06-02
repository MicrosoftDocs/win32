---
description: Retrieves a Boolean value that indicates whether the KeyUsage extension is present.
ms.assetid: 'd666049a-4b40-42b6-8c2d-c27a1bb4c48a'
title: KeyUsage.IsPresent property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsPresent
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsPresent property

\[The **IsPresent** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509enhancedkeyusageextension?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **IsPresent** property retrieves a Boolean value that indicates whether the [**KeyUsage**](keyusage.md) extension is present.

This property is the default property of the [**KeyUsage**](keyusage.md) object.

## Syntax


```VB
KeyUsage.IsPresent As Boolean
```



## Property value

If **true**, the KeyUsage extension is present.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 
