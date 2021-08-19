---
description: "Learn more about: JetDeleteColumn Function"
title: JetDeleteColumn Function
TOCTitle: JetDeleteColumn Function
ms:assetid: b2f4be8c-7ea9-4f66-925b-4e9c14d9d475
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294062(v=EXCHG.10)
ms:contentKeyID: 32765677
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetDeleteColumnA
- JetDeleteColumnW
- JetDeleteColumn
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetDeleteColumn Function


_**Applies to:** Windows | Windows Server_

## JetDeleteColumn Function

The **JetDeleteColumn** function deletes a column from an ESE database table.

```cpp
JET_ERR JET_API JetDeleteColumn(
  __in          JET_SESID sesid,
  __in          JET_TABLEID tableid,
  __in          const tchar* szColumnName
);
```

### Parameters

*sesid*

The database session context to use for the API call.

*tableid*

The table from which to delete the column.

*szColumnName*

The name of the column to be deleted.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errColumnInUse</p> | <p>The column is currently in use. It may be currently used by an index.</p> | 
| <p>JET_errFixedDDL</p> | <p>An attempt was made to modify the fixed DDL.</p> | 
| <p>JET_errFixedInheritedDDL</p> | <p>The column named in <em>szColumnName</em> exists in the template table, and the DDL of a template table cannot be modified.</p> | 
| <p>JET_errInvalidName</p> | <p>This may be returned if a bad name for <em>szColumnName</em> was given.</p> | 
| <p>JET_errPermissionDenied</p> | <p>The table is not writable. This may get returned if the database was opened in read-only mode.</p> | 
| <p>JET_errTransReadOnly</p> | <p>The transaction is a read-only transaction.</p> | 



#### Remarks

Calling **JetDeleteColumn** is identical to calling [JetDeleteColumn2](./jetdeletecolumn2-function.md) with *grbit* set to zero (0).

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetDeleteColumnW</strong> (Unicode) and <strong>JetDeleteColumnA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetDeleteColumn2](./jetdeletecolumn2-function.md)
