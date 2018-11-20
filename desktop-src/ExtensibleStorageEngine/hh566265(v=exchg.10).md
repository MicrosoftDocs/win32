---
title: JET_COLUMNID.Equals method (JET_COLUMNID) (Microsoft.Isam.Esent.Interop)
TOCTitle: Equals method (JET_COLUMNID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_COLUMNID.Equals(Microsoft.Isam.Esent.Interop.JET_COLUMNID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columnid.equals(v=EXCHG.10)
ms:contentKeyID: 39516458
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNID.Equals
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_COLUMNID.Equals method (JET\_COLUMNID)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_COLUMNID _
) As Boolean
'Usage
Dim instance As JET_COLUMNID
Dim other As JET_COLUMNID
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_COLUMNID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET\_COLUMNID](hh564510\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](http://msdn2.microsoft.com/en-us/library/ms131190)  

## See also

#### Reference

[JET\_COLUMNID structure](hh564510\(v=exchg.10\).md)

[JET\_COLUMNID members](hh558343\(v=exchg.10\).md)

[Equals overload](hh579286\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

