---
title: JET_LGPOS.CompareTo method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'CompareTo method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_LGPOS.CompareTo(Microsoft.Isam.Esent.Interop.JET_LGPOS)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_lgpos.compareto(v=EXCHG.10)
ms:contentKeyID: 39514516
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_LGPOS.CompareTo
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_LGPOS.CompareTo
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_LGPOS.CompareTo method

Compares this log position to another log position and determines whether this instance is before, the same as or after the other instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function CompareTo ( _
    other As JET_LGPOS _
) As Integer
'Usage
Dim instance As JET_LGPOS
Dim other As JET_LGPOS
Dim returnValue As Integer

returnValue = instance.CompareTo(other)
```

``` csharp
public int CompareTo(
    JET_LGPOS other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET\_LGPOS](hh578063\(v=exchg.10\).md)  
    
    The log position to compare to the current instance.

#### Return value

Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
A signed number indicating the relative positions of this instance and the value parameter.  

#### Implements

[IComparable\<T\>.CompareTo(T)](http://msdn2.microsoft.com/en-us/library/43hc6wht)  

## See also

#### Reference

[JET\_LGPOS structure](hh578063\(v=exchg.10\).md)

[JET\_LGPOS members](hh566576\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

