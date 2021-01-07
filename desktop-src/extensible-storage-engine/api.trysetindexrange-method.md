---
description: "Learn more about: Api.TrySetIndexRange method"
title: Api.TrySetIndexRange method 
TOCTitle: 'TrySetIndexRange method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.TrySetIndexRange(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,Microsoft.Isam.Esent.Interop.SetIndexRangeGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.trysetindexrange(v=EXCHG.10)
ms:contentKeyID: 55100893
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.TrySetIndexRange
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.TrySetIndexRange
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.TrySetIndexRange method

Temporarily limits the set of index entries that the cursor can walk using JetMove to those starting from the current index entry and ending at the index entry that matches the search criteria specified by the search key in that cursor and the specified bound criteria. A search key must have been previously constructed using JetMakeKey. Returns true if the index range is non-empty, false otherwise.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function TrySetIndexRange ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    grbit As SetIndexRangeGrbit _
) As Boolean
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim grbit As SetIndexRangeGrbit
Dim returnValue As Boolean

returnValue = Api.TrySetIndexRange(sesid, _
    tableid, grbit)
```

``` csharp
public static bool TrySetIndexRange(
    JET_SESID sesid,
    JET_TABLEID tableid,
    SetIndexRangeGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The cursor to position.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.SetIndexRangeGrbit](./setindexrangegrbit-enumeration.md)  
    
    Seek option.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the seek was successful.  

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
