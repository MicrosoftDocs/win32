---
Description: 'Adds the specified OID object to the collection.'
ms.assetid: '0ae087d6-768a-4538-b834-0f936680de05'
title: 'OIDs.Add method'
---

# OIDs.Add method

\[The **Add** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**OidCollection Class**](T:System.Security.Cryptography.OidCollection) in the [**System.Security.Cryptography**](frlrfSystemSecurityCryptography) namespace.\]

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



 

 




