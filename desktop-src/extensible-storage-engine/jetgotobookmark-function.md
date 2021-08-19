---
description: "Learn more about: JetGotoBookmark Function"
title: JetGotoBookmark Function
TOCTitle: JetGotoBookmark Function
ms:assetid: a9a0aa43-834a-4eec-b47f-8e74d35aa972
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294053(v=EXCHG.10)
ms:contentKeyID: 32765656
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGotoBookmark
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

# JetGotoBookmark Function


_**Applies to:** Windows | Windows Server_

## JetGotoBookmark Function

The **JetGotoBookmark** function positions a cursor to an index entry for the record that is associated with the specified bookmark. The bookmark can be used with any index defined over a table. The bookmark for a record can be retrieved using [JetGetBookmark](./jetgetbookmark-function.md).

```cpp
    JET_ERR JET_API JetGotoBookmark(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          void* pvBookmark,
      __in          unsigned long cbBookmark
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*pvBookmark*

The buffer that contains the bookmark to use to position the cursor.

*cbBookmark*

The size of the bookmark in the buffer.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>The operation cannot complete because the instance that is associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p><strong>Windows XP:</strong>   This return value was introduced in Windows XP.</p> | 
| <p>JET_errInvalidBookmark</p> | <p>The bookmark that was provided is invalid. This might have occurred because the size of the bookmark is zero or the bookmark buffer pointer is <strong>NULL</strong>.</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>The cursor is on a secondary index and no index entry could be found for the record that is associated with the bookmark.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance that is associated with the session has not been initialized yet.</p> | 
| <p>JET_errRecordDeleted</p> | <p>The record that is associated with the bookmark could not be found.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>The operation cannot complete because a restore operation is in progress on the instance that is associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p><strong>Windows XP:</strong>   This return value was introduced in Windows XP.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance associated with the session is being shut down.</p> | 



If this function succeeds, the cursor will be positioned at an index entry for the record that is associated with the specified bookmark. If a record has been prepared for update, that update will be canceled. If an index range is in effect, that index range will be canceled. If a search key has been constructed for the cursor, that search key will be deleted. No change to the database state will occur.

If this function fails, the position of the cursor will remain unchanged. If a record has been prepared for update, that update will be canceled. If an index range is in effect, that index range will be canceled. If a search key has been constructed for the cursor, that search key will be deleted. No change to the database state will occur.

#### Remarks

There are two ways to use a bookmark to position a cursor on an index. The first is to use the bookmark to position on the record directly. This occurs when the current index of the cursor is the primary index. This technique works because an ESENT bookmark is the same as the associated record's primary key.

The second way to use a bookmark is to position it on an entry in a secondary index that corresponds to the record that is associated with that bookmark. During this process, the engine looks up the actual record using the bookmark on the primary index. It then uses the record data and the secondary index definition to compute a key into the secondary index that points to the record. It then positions the cursor on the index entry for that key. If the cursor is currently on a secondary index over one or more multi-valued key columns, the cursor will be positioned on the index entry corresponding to the first multi-value of each of those key columns.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetGetBookmark](./jetgetbookmark-function.md)
