---
title: JET_COMMIT_ID.CompareTo method  (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: 'CompareTo method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.CompareTo(Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.windows8.jet_commit_id.compareto(v=EXCHG.10)
ms:contentKeyID: 55104397
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.CompareTo
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.CompareTo
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COMMIT_ID.CompareTo method

Returns a value comparing this instance with another.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows8](dn335439\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function CompareTo ( _
    other As JET_COMMIT_ID _
) As Integer
'Usage
Dim instance As JET_COMMIT_ID
Dim other As JET_COMMIT_ID
Dim returnValue As Integer

returnValue = instance.CompareTo(other)
```

``` csharp
public int CompareTo(
    JET_COMMIT_ID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID](dn335448\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  
A signed value representing the relative positions of the instances.  

#### Implements

[IComparable\<T\>.CompareTo(T)](https://docs.microsoft.com/dotnet/api/system.icomparable-1.compareto?redirectedfrom=MSDN#System_IComparable_1_CompareTo__0_)  

## See also

#### Reference

[JET_COMMIT_ID class](dn335448\(v=exchg.10\).md)

[JET_COMMIT_ID members](dn335451\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Windows8 namespace](dn335439\(v=exchg.10\).md)

