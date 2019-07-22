---
title: Api.GetTableIndexes method (JET_SESID, JET_TABLEID) (Microsoft.Isam.Esent.Interop)
TOCTitle: GetTableIndexes method (JET_SESID, JET_TABLEID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.GetTableIndexes(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.gettableindexes(v=EXCHG.10)
ms:contentKeyID: 55107219
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.GetTableIndexes
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.GetTableIndexes method (JET_SESID, JET_TABLEID)

Iterates over all the indexes in the table, returning information about each one.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function GetTableIndexes ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID _
) As IEnumerable(Of IndexInfo)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim returnValue As IEnumerable(Of IndexInfo)

returnValue = Api.GetTableIndexes(sesid, _
    tableid)
```

``` csharp
public static IEnumerable<IndexInfo> GetTableIndexes(
    JET_SESID sesid,
    JET_TABLEID tableid
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](hh566310\(v=exchg.10\).md)  
    
    The table to retrieve index information for.

#### Return value

Type: [System.Collections.Generic.IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1?redirectedfrom=MSDN)\<[IndexInfo](dn350919\(v=exchg.10\).md)\>  
An iterator over an IndexInfo for each index in the table.  

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[GetTableIndexes overload](dn292087\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

