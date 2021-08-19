---
description: "Learn more about: JetOSSnapshotFreeze Function"
title: JetOSSnapshotFreeze Function
TOCTitle: JetOSSnapshotFreeze Function
ms:assetid: 8dfbff20-199e-4d89-a33c-ae8e39b11ec1
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269332(v=EXCHG.10)
ms:contentKeyID: 32765622
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOSSnapshotFreezeA
- JetOSSnapshotFreezeW
- JetOSSnapshotFreeze
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

# JetOSSnapshotFreeze Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotFreeze Function

The **JetOSSnapshotFreeze** function starts a snapshot. While the snapshot is in progress, no write-to-disk activity by the engine can take place.

**Windows XP:**  **JetOSSnapshotFreeze** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetOSSnapshotFreeze(
      __in          const JET_OSSNAPID snapId,
      __out         unsigned long* pcInstanceInfo,
      __out         JET_INSTANCE_INFO** paInstanceInfo,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*snapId*

The identifier of the snapshot session.

*pcInstanceInfo*

The number of instances currently running in the engine that are part of the snapshot session.

*paInstanceInfo*

An array of structures, one for each running instance that is part of the snapshot session, describing the instance and the databases that are part of it.

*grbit*

The options for this call. This parameter is reserved for future use and the only valid value supported is 0.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidParameter</p> | <p>The pointers provided for the output parameters are NULL, the snapshot session is invalid, or the <em>grbit</em> parameter is invalid.</p> | 
| <p>JET_errOSSnapshotInvalidSequence</p> | <p>The snapshot session is not in the appropriate state to start a freeze (for example, a previous freeze failed on this session before).</p> | 
| <p>JET_errOSSnapshotNotAllowed</p> | <p>The engine is not in a state in which a snapshot can be performed. Either one or more streaming backups is already in progress, or one or more instances are going through recovery steps or terminating.</p> | 
| <p>JET_errOSSnapshotInvalidSnapId</p> | <p>The identifier for the snapshot session is not valid.</p> | 
| <p>JET_errOutOfMemory</p> | <p>The function failed due to an out-of-memory condition.</p> | 
| <p>JET_errOutOfThreads</p> | <p>The function failed because a new thread doing the freeze failed to start.</p> | 



If this function succeeds, there will not be any write IOs issued for the database files or for the log files that are part of instances that are frozen. Also, the instance information will be properly filled and it must be freed later on by calling [JetFreeBuffer](./jetfreebuffer-function.md) with the pointer to the instance info array that was returned.

If this function fails, the engine will keep running normally with the IOs occurring as usual. There is no need to call [JetOSSnapshotThaw](./jetossnapshotthaw-function.md) if the freeze fails. Also, the instance information will not be filled so there is no need to free this resource.

#### Remarks

During the freeze period, there will not be any write IOs issued to the attached databases or the transaction logs, although there might be write IOs issued to the temporary databases or streaming files.

The state in which the databases and the log files will be during the freeze (the state in which the files would be in a Volume Snapshot image) will be such that a normal recovery will be possible if those files are restored later.

Because there are no write operations during the freeze period, normal API calls into the engine might be stalled for that interval. The client application must be able to handle API calls that might take longer then normal if a freeze occurs.

Due to the possible effects described above, there is an internal timeout after which the snapshot session will stop the freeze phase even if the APIs doing the thaw or abort were not called. The value of the timeout can be changed using the [JET_paramOSSnapshotTimeout](./backup-and-restore-parameters.md) system parameter. Note that the typical freeze interval is in the range of 10 seconds with the default timeout somewhere around 60 seconds.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetOSSnapshotFreezeW</strong> (Unicode) and <strong>JetOSSnapshotFreezeA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_INSTANCE_INFO](./jet-instance-info-structure.md)  
[JET_OSSNAPID](./jet-ossnapid.md)  
[JetOSSnapshotAbort](./jetossnapshotabort-function.md)  
[JetOSSnapshotPrepare](./jetossnapshotprepare-function.md)  
[JetOSSnapshotPrepareInstance](./jetossnapshotprepareinstance-function.md)  
[JetOSSnapshotThaw](./jetossnapshotthaw-function.md)
