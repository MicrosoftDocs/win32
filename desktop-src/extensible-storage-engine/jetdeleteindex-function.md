---
description: "Learn more about: JetDeleteIndex Function"
title: JetDeleteIndex Function
TOCTitle: JetDeleteIndex Function
ms:assetid: c540503b-d5a6-47f2-9113-9650891c4b6d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294081(v=EXCHG.10)
ms:contentKeyID: 32765696
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetDeleteIndexW
- JetDeleteIndexA
- JetDeleteIndex
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetDeleteIndex Function


_**Applies to:** Windows | Windows Server_

## JetDeleteIndex Function

The **JetDeleteIndex** function deletes an index from a table.

```cpp
    JET_ERR JET_API JetDeleteIndex(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          JET_PCSTR szIndexName
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*tableid*

The table that contains the column that is to be deleted.

*szIndexName*

The name of the index to be deleted.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errFixedDDL</p> | <p>An attempt was made to delete an index from a fixed table (for example, one created with JET_bitTableCreateFixedDDL).</p> | 
| <p>JET_errFixedInheritedDDL</p> | <p>An attempt was made to delete an index from a template table. A template table has fixed DDL.</p> | 
| <p>JET_errIndexNotFound</p> | <p>The index named in <em>szIndexName</em> was not found.</p> | 
| <p>JET_errPermissionDenied</p> | <p>The table cannot be updated because it was opened read-only.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>Multiple threads attempted to use the same database session.</p> | 
| <p>JET_errTransReadOnly</p> | <p>The transaction was opened as a read-only transaction.</p> | 



#### Remarks

When successful, the index is deleted and therefore cannot be used subsequently. There must not be any active transaction using the index.

On success, the currency is set before the first record.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetDeleteIndexW</strong> (Unicode) and <strong>JetDeleteIndexA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetCreateIndex](./jetcreateindex-function.md)  
[JetCreateIndex2](./jetcreateindex2-function.md)
