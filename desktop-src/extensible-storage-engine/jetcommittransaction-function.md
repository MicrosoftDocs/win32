---
description: "Learn more about: JetCommitTransaction Function"
title: JetCommitTransaction Function
TOCTitle: JetCommitTransaction Function
ms:assetid: 140ca76a-b3a7-4ae8-bc7e-73941fbfc759
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269191(v=EXCHG.10)
ms:contentKeyID: 32765494
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetCommitTransaction
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

# JetCommitTransaction Function


_**Applies to:** Windows | Windows Server_

## JetCommitTransaction Function

The **JetCommitTransaction** function commits the changes made to the state of the database during the current save point and migrates them to the previous save point. If the outermost save point is committed then the changes made during that save point will be committed to the state of the database and the session will exit the transaction.

```cpp
    JET_ERR JET_API JetCommitTransaction(
      __in          JET_SESID sesid,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitCommitLazyFlush</p> | <p>The transaction is committed normally but this API does not wait for the transaction to be flushed to the transaction log file before returning to the caller. This drastically reduces the duration of a commit operation at the cost of durability. Any transaction that is not flushed to the log before a crash will be automatically aborted during crash recovery during the next call to <a href="gg294068(v=exchg.10).md">JetInit</a>.</p><p>If JET_bitWaitLastLevel0Commit or JET_bitWaitAllLevel0Commit are specified, this option is ignored.</p><p>If this call to <strong>JetCommitTransaction</strong> does not match the first call to <a href="gg294083(v=exchg.10).md">JetBeginTransaction</a> for this session, this option is ignored. This is because the final action that occurs on the outermost save point is the determining factor in whether the entire transaction is actually committed to disk.</p> | 
| <p>JET_bitWaitAllLevel0Commit</p> | <p>All transactions previously committed by any session that have not yet been flushed to the transaction log file will be flushed immediately. This API will wait until the transactions have been flushed before returning to the caller.</p><p>This option may be used even if the session is not currently in a transaction.</p><p>This option cannot be used in combination with any other option.</p><p>This option is only available as of Windows Server 2003.</p> | 
| <p>JET_bitWaitLastLevel0Commit</p> | <p>If the session has previously committed any transactions and they have not yet been flushed to the transaction log file, they should be flushed immediately. This API will wait until the transactions have been flushed before returning to the caller. This is useful if the application has previously committed several transactions using JET_bitCommitLazyFlush and now wants to flush all of them to disk.</p><p>This option may be used even if the session is not currently in a transaction.</p><p>This option cannot be used in combination with any other option.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>One of the options requested was invalid or not implemented. This error will be returned by <strong>JetCommitTransaction</strong> when:</p><ul><li><p>An illegal <em>grbit</em> is specified.</p></li><li><p>JET_bitWaitLastLevel0Commit was specified in combination with another <em>grbit</em>.</p></li><li><p>JET_bitWaitAllLevel0Commit was specified in combination with another <em>grbit</em>.</p></li></ul> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errNotInTransaction</p> | <p>The operation failed because the given session is not in a transaction.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, any changes made to the database during the current save point for the given session will be committed and that save point will be ended. If the last save point for the session was ended then the transaction will optionally be flushed to the transaction log file and the session will exit the transaction.

On failure, the transactional state of the session will remain unchanged. No change to the database state will occur. The application should call [JetRollback](./jetrollback-function.md) to abort the transaction.

#### Remarks

There must be one call to **JetCommitTransaction** or [JetRollback](./jetrollback-function.md) to match every call to [JetBeginTransaction](./jetbegintransaction-function.md) for a given session.

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
[JetBeginTransaction](./jetbegintransaction-function.md)  
[JetCommitTransaction]()  
[JetRollback](./jetrollback-function.md)  
[JetStopService](./jetstopservice-function.md)
