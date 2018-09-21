---
title: JET_COLUMNBASE.Equals method (JET_COLUMNBASE) (Microsoft.Isam.Esent.Interop)
TOCTitle: Equals method (JET_COLUMNBASE)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_COLUMNBASE.Equals(Microsoft.Isam.Esent.Interop.JET_COLUMNBASE)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columnbase.equals(v=EXCHG.10)
ms:contentKeyID: 55103355
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNBASE.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_COLUMNBASE.Equals method (JET\_COLUMNBASE)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_COLUMNBASE _
) As Boolean
'Usage
Dim instance As JET_COLUMNBASE
Dim other As JET_COLUMNBASE
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_COLUMNBASE other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET\_COLUMNBASE](dn335045\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](http://msdn2.microsoft.com/en-us/library/ms131190)  

## See also

#### Reference

[JET\_COLUMNBASE class](dn335045\(v=exchg.10\).md)

[JET\_COLUMNBASE members](dn335046\(v=exchg.10\).md)

[Equals overload](dn335059\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

