---
description: "Learn more about: JetSetSessionContext Function"
title: JetSetSessionContext Function
TOCTitle: JetSetSessionContext Function
ms:assetid: e44efadf-a5c7-408a-ad68-56646b6ea650
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294124(v=EXCHG.10)
ms:contentKeyID: 32765738
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetSessionContext
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

# JetSetSessionContext Function


_**Applies to:** Windows | Windows Server_

## JetSetSessionContext Function

The **JetSetSessionContext** function associates a session with the current thread using the given context handle. This association overrides the default engine requirement that a transaction for a given session must occur entirely on the same thread.

```cpp
    JET_ERR JET_API JetSetSessionContext(
      __in          JET_SESID sesid,
      __in          JET_API_PTR ulContext
    );
```

### Parameters

*sesid*

The session to use for this call.

*ulContext*

A unique identifier to which this session will be associated.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>The operation cannot complete because the instance that is associated with the session encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters that was provided contained an unexpected value, or the combination of several parameter values yielded an unexpected result. This error will be returned by <strong>JetSetSessionContext</strong> under the following conditions:</p><ul><li><p><em>ulContext</em> is NULL</p></li><li><p><em>ulContext</em> is -1</p></li></ul> | 
| <p>JET_errNotInitialized</p> | <p>The operation cannot complete because the instance that is associated with the session has not yet been initialized.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>The operation cannot complete because a restore operation is in progress on the instance that is associated with the session.</p> | 
| <p>JET_errSessionContextAlreadySet</p> | <p>The session could not be associated with the current thread because it has already been associated with a thread.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance that is associated with the session is being shut down.</p> | 



If this function succeeds, the session will be associated with the current thread. No change to the database state will occur.

If this function fails, the session state will remain unchanged. No change to the database state will occur.

#### Remarks

A session is usually bound to a specific thread for the duration of a transaction. This behavior is designed to help applications detect and prevent the conceptually ill-advised sharing of a single session amongst multiple threads. Sometimes, this simple check does not work with the application's architecture. For example, if the application is hosting server-side objects using a thread pool and transactions span multiple server calls to a given object then this protection may cause some of those calls to fail with JET_errSessionSharingViolation even though the usage pattern is correct. This situation is common for COM object servers.

**JetSetSessionContext** and [JetResetSessionContext](./jetresetsessioncontext-function.md) solve this problem by making this session sharing check a little more flexible. When the application starts to make a series of ESE API calls using a particular session, it first sets the session context to a given value. This action associates the session to the calling thread. In the given example, this context could be the address of the object that contains the JET session handle. Once the ESE API calls have been made, the application resets the session context. This action disassociates the session from the calling thread. The object and its session can then be used by another thread even if the session has an active transaction.

It is important to note that **JetSetSessionContext** must be called prior to opening a transaction on that session or the association will not work.

**JetSetSessionContext** is thread safe. Multiple threads can try to set a thread context on the same session at the same time and only one will win. This fact can be used by the application as a means to allocate a session from a pool without storing external state about its allocation.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_API_PTR](./jet-api-ptr.md)  
[JET_ERR](./jet-err.md)  
[JetResetSessionContext](./jetresetsessioncontext-function.md)  
[JET_SESID](./jet-sesid.md)  
[JetStopService](./jetstopservice-function.md)
