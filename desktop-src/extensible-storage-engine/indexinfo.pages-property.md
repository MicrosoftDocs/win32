---
title: IndexInfo.Pages property 
TOCTitle: 'Pages property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.IndexInfo.Pages
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.indexinfo.pages(v=EXCHG.10)
ms:contentKeyID: 55103266
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.IndexInfo.Pages
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.IndexInfo.Pages
- Microsoft.Isam.Esent.Interop.IndexInfo.get_Pages
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IndexInfo.Pages property

Gets the number of pages in the index. This value is not current and is only is updated by Api.JetComputeStats.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public ReadOnly Property Pages As Integer
    Get
'Usage
Dim instance As IndexInfo
Dim value As Integer

value = instance.Pages
```

``` csharp
public int Pages { get; }
```

#### Property value

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  

## See also

#### Reference

[IndexInfo class](dn350919\(v=exchg.10\).md)

[IndexInfo members](dn350916\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

