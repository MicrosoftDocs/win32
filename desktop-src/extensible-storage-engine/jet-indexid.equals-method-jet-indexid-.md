---
description: "Learn more about: JET_INDEXID.Equals method (JET_INDEXID)"
title: JET_INDEXID.Equals method (JET_INDEXID)
TOCTitle: Equals method (JET_INDEXID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_INDEXID.Equals(Microsoft.Isam.Esent.Interop.JET_INDEXID)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexid.equals(v=EXCHG.10)
ms:contentKeyID: 39515277
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXID.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXID.Equals method (JET_INDEXID)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_INDEXID _
) As Boolean
'Usage
Dim instance As JET_INDEXID
Dim other As JET_INDEXID
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_INDEXID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_INDEXID](./jet-indexid-structure2.md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](/dotnet/api/system.iequatable-1.equals#System_IEquatable_1_Equals__0_)  

## See also

#### Reference

[JET_INDEXID structure](./jet-indexid-structure2.md)

[JET_INDEXID members](./jet-indexid-members.md)

[Equals overload](./jet-indexid.equals-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
