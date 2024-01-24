---
description: "Learn more about: JetBeginSession Function"
title: JetBeginSession Function
TOCTitle: JetBeginSession Function
ms:assetid: f1c33b78-f2d1-44ea-8ec9-94b729b94e24
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294131(v=EXCHG.10)
ms:contentKeyID: 32765745
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetBeginSessionA
- JetBeginSession
- JetBeginSessionW
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

# JetBeginSession Function


_**Applies to:** Windows | Windows Server_

## JetBeginSession Function

The **JetBeginSession** function starts a session and initializes and returns an ESE session handle ([JET_SESID](./jet-sesid.md)). Sessions control all access to the database and are used to control the scope of transactions. The session can be used to begin, commit, or abort transactions. The session is also used to attach, create, or open a database. The session is used as the context for all DDL and DML operations. To increase concurrency and parallel access to the database, multiple sessions can be begun.

```cpp
    JET_ERR JET_API JetBeginSession(
      __in          JET_INSTANCE instance,
      __out         JET_SESID* psesid,
      __in_opt      JET_PCSTR szUserName,
      __in_opt      JET_PCSTR szPassword
    );
```

### Parameters

*instance*

The database instance to use for this call.

*psesid*

Pointer to the variable that the session handle initializes on successful return.

*szUserName*

This parameter is reserved.

*szPassword*

This parameter is reserved.

### Return Value

This function allows for the return of any [JET_ERR](./jet-err.md)s that are defined in this API. For more information about Jet errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errOutOfMemory</p> | <p>The operation failed because memory could not be allocated.</p> | 
| <p>JET_errOutOfSessions</p> | <p>The number of sessions the engine will allow the client to start is limited. This value can be changed using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with the JET_paramMaxSessions constant. The default number of sessions is 16. See <a href="gg294139(v=exchg.10).md">System Parameters</a> for details about JET_paramMaxSessions.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, the session handle is initialized, and may be used for database operations.

On failure, there are no available sessions or a new session was unable to be initialized.

#### Remarks

Careful attention must be used when using sessions across different threads. A session tracks which thread it was used on during [JetBeginTransaction](./jetbegintransaction-function.md), [JetCommitTransaction](./jetcommittransaction-function.md), or [JetRollback](./jetrollback-function.md), and it will throw an error if used on multiple threads with an open transaction. The [JetResetSessionContext](./jetresetsessioncontext-function.md), [JetSetSessionContext](./jetsetsessioncontext-function.md) can change this behavior. Since the session is still a serialized context, and multiple database operations cannot be performed on a single session concurrently, only serially. However, you can use multiple sessions to achieve concurrent database access. Sessions can be used inside a transaction across threads by setting and resetting the session contexts.

The session handle should be closed with [JetEndSession](./jetendsession-function.md).

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetBeginSessionW</strong> (Unicode) and <strong>JetBeginSessionA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_SESID](./jet-sesid.md)  
[JetBeginTransaction](./jetbegintransaction-function.md)  
[JetCommitTransaction](./jetcommittransaction-function.md)  
[JetDupSession](./jetdupsession-function.md)  
[JetEndSession](./jetendsession-function.md)  
[JetResetSessionContext](./jetresetsessioncontext-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSetSessionContext](./jetsetsessioncontext-function.md)  
[JetStopService](./jetstopservice-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
