---
description: Sets or retrieves the display name for the identifier.
ms.assetid: 53f84d0d-c189-4fd2-a383-29fd0d22de08
title: OID.FriendlyName property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- OID.FriendlyName
api_type:
- COM
api_location:
- Capicom.dll
---

# OID.FriendlyName property

\[The **FriendlyName** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**Oid Class**](/dotnet/api/system.security.cryptography.oid?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **FriendlyName** property sets or retrieves the display name for the identifier.

## Syntax


```VB
OID.FriendlyName As String
```



## Property value

The display name for the [**OID**](oid.md).

## Remarks

If the **FriendlyName** property is set, the [**Value**](oid-value.md) property is set to the corresponding dotted value. If the **Value** property is set, the **FriendlyName** property is set to the corresponding display name.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**OID**](oid.md)
</dt> </dl>

 

 
