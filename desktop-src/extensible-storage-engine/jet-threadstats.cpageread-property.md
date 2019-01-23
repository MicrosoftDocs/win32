---
title: JET_THREADSTATS.cPageRead property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'cPageRead property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPageRead
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.jet_threadstats.cpageread(v=EXCHG.10)
ms:contentKeyID: 39516296
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPageRead
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.get_cPageRead
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPageRead
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.set_cPageRead
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_THREADSTATS.cPageRead property

Gets the total number of database pages fetched from disk by the database engine on the current thread.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cPageRead As Integer
    Get
    Friend Set
'Usage
Dim instance As JET_THREADSTATS
Dim value As Integer

value = instance.cPageRead
```

``` csharp
public int cPageRead { get; internal set; }
```

#### Property value

Type: [System.Int32](https://msdn.microsoft.com/en-us/library/td2s409d)  

## See also

#### Reference

[JET_THREADSTATS structure](hh578565\(v=exchg.10\).md)

[JET_THREADSTATS members](hh579250\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

