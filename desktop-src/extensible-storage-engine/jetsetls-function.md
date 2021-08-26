---
description: "Learn more about: JetSetLS Function"
title: JetSetLS Function
TOCTitle: JetSetLS Function
ms:assetid: 4fc77e09-7173-42e8-9dfd-9a8d8de2fb9b
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269243(v=EXCHG.10)
ms:contentKeyID: 32765545
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetLS
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

# JetSetLS Function


_**Applies to:** Windows | Windows Server_

## JetSetLS Function

The **JetSetLS** function enables the application to associate a context handle known as Local Storage with a cursor or the table associated with that cursor. This context handle can be used by the application to store auxiliary data that is associated with a cursor or table. The application is later notified using a runtime callback when the context handle must be released. This makes it possible to associate dynamically allocated state with a cursor or table.

**Windows XP:**  **JetSetLS** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetSetLS(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          JET_LS ls,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*ls*

The context handle to be associated with the cursor or table.

When JET_bitLSReset is specified then the actual value of this parameter is ignored and JET_LSNil is used.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitLSCursor</p> | <p>This option indicates that the context handle should be associated with the given cursor.</p><p>If neither JET_bitLSCursor nor JET_bitLSTable is specified then JET_bitLSCursor is presumed.</p><p>It is illegal to use this option with JET_bitLSTable. The operation will fail with JET_errInvalidgrbit if this is attempted.</p> | 
| <p>JET_bitLSReset</p> | <p>This option indicates that the specified context handle should be ignored and that the context handle for the chosen object should be reset to JET_LSNil.</p><p>It is important to note that this action will not result in a callback to cleanup the previous value of the context handle for the chosen object. Proper cleanup of the previous context handle can be achieved using <a href="gg269234(v=exchg.10).md">JetGetLS</a> with JET_bitLSReset. See <a href="gg269234(v=exchg.10).md">JetGetLS</a> for more information.</p> | 
| <p>JET_bitLSTable</p> | <p>This option indicates that the context handle should be associated with the table associated with the given cursor.</p><p>It is illegal to use this option with JET_bitLSCursor. The operation will fail with JET_errInvalidgrbit if this is attempted.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>One of the options requested was invalid, used incorrectly, or not implemented. This can happen for <strong>JetSetLS</strong> when JET_bitLSCursor and JET_bitLSTable are both specified.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errLSAlreadySet</p> | <p>The given context handle could not be associated with the requested object because it already had a context handle associated with it.</p> | 
| <p>JET_errLSCallbackNotSpecified</p> | <p>The given context handle could not be associated with the requested object because the runtime callback has not been configured for the instance associated with the session.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, the given context handle was successfully associated with the requested object. No change to the database state will occur.

On failure, no change to the state of the requested object has occurred. No change to the database state will occur.

#### Remarks

The Local Storage for a cursor or table should be viewed as a volatile cache. The application should first try to retrieve the context handle using [JetGetLS](./jetgetls-function.md). If the value is not set (that is it is JET_LSNil) then the application should create a new context and load it into the cache using **JetSetLS**. The application can purge the cache using a call to [JetGetLS](./jetgetls-function.md) with JET_bitLSReset. If the database engine purges the cache then a runtime callback will be generated to give the application a chance to cleanup that context. The callback type will be JET_cbtypFreeCursorLS for a context handle associated with a cursor and JET_cbtypFreeTableLS for a context handle associated with a table. In either case, the context handle will be passed as pvArg1. See [JET_CALLBACK](./jet-callback-callback-function.md) for more information.

The runtime callback must be properly configured for the instance associated with the given session before Local Storage can be used. This callback can be set using [JetSetSystemParameter](./jetsetsystemparameter-function.md) with [JET_paramRuntimeCallback](./callback-parameters.md). See [JetSetSystemParameter](./jetsetsystemparameter-function.md) and [JET_paramRuntimeCallback](./callback-parameters.md) in System Parameters for more information.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_CALLBACK](./jet-callback-callback-function.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_LS](./jet-ls.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetGetLS](./jetgetls-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
