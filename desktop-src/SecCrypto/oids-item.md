---
description: Retrieves an OID object from the collection. This is the default property.
ms.assetid: af0de567-e520-411d-850d-fbdbcb2ace69
title: OIDs.Item property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- OIDs.Item
api_type:
- COM
api_location:
- Capicom.dll
---

# OIDs.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**OidCollection Class**](/dotnet/api/system.security.cryptography.oidcollection) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Item** property retrieves an [**OID**](oid.md) object from the collection. This is the default property.

## Syntax


```VB
OIDs.Item( _
  ByVal Index _
) As Variant
```



## Property value

The [**OID**](oid.md) object at the specified index, or the **OID** object with the specified dotted value.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**OIDs**](oids.md)
</dt> </dl>

 

 
