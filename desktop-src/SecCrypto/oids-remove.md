---
description: Removes the specified OID object from the collection.
ms.assetid: c5eb6831-b195-4dc1-a6bd-d4245f9b0213
title: OIDs.Remove method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- OIDs.Remove
api_type:
- COM
api_location:
- Capicom.dll
---

# OIDs.Remove method

\[The **Remove** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**OidCollection Class**](/dotnet/api/system.security.cryptography.oidcollection?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Remove** method removes the specified [**OID**](oid.md) object from the collection.

## Syntax


```VB
OIDs.Remove( _
  ByVal Index _
)
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index of the [**OID**](oid.md) object to be removed. This can be either an index into the collection or the dotted value of the OID.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
