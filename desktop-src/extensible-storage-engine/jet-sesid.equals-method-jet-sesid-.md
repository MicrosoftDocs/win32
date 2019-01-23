---
title: JET_SESID.Equals method (JET_SESID) (Microsoft.Isam.Esent.Interop)
TOCTitle: Equals method (JET_SESID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_SESID.Equals(Microsoft.Isam.Esent.Interop.JET_SESID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_sesid.equals(v=EXCHG.10)
ms:contentKeyID: 39511762
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_SESID.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_SESID.Equals method (JET_SESID)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_SESID _
) As Boolean
'Usage
Dim instance As JET_SESID
Dim other As JET_SESID
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_SESID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](https://msdn.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](https://msdn.microsoft.com/en-us/library/ms131190)  

## See also

#### Reference

[JET_SESID structure](hh596745\(v=exchg.10\).md)

[JET_SESID members](hh557719\(v=exchg.10\).md)

[Equals overload](hh564734\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

