---
description: "Learn more about: Api.JetMove method (JET_SESID, JET_TABLEID, Int32, MoveGrbit)"
title: Api.JetMove method (JET_SESID, JET_TABLEID, Int32, MoveGrbit)
TOCTitle: JetMove method (JET_SESID, JET_TABLEID, Int32, MoveGrbit)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetMove(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.Int32,Microsoft.Isam.Esent.Interop.MoveGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetmove(v=EXCHG.10)
ms:contentKeyID: 55100765
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetMove
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetMove method (JET_SESID, JET_TABLEID, Int32, MoveGrbit)

Navigate through an index. The cursor can be positioned at the start or end of the index and moved backwards and forwards by a specified number of index entries. Also see [TryMoveFirst(JET_SESID, JET_TABLEID)](./api.trymovefirst-method.md), [TryMoveLast(JET_SESID, JET_TABLEID)](./api.trymovelast-method.md), [TryMoveNext(JET_SESID, JET_TABLEID)](./api.trymovenext-method.md), [TryMovePrevious(JET_SESID, JET_TABLEID)](./api.trymoveprevious-method.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetMove ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    numRows As Integer, _
    grbit As MoveGrbit _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim numRows As Integer
Dim grbit As MoveGrbitApi.JetMove(sesid, tableid, numRows, _
    grbit)
```

``` csharp
public static void JetMove(
    JET_SESID sesid,
    JET_TABLEID tableid,
    int numRows,
    MoveGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use for the call.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The cursor to position.

<!-- end list -->

  - numRows  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    An offset which indicates how far to move the cursor.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.MoveGrbit](./movegrbit-enumeration.md)  
    
    Move options.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[JetMove overload](./api.jetmove-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
