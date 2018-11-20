---
title: JET_TABLEID.Equals method (JET_TABLEID) (Microsoft.Isam.Esent.Interop)
TOCTitle: Equals method (JET_TABLEID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_TABLEID.Equals(Microsoft.Isam.Esent.Interop.JET_TABLEID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_tableid.equals(v=EXCHG.10)
ms:contentKeyID: 39514708
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_TABLEID.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_TABLEID.Equals method (JET\_TABLEID)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_TABLEID _
) As Boolean
'Usage
Dim instance As JET_TABLEID
Dim other As JET_TABLEID
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_TABLEID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET\_TABLEID](hh566310\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](http://msdn2.microsoft.com/en-us/library/ms131190)  

## See also

#### Reference

[JET\_TABLEID structure](hh566310\(v=exchg.10\).md)

[JET\_TABLEID members](hh596310\(v=exchg.10\).md)

[Equals overload](hh577437\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

