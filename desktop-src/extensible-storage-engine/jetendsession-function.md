---
description: "Learn more about: JetEndSession Function"
title: JetEndSession Function
TOCTitle: JetEndSession Function
ms:assetid: a9a8f98a-258e-4fbb-bed0-657581984a07
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294054(v=EXCHG.10)
ms:contentKeyID: 32765660
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetEndSession
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

# JetEndSession Function


_**Applies to:** Windows | Windows Server_

## JetEndSession Function

The **JetEndSession** function ends the session, and cleans up and deallocates any resources associated with the specified session.

```cpp
    JET_ERR JET_API JetEndSession(
      __in          JET_SESID sesid,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to end. Associated resources are released when the session ends.

*grbit*

Reserved. This parameter can contain the JET_bitForceSessionClosed flag, but this flag is reserved and setting it has no effect.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters that was provided contained an unexpected value, or the combination of several parameter values yielded an unexpected result.</p> | 
| <p>JET_errInvalidSesid</p> | <p>The session was not a valid JET session.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errOutOfMemory</p> | <p>The operation failed because memory could not be allocated.</p> | 
| <p>JET_errSessionInUse</p> | <p>This means the session was in use on another thread, or the session was not set or reset properly.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errOutOfBuffers</p> | <p>System error that indicates that there are no more buffers.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, the session handle is closed, and unavailable, and all resources related to this session are cleaned up.

On failure, there are several additional errors that could occur as part of sort table close, cursor close, and transaction rollback. These errors are fairly unlikely, and extremely unlikely if your sessions are completely not in use when **JetEndSession** is called. These errors will be returned if some part of the session was unable to be cleaned up properly.

#### Remarks

This API will rollback any open transactions (not committed to level 0). Also all cursors associated with this session, and any sort tables that have been created or opened will be cleaned up.

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
[JetBeginSession](./jetbeginsession-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[JetStopService](./jetstopservice-function.md)
