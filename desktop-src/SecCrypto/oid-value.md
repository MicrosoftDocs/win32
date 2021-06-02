---
description: Sets or retrieves the value of the OID dotted number of the identifier.
ms.assetid: bb960e65-776e-4ae8-a557-62254dc10558
title: OID.Value property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- OID.Value
api_type:
- COM
api_location:
- Capicom.dll
---

# OID.Value property

\[The **Value** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**Oid Class**](/dotnet/api/system.security.cryptography.oid?view=netcore-3.1) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Value** property sets or retrieves the value of the OID dotted number of the identifier.

## Syntax


```VB
OID.Value As String
```



## Property value

The value of the OID dotted number of the identifier. For possible values, see Wincrypt.h.

## Remarks

If the **Value** property is set, the [**FriendlyName**](oid-friendlyname.md) property is set to the corresponding display name. If the **FriendlyName** property is set, the **Value** property is set to the corresponding dotted value.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**OID**](oid.md)
</dt> </dl>

 

 
