---
description: "Learn more about: JET_RECSIZE.Equals method (JET_RECSIZE)"
title: JET_RECSIZE.Equals method (JET_RECSIZE) (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: Equals method (JET_RECSIZE)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.Equals(Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_recsize.equals(v=EXCHG.10)
ms:contentKeyID: 39511266
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RECSIZE.Equals method (JET_RECSIZE)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_RECSIZE _
) As Boolean
'Usage
Dim instance As JET_RECSIZE
Dim other As JET_RECSIZE
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_RECSIZE other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE](./jet-recsize-structure2.md)  
    
    An object to compare with this instance.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](/dotnet/api/system.iequatable-1.equals#System_IEquatable_1_Equals__0_)  

## See also

#### Reference

[JET_RECSIZE structure](./jet-recsize-structure2.md)

[JET_RECSIZE members](./jet-recsize-members.md)

[Equals overload](./jet-recsize.equals-method.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
