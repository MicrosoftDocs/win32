---
description: "Learn more about: JET_SNPROG.Equals method (JET_SNPROG)"
title: JET_SNPROG.Equals method (JET_SNPROG)
TOCTitle: Equals method (JET_SNPROG)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_SNPROG.Equals(Microsoft.Isam.Esent.Interop.JET_SNPROG)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_snprog.equals(v=EXCHG.10)
ms:contentKeyID: 55103954
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_SNPROG.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_SNPROG.Equals method (JET_SNPROG)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_SNPROG _
) As Boolean
'Usage
Dim instance As JET_SNPROG
Dim other As JET_SNPROG
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_SNPROG other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_SNPROG](./jet-snprog-class.md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](/dotnet/api/system.iequatable-1.equals#System_IEquatable_1_Equals__0_)  

## See also

#### Reference

[JET_SNPROG class](./jet-snprog-class.md)

[JET_SNPROG members](./jet-snprog-members.md)

[Equals overload](./jet-snprog.equals-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
