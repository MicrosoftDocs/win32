---
description: "Learn more about: JetBeginTransaction Function"
title: JetBeginTransaction Function
TOCTitle: JetBeginTransaction Function
ms:assetid: c5b2f9d7-157d-431d-a292-009c43773a9f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294083(v=EXCHG.10)
ms:contentKeyID: 32765698
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetBeginTransaction
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

# JetBeginTransaction Function


_**Applies to:** Windows | Windows Server_

## JetBeginTransaction Function

The **JetBeginTransaction** function causes a session to enter a transaction and create a new save point. This function can be called more than once on a single session to cause the creation of additional save points. These save points can be used to selectively keep or discard changes to the state of the database.

```cpp
    JET_ERR JET_API JetBeginTransaction(
      __in          JET_SESID sesid
    );
```

### Parameters

*sesid*

The session to use for this call.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errTransTooDeep</p> | <p>A new transaction cannot be started because the session is already at the maximum save point depth allowable by the database engine.</p> | 



On success, the provided session will be inside a transaction. If the session was previously inside of a transaction then a new save point will be created.

On failure, the transactional state of the session will remain unchanged. No change to the database state will occur.

#### Remarks

The database engine provides a snapshot isolation model for its transactions. This means that, when a session first enters into a transactional state, the session will see the entire database frozen in time at the start of the transaction. A session does not need to read lock any data because it can always access the appropriate version of that data. This means that a session that is updating data will never block a different session from reading that data.

Another implication of the use of snapshot isolation is the locking model used for updates. The database engine will award a write lock on a given piece of data to the first session that requests it. This write lock is released when the transaction is either committed or aborted completely such that the session is no longer in a transaction. While a session holds a write lock, any other session that requests the same write lock will not block until the write lock is available. Rather, that second session will immediately fail with JET_errWriteConflict. To resolve this conflict, the second session must abort (or commit) its transaction completely, wait some small period of time for the first session to commit or abort its transaction, and then start all over again.

In support of snapshot isolation, the database engine stores all versions of all modified data in memory since the time when the oldest active transaction on any session was first started. This has important implications for your application. Any behavior that causes a large number of versions to build up in memory may cause the instance to exhaust its maximum version store size (see [JET_paramMaxVerPages](./resource-parameters.md) in [System Parameters](./extensible-storage-engine-system-parameters.md) for more information). Such behavior includes, but is not limited to very large updates in a single transaction and very long running transactions. As a result, it is very important to properly configure the version store size for the expected transactional load of the application. It is also important to take great care to limit the number of updates performed in a single transaction. Furthermore, it is important to make transactions as short in duration as possible under high load scenarios.

It is highly recommended that the application always be in the context of a transaction when calling ESE APIs that retrieve or update data. If this is not done, the database engine will automatically wrap each ESE API call of this type in a transaction on behalf of the application. The cost of these very short transactions can add up quickly in some cases.

The default behavior of the engine is to restrict the use of a session to the same thread from the time the first call to **JetBeginTransaction** is made until the time when the matching call to [JetCommitTransaction](./jetcommittransaction-function.md) or [JetRollback](./jetrollback-function.md) is made. This behavior can be changed to remove this restriction by setting a custom session context using [JetSetSessionContext](./jetsetsessioncontext-function.md) and [JetResetSessionContext](./jetresetsessioncontext-function.md).

The database engine also supports transactional schema modifications. For example, it is possible to begin a new transaction, create a table, add a few columns, create an index or two, and then abort the transaction. The schema elements that were just added will be removed from the database. It is also possible to mix schema modifications and ordinary database updates in the same transaction.

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
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JetCommitTransaction](./jetcommittransaction-function.md)  
[JetGetSystemParameter](./jetgetsystemparameter-function.md)  
[JetResetSessionContext](./jetresetsessioncontext-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSetSessionContext](./jetsetsessioncontext-function.md)  
[JetStopService](./jetstopservice-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
