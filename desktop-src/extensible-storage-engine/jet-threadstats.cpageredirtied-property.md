---
description: "Learn more about: JET_THREADSTATS.cPageRedirtied property"
title: JET_THREADSTATS.cPageRedirtied property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'cPageRedirtied property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPageRedirtied
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_threadstats.cpageredirtied(v=EXCHG.10)
ms:contentKeyID: 39515312
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPageRedirtied
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.cPageRedirtied
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.get_cPageRedirtied
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.set_cPageRedirtied
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_THREADSTATS.cPageRedirtied property

Gets the total number of database pages, with unwritten changes, that have been modified by the database engine on the current thread.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cPageRedirtied As Integer
    Get
    Friend Set
'Usage
Dim instance As JET_THREADSTATS
Dim value As Integer

value = instance.cPageRedirtied
```

``` csharp
public int cPageRedirtied { get; internal set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_THREADSTATS structure](./jet-threadstats-structure2.md)

[JET_THREADSTATS members](./jet-threadstats-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
