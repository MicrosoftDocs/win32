---
description: "Learn more about: JET_LOGTIME.Equals method (JET_LOGTIME)"
title: JET_LOGTIME.Equals method (JET_LOGTIME)
TOCTitle: Equals method (JET_LOGTIME)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_LOGTIME.Equals(Microsoft.Isam.Esent.Interop.JET_LOGTIME)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_logtime.equals(v=EXCHG.10)
ms:contentKeyID: 39512684
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_LOGTIME.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_LOGTIME.Equals method (JET_LOGTIME)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_LOGTIME _
) As Boolean
'Usage
Dim instance As JET_LOGTIME
Dim other As JET_LOGTIME
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_LOGTIME other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_LOGTIME](./jet-logtime-structure2.md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](/dotnet/api/system.iequatable-1.equals#System_IEquatable_1_Equals__0_)  

## See also

#### Reference

[JET_LOGTIME structure](./jet-logtime-structure2.md)

[JET_LOGTIME members](./jet-logtime-members.md)

[Equals overload](./jet-logtime.equals-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
