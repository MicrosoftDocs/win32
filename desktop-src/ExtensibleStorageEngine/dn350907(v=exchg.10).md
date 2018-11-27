---
title: IndexInfo.Entries property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Entries property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.IndexInfo.Entries
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.indexinfo.entries(v=EXCHG.10)
ms:contentKeyID: 55103234
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.IndexInfo.Entries
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.IndexInfo.get_Entries
- Microsoft.Isam.Esent.Interop.IndexInfo.Entries
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IndexInfo.Entries property

Gets the number of entries in the index. This value is not current and is only is updated by Api.JetComputeStats.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public ReadOnly Property Entries As Integer
    Get
'Usage
Dim instance As IndexInfo
Dim value As Integer

value = instance.Entries
```

``` csharp
public int Entries { get; }
```

#### Property value

Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  

## See also

#### Reference

[IndexInfo class](dn350919\(v=exchg.10\).md)

[IndexInfo members](dn350916\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

