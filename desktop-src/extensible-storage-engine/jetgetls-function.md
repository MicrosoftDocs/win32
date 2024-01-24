---
description: "Learn more about: JetGetLS Function"
title: JetGetLS Function
TOCTitle: JetGetLS Function
ms:assetid: 411baf34-d167-4633-81af-be4886f4a646
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269234(v=EXCHG.10)
ms:contentKeyID: 32765536
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetLS
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

# JetGetLS Function


_**Applies to:** Windows | Windows Server_

## JetGetLS Function

The **JetGetLS** function enables the application to retrieve the context handle known as Local Storage that is associated with a cursor or the table associated with that cursor. This context handle must have been previously set using [JetSetLS](./jetsetls-function.md). **JetGetLS** can also be used to simultaneously fetch the current context handle for a cursor or table and reset that context handle.

**Windows XP:  JetGetLS** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetGetLS(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out         JET_LS* pls,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*pls*

The output buffer that receives the context handle currently associated with the cursor or table.

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitLSCursor</p> | <p>Indicates that the context handle associated with the given cursor should be retrieved.</p><p>If neither JET_bitLSCursor nor JET_bitLSTable is specified then JET_bitLSCursor is presumed.</p><p>This option cannot be used with JET_bitLSTable. The operation will fail with JET_errInvalidgrbit if this is attempted.</p> | 
| <p>JET_bitLSTable</p> | <p>Indicates that the context handle associated to the table that contains the given cursor should be retrieved. It is illegal to use this option with JET_bitLSCursor. The operation will fail with JET_errInvalidgrbit if this is attempted.</p> | 
| <p>JET_bitLSReset</p> | <p>Indicates that the context handle for the chosen object should be reset to JET_LSNil. The current value of the context handle is returned in the output buffer.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>One of the options requested was invalid, used in an illegal manner, or not implemented.</p><p>This can happen for <strong>JetGetLS</strong> when both JET_bitLSCursor and JET_bitLSTable are set.</p> | 
| <p>JET_errLSNotSet</p> | <p>The context handle could not be returned because no context handle is currently associated with the requested object.</p><p><strong>Note  </strong> This error is not returned if JET_bitLSReset is specified yet no context handle was associated with the requested object.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, the context handle was successfully retrieved from the requested object. If JET_bitLSReset was specified then that context handle was also successfully removed from the object. No change to the database state will occur.

On failure, no change to the state of the requested object has occurred. No change to the database state will occur.

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
[JET_LS](./jet-ls.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetSetLS](./jetsetls-function.md)
