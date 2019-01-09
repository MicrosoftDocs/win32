---
title: JET_DBINFOMISC.Equals method (JET_DBINFOMISC) (Microsoft.Isam.Esent.Interop)
TOCTitle: Equals method (JET_DBINFOMISC)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.Equals(Microsoft.Isam.Esent.Interop.JET_DBINFOMISC)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_dbinfomisc.equals(v=EXCHG.10)
ms:contentKeyID: 39514332
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.Equals
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.Equals method (JET_DBINFOMISC)

Indicates whether the current object is equal to another object of the same type.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_DBINFOMISC _
) As Boolean
'Usage
Dim instance As JET_DBINFOMISC
Dim other As JET_DBINFOMISC
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_DBINFOMISC other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBINFOMISC](hh538867\(v=exchg.10\).md)  
    
    An object to compare with this object.

#### Return value

Type: [System.Boolean](https://msdn.microsoft.com/en-us/library/a28wyd50)  
True if the current object is equal to the other parameter; otherwise, false.  

#### Implements

[IEquatable\<T\>.Equals(T)](https://msdn.microsoft.com/en-us/library/ms131190)  

## See also

#### Reference

[JET_DBINFOMISC class](hh538867\(v=exchg.10\).md)

[JET_DBINFOMISC members](hh566148\(v=exchg.10\).md)

[Equals overload](hh577631\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

