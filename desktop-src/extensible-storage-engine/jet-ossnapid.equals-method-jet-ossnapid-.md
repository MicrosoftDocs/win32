---
description: "Learn more about: JET_OSSNAPID.Equals method (JET_OSSNAPID)"
title: JET_OSSNAPID.Equals method (JET_OSSNAPID)
TOCTitle: Equals method (JET_OSSNAPID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_OSSNAPID.Equals(Microsoft.Isam.Esent.Interop.JET_OSSNAPID)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_ossnapid.equals(v=EXCHG.10)
ms:contentKeyID: 39516381
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_OSSNAPID.Equals
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_OSSNAPID.Equals method (JET_OSSNAPID)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_OSSNAPID _
) As Boolean
'Usage
Dim instance As JET_OSSNAPID
Dim other As JET_OSSNAPID
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_OSSNAPID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_OSSNAPID](./jet-ossnapid-structure.md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](/dotnet/api/system.iequatable-1.equals#System_IEquatable_1_Equals__0_)  

## See also

#### Reference

[JET_OSSNAPID structure](./jet-ossnapid-structure.md)

[JET_OSSNAPID members](./jet-ossnapid-members.md)

[Equals overload](./jet-ossnapid.equals-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
