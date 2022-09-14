---
description: "Learn more about: JetDupCursor Function"
title: JetDupCursor Function
TOCTitle: JetDupCursor Function
ms:assetid: 154b7d2d-4656-46b3-873c-2e194a9059b4
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269193(v=EXCHG.10)
ms:contentKeyID: 32765496
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetDupCursor
topic_type: 
- kbArticle
- apiref
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetDupCursor Function


_**Applies to:** Windows | Windows Server_

## JetDupCursor Function

The **JetDupCursor** function duplicates an open cursor and returns a handle to the duplicated cursor. If the cursor that was duplicated was a read-only cursor then the duplicated cursor is also a read-only cursor. Any state related to constructing a search key or updating a record is not copied into the duplicated cursor. In addition, the location of the original cursor is not duplicated into the duplicated cursor. The duplicated cursor is always opened on the clustered index and its location is always on the first row of the table.

```cpp
    JET_ERR JET_API JetDupCursor(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out         JET_TABLEID* ptableid,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*ptableid*

Pointer to *tableid*.

*grbit*

Reserved for future use.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errOutOfCursors</p> | <p>No available cursor resources exist.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, *ptableid* is set to a duplicated cursor.

On failure, no changes are made. The state of *tableid* is unchanged.

#### Remarks

The duplicated cursor does not have the entire cursor state copied. The location of the duplicated cursor, including the current index, is usually different from the given cursor. The duplicated cursor is always returned on the clustered index and on the first row in the table. If the table is empty, the duplicated cursor is not on any row.

Tables opened with **JetDupCursor** should usually be closed with [JetCloseTable](./jetclosetable-function.md). The exception to this rule happens when **JetDupCursor** is called in a transaction and the transaction is rolled back (with [JetRollback](./jetrollback-function.md)). When rolling back a transaction, the cursor is automatically closed. In this case, it is an error to close the table with [JetCloseTable](./jetclosetable-function.md).

The number of tables that can be opened simultaneously is affected directly by [JET_paramMaxOpenTables](./resource-parameters.md). See [System Parameters](./extensible-storage-engine-system-parameters.md) for details.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetStopService](./jetstopservice-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
