---
title: JET_THREADSTATS.cPagePreread property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'cPagePreread property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPagePreread
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.jet_threadstats.cpagepreread(v=EXCHG.10)
ms:contentKeyID: 39510638
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPagePreread
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.get_cPagePreread
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPagePreread
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.set_cPagePreread
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_THREADSTATS.cPagePreread property

Gets the total number of database pages prefetched from disk by the database engine on the current thread.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cPagePreread As Integer
    Get
    Friend Set
'Usage
Dim instance As JET_THREADSTATS
Dim value As Integer

value = instance.cPagePreread
```

``` csharp
public int cPagePreread { get; internal set; }
```

#### Property value

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  

## See also

#### Reference

[JET_THREADSTATS structure](hh578565\(v=exchg.10\).md)

[JET_THREADSTATS members](hh579250\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

