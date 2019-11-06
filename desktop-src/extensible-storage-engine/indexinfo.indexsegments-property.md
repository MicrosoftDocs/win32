---
title: IndexInfo.IndexSegments property 
TOCTitle: 'IndexSegments property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.IndexInfo.IndexSegments
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.indexinfo.indexsegments(v=EXCHG.10)
ms:contentKeyID: 55103239
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.IndexInfo.IndexSegments
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.IndexInfo.IndexSegments
- Microsoft.Isam.Esent.Interop.IndexInfo.get_IndexSegments
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IndexInfo.IndexSegments property

Gets the segments of the index.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public ReadOnly Property IndexSegments As IList(Of IndexSegment)
    Get
'Usage
Dim instance As IndexInfo
Dim value As IList(Of IndexSegment)

value = instance.IndexSegments
```

``` csharp
public IList<IndexSegment> IndexSegments { get; }
```

#### Property value

Type: [System.Collections.Generic.IList](https://docs.microsoft.com/dotnet/api/system.collections.generic.ilist-1?redirectedfrom=MSDN)\<[IndexSegment](dn350912\(v=exchg.10\).md)\>  

## See also

#### Reference

[IndexInfo class](dn350919\(v=exchg.10\).md)

[IndexInfo members](dn350916\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

