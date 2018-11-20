---
title: JET_COLUMNID.CompareTo method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'CompareTo method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_COLUMNID.CompareTo(Microsoft.Isam.Esent.Interop.JET_COLUMNID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columnid.compareto(v=EXCHG.10)
ms:contentKeyID: 39509744
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_COLUMNID.CompareTo
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNID.CompareTo
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_COLUMNID.CompareTo method

Compares this columnid to another columnid and determines whether this instance is before, the same as or after the other instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function CompareTo ( _
    other As JET_COLUMNID _
) As Integer
'Usage
Dim instance As JET_COLUMNID
Dim other As JET_COLUMNID
Dim returnValue As Integer

returnValue = instance.CompareTo(other)
```

``` csharp
public int CompareTo(
    JET_COLUMNID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET\_COLUMNID](hh564510\(v=exchg.10\).md)  
    
    The columnid to compare to the current instance.

#### Return value

Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
A signed number indicating the relative positions of this instance and the value parameter.  

#### Implements

[IComparable\<T\>.CompareTo(T)](http://msdn2.microsoft.com/en-us/library/43hc6wht)  

## See also

#### Reference

[JET\_COLUMNID structure](hh564510\(v=exchg.10\).md)

[JET\_COLUMNID members](hh558343\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

