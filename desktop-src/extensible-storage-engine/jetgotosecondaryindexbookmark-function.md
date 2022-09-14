---
description: "Learn more about: JetGotoSecondaryIndexBookmark Function"
title: JetGotoSecondaryIndexBookmark Function
TOCTitle: JetGotoSecondaryIndexBookmark Function
ms:assetid: 06983b1e-503a-469b-9be5-b37e7551de67
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269180(v=EXCHG.10)
ms:contentKeyID: 32765483
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGotoSecondaryIndexBookmark
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

# JetGotoSecondaryIndexBookmark Function


_**Applies to:** Windows | Windows Server_

## JetGotoSecondaryIndexBookmark Function

The **JetGotoSecondaryIndexBookmark** function positions a cursor to an index entry that is associated with the specified secondary index bookmark. The secondary index bookmark must be used with the same index over the same table from which it was originally retrieved. The secondary index bookmark for an index entry can be retrieved using **JetGotoSecondaryIndexBookmark**.

**Windows XP:**  **JetGotoSecondaryIndexBookmark** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetGotoSecondaryIndexBookmark(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          void* pvSecondaryKey,
      __in          unsigned long cbSecondaryKey,
      __in_opt      void* pvPrimaryBookmark,
      __in          unsigned long cbPrimaryBookmark,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*pvSecondaryKey*

The buffer that contains the secondary key to use to position the cursor.

*cbSecondaryKey*

The size of the secondary key in the buffer.

*pvPrimaryBookmark*

The buffer that contains the primary key bookmark to use to position the cursor.

*cbPrimaryBookmark*

The size of the primary key bookmark in the buffer.

*grbit*

A group of bits that specifies zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitBookmarkPermitVirtualCurrency</p> | <p>In the event that the index entry can no longer be found, the cursor will be left positioned where that index entry was previously found. The operation will still fail with JET_errRecordDeleted; however, it will be possible to move to the next or previous index entry relative to the index entry that is now missing.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>The operation cannot complete because is because the instance that is associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 
| <p>JET_errInvalidBookmark</p> | <p>The secondary index bookmark that was provided was invalid. This error might have occurred because the secondary key is zero or the secondary key buffer pointer is <strong>NULL</strong>. This error occurs because</p><ul><li><p>The current secondary index does not have a uniqueness constraint and the size of the provided bookmark is zero.</p></li><li><p>The bookmark buffer pointer is <strong>NULL</strong>.</p></li></ul> | 
| <p>JET_errNoCurrentIndex</p> | <p>The cursor is not currently on a secondary index. It is not meaningful to go to a secondary index bookmark when the cursor is not currently using a secondary index. <a href="gg294053(v=exchg.10).md">JetGotoBookmark</a> should be used when the cursor is not on a secondary index.</p> | 
| <p>JET_errNotInitialized</p> | <p>The operation cannot complete because the instance that is associated with the session has not yet been initialized.</p> | 
| <p>JET_errRecordDeleted</p> | <p>The index entry that is associated with the secondary index bookmark could not be found.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>The operation cannot complete because a restore operation is in progress on the instance that is associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance that is associated with the session is being shut down.</p> | 



If this function succeeds, the cursor will be positioned at an index entry that is associated with the specified secondary index bookmark. If a record has been prepared for update, that update will be canceled. If an index range is in effect, that index range will be canceled. If a search key has been constructed for the cursor to use, that search key will be deleted. No change to the database state will occur.

If this function fails, the position of the cursor remains unchanged unless JET_errRecordDeleted is returned and JET_bitBookmarkPermitVirtualCurrency is specified. In that case, the cursor will be positioned where the index entry that is associated with the specified secondary index bookmark would have been. The cursor can be moved relative to that position, but is still not on a valid index entry.

If a record has been prepared for update, that update will be canceled. If an index range is in effect, that index range will be canceled. If a search key has been constructed for the cursor to use, that search key will be deleted. In any case, no change to the database state will occur.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetGetSecondaryIndexBookmark](./jetgetsecondaryindexbookmark-function.md)  
[JetGotoBookmark](./jetgotobookmark-function.md)  
[JetStopService](./jetstopservice-function.md)
