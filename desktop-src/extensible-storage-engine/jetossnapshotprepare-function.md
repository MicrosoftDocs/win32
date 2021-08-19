---
description: "Learn more about: JetOSSnapshotPrepare Function"
title: JetOSSnapshotPrepare Function
TOCTitle: JetOSSnapshotPrepare Function
ms:assetid: 364cbcba-7ddb-4748-8417-e885a5984b0d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269224(v=EXCHG.10)
ms:contentKeyID: 32765526
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOSSnapshotPrepare
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

# JetOSSnapshotPrepare Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotPrepare Function

The **JetOSSnapshotPrepare** function begins the preparations for a snapshot session. A snapshot session is a short time interval in which the engine does not issue any write IOs to disk, so that the engine can participate in a volume snapshot session (when driven by a snapshot writer).

**Windows XP:**  **JetOSSnapshotPrepare** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetOSSnapshotPrepare(
      __out         JET_OSSNAPID* psnapId,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*psnapId*

The identifier of the snapshot session to be started.

*grbit*

The options for this call. This parameter can have a combination of the following values.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>0</p> | <p>Normal snapshot.</p> | 
| <p>JET_bitIncrementalSnapshot</p> | <p>Only log files will be taken.</p> | 
| <p>JET_bitCopySnapshot</p> | <p>A copy snapshot (normal or incremental) with no log truncation.</p> | 
| <p>JET_bitContinueAfterThaw</p> | <p>The snapshot session occurs after <a href="gg269229(v=exchg.10).md">JetOSSnapshotThaw</a> and will require a <a href="gg294136(v=exchg.10).md">JetOSSnapshotEnd</a> function call.</p> | 
| <p>JET_bitExplicitPrepare</p> | <p>No instances will be prepared by default.</p><p><strong>Windows 7:</strong>  JET_bitExplicitPrepare is introduced in Windows 7.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidParameter</p> | <p>The snapshot ID pointer is NULL or the <em>grbit</em> parameter is invalid.</p> | 
| <p>JET_errOSSnapshotInvalidSequence</p> | <p>A snapshot session is already in progress and the operation is not allowed to have more then one snapshot session at any given time.</p> | 



If this function succeeds, a snapshot session will be able to start at any time with the IO freeze phase. The identifier for the session will be returned and must be used in the subsequent calls for the snapshot session.

The running instances of the engine will now be considered part of the snapshot session.

**Windows Vista:**  To specify a different subset of instances, the [JetOSSnapshotPrepareInstance](./jetossnapshotprepareinstance-function.md) can be called.

The normal API sequence call is: **JetOSSnapshotPrepare**, optionally followed by one or more calls to [JetOSSnapshotPrepareInstance](./jetossnapshotprepareinstance-function.md), then followed by [JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md). Once the freeze is started, it can be terminated using [JetOSSnapshotThaw](./jetossnapshotthaw-function.md). At any time after the prepare, the snapshot session can be abruptly terminated with [JetOSSnapshotAbort](./jetossnapshotabort-function.md).

If JET_bitContinueAfterThaw is specified after [JetOSSnapshotThaw](./jetossnapshotthaw-function.md), the snapshot session will remain (although the I/O will resume). This will enable a verification of the snapshot, and if needed, will enable log truncation using [JetOSSnapshotTruncateLog](./jetossnapshottruncatelog-function.md) and will require a call to [JetOSSnapshotEnd](./jetossnapshotend-function.md).

If this function fails, no change in the engine state occurs.

#### Remarks

Event log entries will be generated for the different steps of the snapshot.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_OSSNAPID](./jet-ossnapid.md)  
[JetOSSnapshotAbort](./jetossnapshotabort-function.md)  
[JetOSSnapshotEnd](./jetossnapshotend-function.md)  
[JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)  
[JetOSSnapshotPrepareInstance](./jetossnapshotprepareinstance-function.md)  
[JetOSSnapshotThaw](./jetossnapshotthaw-function.md)  
[JetOSSnapshotTruncateLog](./jetossnapshottruncatelog-function.md)
