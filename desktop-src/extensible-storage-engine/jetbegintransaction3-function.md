---
description: "Learn more about: JetBeginTransaction3 Function"
title: JetBeginTransaction3 Function
TOCTitle: JetBeginTransaction3 Function
ms:assetid: 7f8ed059-0b97-46fa-9925-e46cdcbee6ea
ms:mtpsurl: https://msdn.microsoft.com/library/JJ835043(v=EXCHG.10)
ms:contentKeyID: 49894665
ms.date: 04/11/2016
ms.topic: reference
dev_langs:
- c++
api_name: 
- JetBeginTransaction3
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetBeginTransaction3 Function


_**Applies to:** Windows | Windows Server_

The **JetBeginTransaction3** function causes a session to enter a transaction and create a new save point. This function can be called more than once in a single session to create additional save points. These save points can be used to selectively to keep or discard changes to the database.

The **JetBeginTransaction3** function was introduced in the Windows 8 operating system.

``` c++
JET_ERR JET_API JetBeginTransaction3(
  __in          JET_SESID sesid,
  __in          int64 trxid,
  __in          JET_GRBIT grbit
);
```

### Parameters

*sesid*

The session to use for this call.

*trxid*

An optional identifier supplied by the user to identify the transaction.

*grbit*

A group of bits that that specifies zero or more of the call option values listed in the following table.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitTransactionReadOnly</p> | <p>The transaction will not modify the database. If an update is attempted, that operation will fail with JET_errTransReadOnly response code. This option is ignored unless it is requested when the given session is not already in a transaction. This option is available in versions of the Windows operating system starting with Windows XP.</p> | 



### Return value

This function returns the [JET_ERR](./jet-err.md) data type with one of the return codes listed in the following table. For more information about the possible Extensible Storage Engine (ESE) errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to the <a href="gg269240(v=exchg.10).md">JetStopService</a> function.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This return code is returned by versions of Windows starting with Windows XP.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error is returned by versions of Windows starting with Windows XP.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errTransTooDeep</p> | <p>A new transaction cannot be started because the session is already at the maximum save point depth allowable by the database engine.</p> | 



On success, the provided session will be inside a transaction. If the session was previously inside a transaction, a new save point will be created.

On failure, the transactional state of the session will remain unchanged. No change to the database state will occur.

#### Remarks

For more information about how transactions work, see [JetBeginTransaction](./jetbegintransaction-function.md).

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows 8.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2012.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JetBeginTransaction](./jetbegintransaction-function.md)  
[JetCommitTransaction](./jetcommittransaction-function.md)  
[JetGetSystemParameter](./jetgetsystemparameter-function.md)  
[JetResetSessionContext](./jetresetsessioncontext-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSetSessionContext](./jetsetsessioncontext-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
