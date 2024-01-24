---
description: "Learn more about: JET_COMMIT_ID.Equals method (JET_COMMIT_ID)"
title: JET_COMMIT_ID.Equals method (JET_COMMIT_ID) (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: Equals method (JET_COMMIT_ID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.Equals(Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.windows8.jet_commit_id.equals(v=EXCHG.10)
ms:contentKeyID: 55104294
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.Equals
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COMMIT_ID.Equals method (JET_COMMIT_ID)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows8](./microsoft.isam.esent.interop.windows8-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_COMMIT_ID _
) As Boolean
'Usage
Dim instance As JET_COMMIT_ID
Dim other As JET_COMMIT_ID
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_COMMIT_ID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID](./jet-commit-id-class.md)  
    
    An object to compare with this instance.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
true if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](/dotnet/api/system.iequatable-1.equals#System_IEquatable_1_Equals__0_)  

## See also

#### Reference

[JET_COMMIT_ID class](./jet-commit-id-class.md)

[JET_COMMIT_ID members](./jet-commit-id-members.md)

[Equals overload](./jet-commit-id.equals-method.md)

[Microsoft.Isam.Esent.Interop.Windows8 namespace](./microsoft.isam.esent.interop.windows8-namespace.md)
