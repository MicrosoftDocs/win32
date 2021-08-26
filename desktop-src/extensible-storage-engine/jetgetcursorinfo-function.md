---
description: "Learn more about: JetGetCursorInfo Function"
title: JetGetCursorInfo Function
TOCTitle: JetGetCursorInfo Function
ms:assetid: e779fa5d-1d7e-46f1-80c9-f7c819279188
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294126(v=EXCHG.10)
ms:contentKeyID: 32765740
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetCursorInfo
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

# JetGetCursorInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetCursorInfo Function

The **JetGetCursorInfo** function is used to determine whether an update of the current record of a cursor will result in a write conflict, based on the current update status of the record. It is possible that a write conflict will ultimately be returned even if **JetGetCursorInfo** returns JET_errSuccess, because another session may update the record before the current session is able to update the same record.

```cpp
    JET_ERR JET_API JetGetCursorInfo(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out         void* pvResult,
      __in          unsigned long cbMax,
      __in          unsigned long InfoLevel
    );
```

### Parameters

*sesid*

The session that will be used for this call.

*tableid*

The cursor that will be used for this call.

*pvResult*

Reserved for future use.

*cbMax*

Must be set to 0 (zero), otherwise unused. It is present for future functionality.

*InfoLevel*

Must be set to 0 (zero), otherwise unused. It is present for future functionality.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidParameter</p> | <p>Either <em>cbMax</em> is not 0 (zero) or <em>InfoLevel</em> is not 0 (zero).</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>The cursor is not currently on a record and information on a logical record cannot be returned as a result.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errWriteConflict</p> | <p>The current record of the cursor has been updated by another session and an update of this record by this session will result in a write conflict.</p> | 



On success, this operation has no effect on the location of the cursor but only indicates that no other session has currently updated this record.

On failure, if a negative error code is returned there are no effects to the cursor or the database.

#### Remarks

This operation does not affect the state of the cursor or the data. It only returns an error code describing whether an update to the current record by the calling session is known to result in a JET_errWriteConflict, or is unknown to return JET_errWriteConflict. If another session has already updated this record to use it is certain that an update of this record by this session will result in a write conflict. This will be true until this session commits or rolls back its transactions to transaction level 0 (zero). However, if **JetGetCursorInfo** returns JET_errSuccess, it is still possible for another session to update this record before the current session and thus it is still possible that an update of the current record by this session in its current transaction will result in a write conflict.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetGetLock](./jetgetlock-function.md)  
[JetPrepareUpdate](./jetprepareupdate-function.md)  
[JetStopService](./jetstopservice-function.md)  
[JetUpdate](./jetupdate-function.md)
