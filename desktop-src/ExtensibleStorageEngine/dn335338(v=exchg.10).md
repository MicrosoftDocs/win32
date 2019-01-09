---
title: JET_ERRINFOBASIC.ContentEquals method  (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: 'ContentEquals method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Windows8.JET_ERRINFOBASIC.ContentEquals(Microsoft.Isam.Esent.Interop.Windows8.JET_ERRINFOBASIC)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.windows8.jet_errinfobasic.contentequals(v=EXCHG.10)
ms:contentKeyID: 55104306
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRINFOBASIC.ContentEquals
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRINFOBASIC.ContentEquals
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_ERRINFOBASIC.ContentEquals method

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows8](dn335439\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function ContentEquals ( _
    other As JET_ERRINFOBASIC _
) As Boolean
'Usage
Dim instance As JET_ERRINFOBASIC
Dim other As JET_ERRINFOBASIC
Dim returnValue As Boolean

returnValue = instance.ContentEquals(other)
```

``` csharp
public bool ContentEquals(
    JET_ERRINFOBASIC other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET_ERRINFOBASIC](dn335334\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](https://msdn.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are equal.  

#### Implements

[IContentEquatable\<T\>.ContentEquals(T)](hh538970\(v=exchg.10\).md)  

## See also

#### Reference

[JET_ERRINFOBASIC class](dn335334\(v=exchg.10\).md)

[JET_ERRINFOBASIC members](dn335336\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Windows8 namespace](dn335439\(v=exchg.10\).md)

