---
description: "Learn more about: JetRestore Function"
title: JetRestore Function
TOCTitle: JetRestore Function
ms:assetid: cdfb8823-6260-46f2-adfc-77e2512a68fd
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294093(v=EXCHG.10)
ms:contentKeyID: 32765708
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetRestore
- JetRestoreW
- JetRestoreA
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

# JetRestore Function


_**Applies to:** Windows | Windows Server_

## JetRestore Function

The **JetRestore** function restores and recovers a streaming backup of an instance, including all the attached databases. This function is primarily for backwards compatibility with Windows 2000 and earlier database engines, where only one instance of a database is allowed. In this case, the active instance is the instance that is restored. With **JetRestore**, the location for the restored databases cannot be specified.

```cpp
JET_ERR JET_API JetRestore(
  __in          JET_PCSTR sz,
  __in          JET_PFNSTATUS pfn
);
```

### Parameters

*sz*

The folder where the backup is located. The backup should have been generated using the [JetBackup](./jetbackup-function.md) function.

*pfn*

The optional pointer to the function which will be called as notification information about the progress of the restore operation.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errAlreadyInitialized</p> | <p>The operation failed because the engine is already initialized for this instance.</p> | 
| <p>JET_errInvalidLogSequence</p> | <p>The set of log files from the backup set and from the current log path do not match.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter.</p> | 
| <p>JET_errInvalidPath</p> | <p>The operation failed because some of paths provided are invalid (the backup path, the destination path, the log or system path for the instance).</p> | 
| <p>JET_errPageSizeMismatch</p> | <p>The operation failed because the engine is configured to use a database page size (using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> for <a href="gg269337(v=exchg.10).md">JET_paramDatabasePageSize</a>) that does not match the database page size used to create the transaction log files or the databases associated with the transaction log files.</p> | 
| <p>JET_errRunningInMultiInstanceMode</p> | <p>The operation failed because the parameters implied single instance mode (Windows 2000 compatibility mode) and the engine is already in multi-instance mode.</p> | 



On success, database files from the backup set will be restored over to their location and recovery will be run such that the databases will be in a clean transactional consistency state. Recovery will replay the log files from the backup set and the log files from the log path if such files do exists. This recovery will result in changes to the checkpoint file, the transaction log files, and any databases referenced by those transaction log files.

On failure, the instance remains in an uninitialized state. The state of the transaction log files and any databases referenced by those transaction log files will likely have been changed in the attempt to initialize the restore and recover the databases.

#### Remarks

The recovery process will reconstruct the databases attached to the instance during the backup and save the changes back to the database files. The result will be databases that are transaction consistent. If possible, it will also save to the database the changes done since the backup was taken until the most recent change found in the transaction logs. This would be possible if the transaction logs generated since the backup was taken are still present in the transaction log directory. Note that if circular logging was enabled for the instance, the transaction logs generated are reused such that the recovery will be able to save the changes which took place up to the backup moment. In any case, it is possible for this process to take quite some time if the number of transaction log files to replay against the databases is large.

**JetRestore** functions must be called on an instance before [JetInit](./jetinit-function.md) is called for that instance.

Because during recovery a significant number of database pages and transaction logs will be used, there is an entire series of error which might be returned by these functions. Such errors can be from temporary resource allocation failures like Jet_errOutOfMemory to errors representing physical corruptions like JET_errReadVerifyFailure, JET_errLogFileCorrupt or JET_errBadPageLink. These errors are almost always caused by hardware problems and thus cannot be avoided. File mismanagement will manifest itself most often as JET_errMissingLogFile or JET_errAttachedDatabaseMismatch or JET_errDatabaseSharingViolation or JET_errInvalidLogSequence. These errors are preventable by the application. The application must be careful to protect the repository of these files from manipulation by outside forces such as the user or other applications. If the application desires to destroy an instance entirely then all the files associated with the instance must be deleted. These include the checkpoint file, the transaction log files, and any database files attached to the instance.

The different steps of the recovery will have Event Log entries generated including the transaction log replay progress and the final result of the restore.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetRestoreW</strong> (Unicode) and <strong>JetRestoreA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetBackup](./jetbackup-function.md)  
[JetBackupInstance](./jetbackupinstance-function.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
