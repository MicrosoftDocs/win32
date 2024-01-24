---
description: "Learn more about: JetGetLogInfo Function"
title: JetGetLogInfo Function
TOCTitle: JetGetLogInfo Function
ms:assetid: a9d14830-d731-4d47-bdc2-c0660a08678e
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294055(v=EXCHG.10)
ms:contentKeyID: 32765665
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetLogInfoA
- JetGetLogInfoW
- JetGetLogInfo
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

# JetGetLogInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetLogInfo Function

The **JetGetLogInfo** function is used during a backup initiated by [JetBeginExternalBackup](./jetbeginexternalbackup-function.md) to query an instance for the names of database patch files and transaction log files that should become part of the backup file set. These files may subsequently be opened using [JetOpenFile](./jetopenfile-function.md) and read using [JetReadFile](./jetreadfile-function.md).

```cpp
    JET_ERR JET_API JetGetLogInfo(
      __out_opt     tchar* szz,
      __in          unsigned long cbMax,
      __out_opt     unsigned long* pcbActual
    );
```

### Parameters

*szz*

The output buffer that will receive the list of null terminated strings describing the set of database patch files and transaction log files that should be a part of the backup file set.

The list of strings returned in this buffer is in the same format as a multi-string used by the registry. Each null terminated string is returned in sequence followed by a final null terminator.

*cbMax*

The maximum size in bytes of the output buffer.

*pcbActual*

Receives the actual amount of string data received in the output buffer.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBackupAbortByServer</p> | <p>The operation failed because the current external backup has been aborted by a call to <a href="gg294067(v=exchg.10).md">JetStopBackup</a>. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidBackupSequence</p> | <p>The backup operation failed because it was called out of sequence. <strong>JetGetLogInfo</strong> will return this error if there are any outstanding file handles created using <a href="gg269249(v=exchg.10).md">JetOpenFile</a> for the instance.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen for <strong>JetGetLogInfo</strong> when the specified instance handle is invalid (Windows XP and later releases).</p> | 
| <p>JET_errNoBackup</p> | <p>The operation failed because no external backup is in progress.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errRunningInMultiInstanceMode</p> | <p>The operation failed because an attempt was made to use the engine in legacy mode (Windows 2000 compatibility mode) where only one instance is supported when in fact multiple instances already exist.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, the requested information on the set of database patch files and transaction log files that should be part of the backup file set will be placed in the output buffers where provided. The backup state machine will be advanced such that the backup of database files is no longer allowed. Only database patch files and transaction log files are permitted to be opened for backup beyond this point.

On failure, the state of the output buffers is undefined. The failure will result in the cancellation of the entire backup process for the instance.

#### Remarks

It is important to note that this API does not return an error or warning if the output buffer is too small to accept the full list of files that should be part of the backup file set. The application should always provide a buffer to receive the actual size of this list and use that information to determine if the list was truncated.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetGetLogInfoW</strong> (Unicode) and <strong>JetGetLogInfoA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_LOGINFO](./jet-loginfo-structure.md)  
[JetBeginExternalBackup](./jetbeginexternalbackup-function.md)  
[JetOpenFile](./jetopenfile-function.md)  
[JetReadFile](./jetreadfile-function.md)  
[JetStopBackup](./jetstopbackup-function.md)
