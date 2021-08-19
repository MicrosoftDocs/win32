---
description: "Learn more about: JetTruncateLogInstance Function"
title: JetTruncateLogInstance Function
TOCTitle: JetTruncateLogInstance Function
ms:assetid: 9b6852c6-a991-4d7b-bc54-49092f788751
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269352(v=EXCHG.10)
ms:contentKeyID: 32765639
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetTruncateLogInstance
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

# JetTruncateLogInstance Function


_**Applies to:** Windows | Windows Server_

## JetTruncateLogInstance Function

The **JetTruncateLogInstance** function is used during a backup initiated by [JetBeginExternalBackup](./jetbeginexternalbackup-function.md) to delete any transaction log files that will no longer be needed once the current backup completes successfully.

**Windows XP:**  **JetTruncateLogInstance** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetTruncateLogInstance(
      __in          JET_INSTANCE instance
    );
```

### Parameters

*instance*

The instance to use for this call.

For Windows 2000, the API variant that accepts this parameter is not available because only one instance is supported. The use of this one global instance is implied in this case.

For Windows XP and later releases, the API variant that does not accept this parameter can only be called when the engine is in legacy mode (Windows 2000 compatibility mode) where only one instance is supported. Otherwise, the operation will fail with JET_errRunningInMultiInstanceMode.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBackupAbortByServer</p> | <p><strong>Windows Server 2003:</strong>  This return value is introduced in Windows Server 2003.</p><p>The operation failed because the current external backup has been aborted by a call to <a href="gg294067(v=exchg.10).md">JetStopBackup</a>.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>The operation cannot complete because the instance that is associated with the session encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidBackupSequence</p> | <p>The backup operation failed because it was called out of sequence. <a href="gg269263(v=exchg.10).md">JetTruncateLog</a> will return this error if there are any outstanding file handles that were created using <a href="gg269249(v=exchg.10).md">JetOpenFile</a> for the instance.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters that was provided contained an unexpected value, or the combination of several parameters yielded an unexpected result. This can happen for <a href="gg269263(v=exchg.10).md">JetTruncateLog</a> when the specified instance handle is invalid.</p> | 
| <p>JET_errNoBackup</p> | <p>The operation failed because no external backup is in progress.</p> | 
| <p>JET_errNotInitialized</p> | <p>The operation cannot complete because the instance that is associated with the session has not yet been initialized.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>The operation cannot complete because a restore operation is in progress on the instance that is associated with the session.</p> | 
| <p>JET_errRunningInMultiInstanceMode</p> | <p>The operation failed because an attempt was made to use the engine in legacy mode (Windows 2000 compatibility mode) where only one instance is supported when in fact multiple instances already exist.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance that is associated with the session is being shut down.</p> | 



If this function succeeds, the set of transaction log files that will no longer be needed once the current backup completes successfully are deleted. The backup state machine will be advanced such that the backup of database files is no longer allowed. Only database patch files and transaction log files are permitted to be opened for backup beyond this point.

If this function fails, the backup state machine can be advanced such that the backup of database files is no longer allowed. Some number of transaction log files might be deleted that is less than the desired number, but they will always be deleted from oldest to youngest.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetBeginExternalBackup](./jetbeginexternalbackup-function.md)  
[JetOpenFile](./jetopenfile-function.md)  
[JetStopBackup](./jetstopbackup-function.md)  
[JetStopService](./jetstopservice-function.md)
