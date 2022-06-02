---
description: Retrieves a Boolean value that indicates whether the keyEncipherment bit is set.
ms.assetid: 2bdce181-3de7-4dc1-8059-1e1ca96c0d2d
title: KeyUsage.IsKeyEnciphermentEnabled property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- KeyUsage.IsKeyEnciphermentEnabled
api_type:
- COM
api_location:
- Capicom.dll
---

# KeyUsage.IsKeyEnciphermentEnabled property

\[The **IsKeyEnciphermentEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509enhancedkeyusageextension?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **IsKeyEnciphermentEnabled** property retrieves a Boolean value that indicates whether the keyEncipherment bit is set.

## Syntax


```VB
KeyUsage.IsKeyEnciphermentEnabled As Boolean
```



## Property value

If **true**, the keyEncipherment bit is set.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 
