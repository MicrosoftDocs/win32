---
description: "Learn more about: JetDupSession Function"
title: JetDupSession Function
TOCTitle: JetDupSession Function
ms:assetid: fa8fbaca-fe48-401e-9700-1303f4842ad9
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294141(v=EXCHG.10)
ms:contentKeyID: 32765755
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetDupSession
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

# JetDupSession Function


_**Applies to:** Windows | Windows Server_

## JetDupSession Function

The **JetDupSession** function starts a session, and initializes and returns an ESE session handle ([JET_SESID](./jet-sesid.md)). Sessions control all access to the database and are used to control the scope of transactions. The session can be used to begin, commit, or abort transactions. The session is also used to attach, create, or open a database. The session is used as the context for all DDL and DML operations. To increase concurrency and parallel access to the database, multiple sessions can be begun.

**Note** This API will act in all ways as a [JetBeginSession](./jetbeginsession-function.md) called on the instance of the session passed in. This function is not recommended, [JetBeginSession](./jetbeginsession-function.md) is preferred.

```cpp
    JET_ERR JET_API JetDupSession(
      __in          JET_SESID sesid,
      __out         JET_SESID* psesid
    );
```

### Parameters

*sesid*

The session to use as the source for duplicating or beginning the session.

*psesid*

A pointer to the variable that the session handle initializes on successful return.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errOutOfMemory</p> | <p>The operation failed because memory could not be allocated.</p> | 
| <p>JET_errOutOfSessions</p> | <p>The number of sessions the engine will allow the client to start is limited. This value can be changed using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with the <em>JET_paramMaxSessions</em> constant. The default number of sessions is 16. See <a href="gg294139(v=exchg.10).md">System Parameters</a> for details about <em>JET_paramMaxSessions</em>.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, the session handle is initialized, and may be used for database operations.

On failure, there are no available sessions or a new session was unable to be initialized.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_SESID](./jet-sesid.md)  
[JetBeginSession](./jetbeginsession-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[JetStopService](./jetstopservice-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
