---
title: JET_INDEXRANGE.ContentEquals method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'ContentEquals method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_INDEXRANGE.ContentEquals(Microsoft.Isam.Esent.Interop.JET_INDEXRANGE)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_indexrange.contentequals(v=EXCHG.10)
ms:contentKeyID: 55103676
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXRANGE.ContentEquals
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXRANGE.ContentEquals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_INDEXRANGE.ContentEquals method

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function ContentEquals ( _
    other As JET_INDEXRANGE _
) As Boolean
'Usage
Dim instance As JET_INDEXRANGE
Dim other As JET_INDEXRANGE
Dim returnValue As Boolean

returnValue = instance.ContentEquals(other)
```

``` csharp
public bool ContentEquals(
    JET_INDEXRANGE other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET\_INDEXRANGE](dn335175\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are equal.  

#### Implements

[IContentEquatable\<T\>.ContentEquals(T)](hh538970\(v=exchg.10\).md)  

## See also

#### Reference

[JET\_INDEXRANGE class](dn335175\(v=exchg.10\).md)

[JET\_INDEXRANGE members](dn335176\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

