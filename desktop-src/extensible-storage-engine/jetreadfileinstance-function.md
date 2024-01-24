---
description: "Learn more about: JetReadFileInstance Function"
title: JetReadFileInstance Function
TOCTitle: JetReadFileInstance Function
ms:assetid: b17b4b43-86e5-4507-8a85-bbd5eac0aa3c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294060(v=EXCHG.10)
ms:contentKeyID: 32765675
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetReadFileInstance
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

# JetReadFileInstance Function


_**Applies to:** Windows | Windows Server_

## JetReadFileInstance Function

The **JetReadFileInstance** function retrieves the contents of a file opened with the [JetOpenFileInstance](./jetopenfileinstance-function.md) function.

**Windows XP**:   **JetReadFileInstance** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetReadFileInstance(
      __in          JET_INSTANCE instance,
      __in          JET_HANDLE hfFile,
      __out         void* pv,
      __in          unsigned long cb,
      __out_opt     unsigned long* pcb
    );
```

### Parameters

*instance*

The instance to use for a particular API call.

Note that for Windows 2000, the API variant that accepts this parameter is not available because only one instance is supported. The use of this one global instance is implied in this case.

For Windows XP and later releases, you can call the API variant that does not accept this parameter only when the engine is in legacy mode (Windows 2000 compatibility mode) in cases where only one instance is supported. Otherwise, the operation will fail and return the JET_errRunningInMultiInstanceMode error.

*hfFile*

The handle of the file to be read.

*pv*

The output buffer that will receive the file data.

*cb*

The maximum size, in bytes, of the output buffer.

*pcb*

The actual amount of file data retrieved.

### Return Value

This function facilitates the return of any [JET_ERR](./jet-err.md) data types that are defined in the Extensible Storage Engine (ESE) API. For more information about JET errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Meaning</p> | 
|--------------------|----------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBackupAbortByServer</p> | <p>The operation failed because the current external backup has been aborted by a call to the <a href="gg269240(v=exchg.10).md">JetStopService</a> function. This error will be returned only by Windows XP and later Windows versions.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to the <a href="gg269240(v=exchg.10).md">JetStopService</a> function.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error requiring that access to all data be revoked to protect the integrity of that data. This error will be returned only by Windows XP and later Windows versions.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the specified parameters contained either an unexpected value or a value that did not make sense when combined with the value of another parameter. This can happen for the <strong>JetReadFileInstance</strong> function when any of the following occurs:</p><ul><li><p>The specified instance handle is invalid. Windows XP and later Windows versions.</p></li><li><p>The output buffer size is not a multiple of the database page size (<a href="gg269337(v=exchg.10).md">JET_paramDatabasePageSize</a>). Windows XP and later Windows versions.</p></li><li><p>The output buffer size is smaller than three database pages (<a href="gg269337(v=exchg.10).md">JET_paramDatabasePageSize</a>), and this is the first call to the <strong>JetReadFileInstance</strong> function for the specified handle. Windows XP and later Windows versions.</p></li></ul> | 
| <p>JET_errLogReadVerifyFailure</p> | <p>The operation failed because unrecoverable data corruption was detected while reading a transaction log file. This error will be returned only by Windows XP and later Windows versions.</p> | 
| <p>JET_errNoBackup</p> | <p>The operation failed because no external backup is in progress.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with this session has not been initialized yet.</p> | 
| <p>JET_errReadVerifyFailure</p> | <p>The operation failed because unrecoverable data corruption was detected while reading a database page from a database file or database patch file.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with this session.</p> | 
| <p>JET_errRunningInMultiInstanceMode</p> | <p>The operation failed because an attempt was made to use the engine in legacy mode (Windows 2000 compatibility mode) in a case where only one instance is supported but multiple instances already exist.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with this session is being shut down.</p> | 



On success, the next chunk of data from the file will be read into the output buffer. The actual number of bytes retrieved will also be returned. The file offset at which the next read will occur will be advanced by this amount.

On failure, the state of the output buffer is undefined. The failure will result in the cancellation of the entire backup process for the current instance. In Windows XP and later Windows versions, the backup will not be canceled if an error occurred while reading a database file. However, the backup of that database file will still be canceled and the corresponding handle will automatically be closed.

#### Remarks

Any call to the **JetReadFileInstance** function made by using a handle that has already returned all the data in the underlying file (such as if a previous call returned fewer bytes than the size of the output buffer) will always succeed but will return zero bytes of data.

You should use a large output buffer to maximize backup performance. You might need to experiment to find the optimal tradeoff between resource consumption and throughput for a particular situation. In any case, the output buffer should be no smaller than 64 KB. The pointer that you pass to **JetReadFileInstance** must be aligned with a memory page boundary (either 4 KB or 8 KB). You can do this by calling the **VirtualAlloc** function.

Multiple concurrent calls to **JetReadFileInstance** made by using the same file handle are not supported. This means that it is not possible to queue several buffers for concurrent reading against the same file to achieve high sequential throughput. You should use a single large buffer instead.

If you have configured a particular instance such that database page scrubbing is enabled (see the [JET_paramCircularLog](./transaction-log-parameters.md) parameter in [System Parameters](./extensible-storage-engine-system-parameters.md)), deleted data will be removed from the database as a side-effect of a call to **JetReadFileInstance** against the database file.

It is very important to understand how backup and data corruption interact. If the database engine detects data corruption during a backup, it will fail the backup of either the affected database or the entire instance. This is a conscious design decision intended to protect against data loss. If the database engine allowed a backup to succeed where data corruption was present, it is possible that an older, uncorrupted backup could be discarded as a result. This would be unfortunate because then it would be possible to fix the data corruption on the live instance by restoring that backup and replaying all the transaction log files against that database. This zero-data-loss scenario presumes that circular logging is not enabled (see [JET_paramCircularLog](./transaction-log-parameters.md) in [System Parameters](./extensible-storage-engine-system-parameters.md)).

It is also important to understand that cases of data corruption are usually first detected during streaming backup. This is because streaming backup is the only process that routinely scans every single page of the database file. It is also likely that streaming backup will be the first process to detect the early signs of hardware failure as manifested by intermittent data corruption errors, because of both the amount of data retrieved by backup and the speed at which that data is retrieved.

Data corruption is detected by the database engine through the use of block checksums. These checksums are set just before a database page write and are verified on a database page read. This scheme enables the database engine to determine that data has been corrupted at some point, but it does not enable the database engine to determine the source of that corruption. Historically, instances of such data corruption have originated from sources other than the database engine itself.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p>Client</p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p>Server</p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p>Header</p> | <p>Is declared in Esent.h.</p> | 
| <p>Library</p> | <p>Uses ESENT.lib.</p> | 
| <p>DLL</p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_HANDLE](./jet-handle.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetOpenFileInstance](./jetopenfileinstance-function.md)  
[JetStopService](./jetstopservice-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
