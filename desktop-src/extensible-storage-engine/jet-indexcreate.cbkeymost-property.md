---
title: JET_INDEXCREATE.cbKeyMost property 
TOCTitle: 'cbKeyMost property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.cbKeyMost
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexcreate.cbkeymost(v=EXCHG.10)
ms:contentKeyID: 55103646
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.cbKeyMost
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.cbKeyMost
- Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.get_cbKeyMost
- Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.set_cbKeyMost
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXCREATE.cbKeyMost property

Gets or sets the maximum allowable size, in bytes, for keys in the index. The minimum supported maximum key size is JET_cbKeyMostMin (255) which is the legacy maximum key size. The maximum key size is dependent on the database page size [DatabasePageSize](hh596135\(v=exchg.10\).md). The maximum key size can be retrieved with [KeyMost](dn351156\(v=exchg.10\).md). This parameter is ignored on Windows XP and Windows Server 2003. Unlike the unmanaged API, **IndexKeyMost()** (JET_bitIndexKeyMost) is not needed, it will be added automatically.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cbKeyMost As Integer
    Get
    Set
'Usage
Dim instance As JET_INDEXCREATE
Dim value As Integer

value = instance.cbKeyMost

instance.cbKeyMost = value
```

``` csharp
public int cbKeyMost { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_INDEXCREATE class](dn335112\(v=exchg.10\).md)

[JET_INDEXCREATE members](dn335151\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)