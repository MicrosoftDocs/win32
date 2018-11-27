---
title: Api.JetMove method (JET_SESID, JET_TABLEID, JET_Move, MoveGrbit) (Microsoft.Isam.Esent.Interop)
TOCTitle: JetMove method (JET_SESID, JET_TABLEID, JET_Move, MoveGrbit)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetMove(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,Microsoft.Isam.Esent.Interop.JET_Move,Microsoft.Isam.Esent.Interop.MoveGrbit)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetmove(v=EXCHG.10)
ms:contentKeyID: 55100766
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetMove
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetMove method (JET\_SESID, JET\_TABLEID, JET\_Move, MoveGrbit)

Navigate through an index. The cursor can be positioned at the start or end of the index and moved backwards and forwards by a specified number of index entries. Also see [TryMoveFirst(JET\_SESID, JET\_TABLEID)](dn334150\(v=exchg.10\).md), [TryMoveLast(JET\_SESID, JET\_TABLEID)](dn334140\(v=exchg.10\).md), [TryMoveNext(JET\_SESID, JET\_TABLEID)](dn334095\(v=exchg.10\).md), [TryMovePrevious(JET\_SESID, JET\_TABLEID)](dn334144\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetMove ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    numRows As JET_Move, _
    grbit As MoveGrbit _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim numRows As JET_Move
Dim grbit As MoveGrbitApi.JetMove(sesid, tableid, numRows, _
    grbit)
```

``` csharp
public static void JetMove(
    JET_SESID sesid,
    JET_TABLEID tableid,
    JET_Move numRows,
    MoveGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use for the call.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_TABLEID](hh566310\(v=exchg.10\).md)  
    
    The cursor to position.

<!-- end list -->

  - numRows  
    Type: [Microsoft.Isam.Esent.Interop.JET\_Move](hh558184\(v=exchg.10\).md)  
    
    An offset which indicates how far to move the cursor.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.MoveGrbit](hh558238\(v=exchg.10\).md)  
    
    Move options.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[JetMove overload](dn292215\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

