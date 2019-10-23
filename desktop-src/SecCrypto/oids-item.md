---
Description: Retrieves an OID object from the collection. This is the default property.
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

\[The **Item** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**OidCollection Class**](https://msdn.microsoft.com/library/023e15dk(v=VS.90).aspx) in the [**System.Security.Cryptography**](https://msdn.microsoft.com/library/9eat8fht(v=VS.100).aspx) namespace.\]

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



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**OIDs**](oids.md)
</dt> </dl>

 

 




