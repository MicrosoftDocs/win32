---
description: "Learn more about: JET_THREADSTATS.Create method"
title: JET_THREADSTATS.Create method  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'Create method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.Create(System.Int32,System.Int32,System.Int32,System.Int32,System.Int32,System.Int32,System.Int32)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_threadstats.create(v=EXCHG.10)
ms:contentKeyID: 39509886
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.Create
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.Create
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_THREADSTATS.Create method

Create a new [JET_THREADSTATS](./jet-threadstats-structure2.md) struct with the specified valued.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function Create ( _
    cPageReferenced As Integer, _
    cPageRead As Integer, _
    cPagePreread As Integer, _
    cPageDirtied As Integer, _
    cPageRedirtied As Integer, _
    cLogRecord As Integer, _
    cbLogRecord As Integer _
) As JET_THREADSTATS
'Usage
Dim cPageReferenced As Integer
Dim cPageRead As Integer
Dim cPagePreread As Integer
Dim cPageDirtied As Integer
Dim cPageRedirtied As Integer
Dim cLogRecord As Integer
Dim cbLogRecord As Integer
Dim returnValue As JET_THREADSTATS

returnValue = JET_THREADSTATS.Create(cPageReferenced, _
    cPageRead, cPagePreread, cPageDirtied, _
    cPageRedirtied, cLogRecord, cbLogRecord)
```

``` csharp
public static JET_THREADSTATS Create(
    int cPageReferenced,
    int cPageRead,
    int cPagePreread,
    int cPageDirtied,
    int cPageRedirtied,
    int cLogRecord,
    int cbLogRecord
)
```

#### Parameters

  - cPageReferenced  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Number of pages visited.

<!-- end list -->

  - cPageRead  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Number of pages read.

<!-- end list -->

  - cPagePreread  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Number of pages preread.

<!-- end list -->

  - cPageDirtied  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    TNumber of pages dirtied.

<!-- end list -->

  - cPageRedirtied  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Number of pages redirtied.

<!-- end list -->

  - cLogRecord  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Number of log records generated.

<!-- end list -->

  - cbLogRecord  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Bytes of log records written.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS](./jet-threadstats-structure2.md)  
A new [JET_THREADSTATS](./jet-threadstats-structure2.md) struct with the specified values.  

## See also

#### Reference

[JET_THREADSTATS structure](./jet-threadstats-structure2.md)

[JET_THREADSTATS members](./jet-threadstats-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
