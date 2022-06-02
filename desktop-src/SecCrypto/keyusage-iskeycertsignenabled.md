---
description: Retrieves a Boolean value that indicates whether the keyCertSign bit is set.
ms.assetid: c0331293-4a65-40f0-a404-87d8546349c2
title: KeyUsage.IsKeyCertSignEnabled property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsKeyCertSignEnabled
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsKeyCertSignEnabled property

\[The **IsKeyCertSignEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509enhancedkeyusageextension?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **IsKeyCertSignEnabled** property retrieves a Boolean value that indicates whether the keyCertSign bit is set.

## Syntax


```VB
KeyUsage.IsKeyCertSignEnabled As Boolean
```



## Property value

If **true**, the keyCertSign bit is set.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 
