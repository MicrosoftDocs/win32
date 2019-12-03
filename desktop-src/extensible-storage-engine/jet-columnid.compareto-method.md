---
title: JET_COLUMNID.CompareTo method 
TOCTitle: 'CompareTo method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_COLUMNID.CompareTo(Microsoft.Isam.Esent.Interop.JET_COLUMNID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columnid.compareto(v=EXCHG.10)
ms:contentKeyID: 39509744
ms.date: 07/30/2014
ms.topic: reference
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

# JET_COLUMNID.CompareTo method

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
    Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](hh564510\(v=exchg.10\).md)  
    
    The columnid to compare to the current instance.

#### Return value

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  
A signed number indicating the relative positions of this instance and the value parameter.  

#### Implements

[IComparable\<T\>.CompareTo(T)](https://docs.microsoft.com/dotnet/api/system.icomparable-1.compareto?redirectedfrom=MSDN#System_IComparable_1_CompareTo__0_)  

## See also

#### Reference

[JET_COLUMNID structure](hh564510\(v=exchg.10\).md)

[JET_COLUMNID members](hh558343\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

