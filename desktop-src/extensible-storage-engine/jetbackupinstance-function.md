---
description: "Learn more about: JetBackupInstance Function"
title: JetBackupInstance Function
TOCTitle: JetBackupInstance Function
ms:assetid: 82486441-5037-440b-8632-038e953ad870
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269318(v=EXCHG.10)
ms:contentKeyID: 32765608
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetBackupInstanceW
- JetBackupInstanceA
- JetBackupInstance
topic_type: 
- kbArticle
- apiref
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetBackupInstance Function


_**Applies to:** Windows | Windows Server_

## JetBackupInstance Function

The **JetBackupInstance** function performs a streaming backup of an instance, including all the attached databases, to a directory. With multiple backup methods supported by the engine, this is the simplest and most encapsulated function.

**Windows XP:  JetBackupInstance** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetBackupInstance(
      __in          JET_INSTANCE instance,
      __in          JET_PCSTR szBackupPath,
      __in          JET_GRBIT grbit,
      __in          JET_PFNSTATUS pfnStatus
    );
```

### Parameters

*instance*

The instance of the database to backup.

*szBackupPath*

The directory where the backup is stored. If the backup path is NULL to use the function will truncate the logs, if possible.

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitBackupAtomic</p> | <p>Creates a full backup of the database. This allows the preservation of an existing backup in the same directory if the new backup fails.</p> | 
| <p>JET_bitBackupIncremental</p> | <p>Creates an incremental backup as opposed to a full backup. This means that only the log files created since the last full or incremental backup will be backed up.</p> | 
| <p>JET_bitBackupSnapshot</p> | <p>Reserved for future use.</p> | 



*pfnStatus*

Pointer to the [JET_PFNSTATUS](./jet-pfnstatus-callback-function.md) callback function, which provides notification information about the progress of the backup operation.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBackupInProgress</p> | <p>A backup is already in progress for the same instance. Multiple backups are not allowed at the same time.</p> | 
| <p>JET_errBackupNotAllowedYet</p> | <p>The instance is not ready yet for backup as it is initializing.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg294108(v=exchg.10).md">JetStopServiceInstance</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>The operation cannot complete because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p><strong>Windows XP:  </strong>This return value is introduced in Windows XP.</p> | 
| <p>JET_errInvalidBackup</p> | <p>An incremental backup is not allowed if circular logging is on.</p> | 
| <p>JET_errInvalidGrbit</p> | <p>The specified options are invalid.</p> | 
| <p>JET_errInvalidParameter</p> | <p>An invalid parameter was passed into the API.</p> | 
| <p>JET_errInvalidPath</p> | <p>The destination path does not exist.</p> | 
| <p>JET_errLoggingDisabled</p> | <p>The instance is running without logging. No backup is allowed.</p> | 
| <p>JET_errLogReadVerifyFailure</p> | <p>There was a checksum verification error on a log file.</p> | 
| <p>JET_errLogWriteFail</p> | <p>The logging for the instance is temporary or permanently disabled due to an unexpected error.</p> | 
| <p>JET_errNotInitialized</p> | <p>The operation cannot complete because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errReadVerifyFailure</p> | <p>There was a checksum verification error on a database page.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>The operation cannot complete because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p><strong>Windows XP:  </strong>This return value is introduced in Windows XP.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance associated with the session is being shut down.</p> | 



After the function returns success, in the backup directory all the files needed for a restore up to the moment of the backup will be present. If this is a full backup, the files will be the database files and the log files needed to bring the database to a consistent state. If this is an incremental backup, only log files will be added to the directories but the already existing files (databases and log files) together with the new log files will be able to be restored and bring the database back to the state at the moment of the backup.

As a side effect of the backup, the log files which are not longer needed will be truncated.

In the same time, the database headers will be updated with the information when the last backup took place.

On failure, there will not be any files in the backup directory destination so no restore will be possible. In the same time, the current log files will not be truncated.

#### Remarks

The different steps of the backup will have Event Log entries generated including the file names, the log truncation and the final result of the backup.

Incremental backup are possible only after a full backup was taken. Also, incremental backups are possible only if circular logging is turned off. It is recommended that the backup directory should not contain other files then the one involved in the backup or added by a previous successful backup.

The backup directory should exist unless the parameter *JET_paramCreatePathIfNotExist* is set for the instance. For information, see [System Parameters](./extensible-storage-engine-system-parameters.md).

The backup will do checksum verification on all the used database pages and starting with Windows Server 2003, on the log files as well. This gives an opportunity to estimate the health of the database even for pages which are not read during normal operations. If any such corruption will be encountered, the backup will fail.

During the backup, the current log file will be finished and we will start a new log generation. This will allow copying the needed log files because the last needed one will not be in use anymore.

It is strongly recommended that the backup should not be used for other purposed other then the backup and restored at the engine level. This will minimize the change of getting errors during the backup and restore operations.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetBackupInstanceW</strong> (Unicode) and <strong>JetBackupInstanceA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_PFNSTATUS](./jet-pfnstatus-callback-function.md)  
[JetRestore](./jetrestore-function.md)  
[JetRestore2](./jetrestore2-function.md)  
[JetRestoreInstance](./jetrestoreinstance-function.md)  
[JetStopServiceInstance](./jetstopserviceinstance-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
