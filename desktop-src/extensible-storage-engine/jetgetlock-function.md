---
description: "Learn more about: JetGetLock Function"
title: JetGetLock Function
TOCTitle: JetGetLock Function
ms:assetid: cebf0789-3d31-4ae8-9b23-dcf5e34e98fc
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294094(v=EXCHG.10)
ms:contentKeyID: 32765709
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetLock
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetGetLock Function


_**Applies to:** Windows | Windows Server_

## JetGetLock Function

The **JetGetLock** function provides a means to explicitly reserve the ability to update a row, write lock, or to explicitly prevent a row from being updated by any other session, read lock. Normally, row write locks are acquired implicitly as a result of updating rows. Read locks are usually not required because of record versioning. However, in some cases a transaction may desire to explicitly lock a row to enforce serialization, or to ensure that a subsequent operation will succeed by virtue that required locks have already been taken.

```cpp
JET_ERR JET_API JetGetLock(
  __in          JET_SESID sesid,
  __in          JET_TABLEID tableid,
  __in          JET_GRBIT grbit
);
```

### Parameters

*sesid*

The session that will be used for this call.

*tableid*

The cursor that will be used for this call.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following:


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitReadLock</p> | <p>This flag causes a read lock to be acquired on the current record. Read locks are incompatible with write locks already held by other sessions but are compatible with read locks held by other sessions.</p> | 
| <p>JET_bitWriteLock</p> | <p>This flag causes a write lock to be acquired on the current record. Write locks are not compatible with write or read locks held by other sessions but are compatible with read locks held by the same session.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>The given <em>grbit</em> is neither JET_bitReadLock or JET_bitWriteLock. It must be one of these two flags.</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>Cursor must be on a record in order to acquire a lock. Locks are always on records.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errNotInTransaction</p> | <p>Locks can only be acquired by sessions in a transaction.</p> | 
| <p>JET_errPermissionDenied</p> | <p>Cursor cannot be read only and acquire a write lock.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errTransReadOnly</p> | <p>Session must have write permissions to acquire write lock.</p> | 
| <p>JET_errWriteConflict</p> | <p>The error returned when a conflicting lock is requested.</p> | 



On success, session has acquired requested lock.

On failure, session has not acquired requested lock.

#### Remarks

Write locks cannot be acquired with sessions or cursors that have read-only permissions, even if the session and cursor ultimately do not perform an update operation. Both the session and the cursor must have write privileges in order to acquire a write lock.

Read and write locks are a means of pessimistic locking. Pessimistic locking expects multiple concurrent sessions to conflict and acquire locks in advance to ensure that their operations succeed.

Most operations will be serializable by virtue of locks implicitly taken. However, some operations will not. To illustrate this, consider the two transactions,

T1 : R(A), U(B)

T2 : R(B), U(A)

Record level versioning will ensure that each transaction when executed concurrently will see the original values for A and B. There is no serial order of execution that could produce the same results for A and B in the case that the results are dependent upon the data read. In order for the application to make this transaction serializable, it should acquire an explicit read lock on A and B in each transaction when the value is read.

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
[JetPrepareUpdate](./jetprepareupdate-function.md)  
[JetStopService](./jetstopservice-function.md)  
[JetUpdate](./jetupdate-function.md)
