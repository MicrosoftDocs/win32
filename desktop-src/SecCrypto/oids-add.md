---
Description: Adds the specified OID object to the collection.
ms.assetid: 0ae087d6-768a-4538-b834-0f936680de05
title: OIDs.Add method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- OIDs.Add
api_type:
- COM
api_location:
- Capicom.dll
---

# OIDs.Add method

\[The **Add** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**OidCollection Class**](https://msdn.microsoft.com/library/023e15dk(v=VS.90).aspx) in the [**System.Security.Cryptography**](https://msdn.microsoft.com/library/9eat8fht(v=VS.100).aspx) namespace.\]

The **Add** method adds the specified [**OID**](oid.md) object to the collection.

## Syntax


```VB
OIDs.Add( _
  ByVal OID _
)
```



## Parameters

<dl> <dt>

*OID* \[in\]
</dt> <dd>

The [**OID**](oid.md) object to be added to the collection. The **OID** object is added in sorted order based on its dotted value.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




