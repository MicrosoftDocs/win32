---
description: "Learn more about: JetBackup Function"
title: JetBackup Function
TOCTitle: JetBackup Function
ms:assetid: afff995f-378a-4e67-b522-d5eafcbad57e
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294058(v=EXCHG.10)
ms:contentKeyID: 32765673
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetBackupA
- JetBackup
- JetBackupW
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

# JetBackup Function


_**Applies to:** Windows | Windows Server_

## JetBackup Function

The **JetBackup** function creates a backup of the database while the database is online. This function is primarily for backwards compatibility with Windows 2000 and earlier database engines, where only one instance of a database is allowed. In this case, the active instance is the instance that is backed up.

```cpp
    JET_ERR JET_API JetBackup(
      __in          JET_PCSTR szBackupPath,
      __in          JET_GRBIT grbit,
      __in          JET_PFNSTATUS pfnStatus
    );
```

### Parameters

*szBackupPath*

The directory where the backup is stored. If the backup path is NULL, the function will truncate the logs, if possible.

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitBackupAtomic</p> | <p>Creates a full backup of the database. This allows the preservation of an existing backup in the same directory if the new backup fails.</p> | 
| <p>JET_bitBackupIncremental</p> | <p>Creates an incremental backup as opposed to a full backup. This means that only the log files since the last full or incremental backup will be backed up.</p> | 



*pfnStatus*

Pointer to the [JET_PFNSTATUS](./jet-pfnstatus-callback-function.md) callback function, which provides notification information about the progress of the backup operation.

### Return Value

The function returns one of the [JET_ERR](./jet-err.md) error codes. The following are the most commonly returned. (For a complete list of errors for this API, see [Extensible Storage Engine Error Codes](./extensible-storage-engine-error-codes.md).)


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBackupInProgress</p> | <p>A backup is already in progress for the same instance. Multiple backups are not allowed at the same time.</p> | 
| <p>JET_errBackupNotAllowedYet</p> | <p>The instance is not ready yet for backup as it is initializing.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
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



If the function succeeds, all the files needed for a restore up to the moment of the backup will be contained in the backup directory. If this is a full backup, the files will be the database files and the log files needed to bring the database to a consistent state. If this is an incremental backup, only log files will be added to the directories, but the already existing files (databases and log files), together with the new log files, will be able to be restored to bring the database back to the state it was in at the moment that the backup began.

As a side effect of the backup, the log files which are no longer needed will be truncated.

In the same time, the database headers will be updated with the information when the last backup took place.

If the function fails, there will not be any files in the backup directory destination so no restore will be possible. In the same time, the current log files will not be truncated.

#### Remarks

The different steps of the backup will have Event Log entries generated, including the file names, the log truncation, and the final result of the backup.

Incremental backups are possible only after a full backup was taken. Also, incremental backups are possible only if circular logging is turned off. It is recommended that the backup directory should not contain any files other than the one used in the backup or added by a previous successful backup.

The backup directory should exist unless the parameter *JET_paramCreatePathIfNotExist* is set for the instance. For information, see [System Parameters](./extensible-storage-engine-system-parameters.md).

The backup will do a checksum verification on all the used database pages and starting with Windows Server 2003, on the log files as well. This gives an opportunity to estimate the health of the database, even for pages which are not read during normal operations. If any such corruption is encountered, the backup will fail.

During the backup, the current log file will be finished and a new log will be generated. This way, all of the necessary log files can be copies, because the current log will not be in use anymore.

It is strongly recommended that the backup not be used for any purpose other than the backup and restore at the engine level. This will minimize the chance of getting errors during the backup and restore operations.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetBackupW</strong> (Unicode) and <strong>JetBackupA</strong> (ANSI).</p> | 



#### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_PFNSTATUS](./jet-pfnstatus-callback-function.md)  
[JetRestore](./jetrestore-function.md)  
[JetRestore2](./jetrestore2-function.md)  
[JetRestoreInstance](./jetrestoreinstance-function.md)  
[JetStopService](./jetstopservice-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
