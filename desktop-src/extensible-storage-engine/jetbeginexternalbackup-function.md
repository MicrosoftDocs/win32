---
description: "Learn more about: JetBeginExternalBackup Function"
title: JetBeginExternalBackup Function
TOCTitle: JetBeginExternalBackup Function
ms:assetid: 702e6cbf-4648-40f2-b2eb-6194759d4cde
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269292(v=EXCHG.10)
ms:contentKeyID: 32765584
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetBeginExternalBackup
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

# JetBeginExternalBackup Function


_**Applies to:** Windows | Windows Server_

## JetBeginExternalBackup Function

The **JetBeginExternalBackup** function initiates an external backup while the engine and database is online and active. **JetBeginExternalBackup** is the first in a series of functions that must be called to execute a successful online (non-VSS based) backup.

An external backup can be used to implement full, incremental, or differential backups.

The backup will be fuzzy, in that the backup will be consistent to a single point in time in the transaction history, but controlling the exact point in time is not possible.

```cpp
    JET_ERR JET_API JetBeginExternalBackup(
      __in          JET_GRBIT grbit
    );
```

### Parameters

*grbit*

A group of bits that specify zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitBackupAtomic</p> | <p>This flag is deprecated. Usage of this bit will result in JET_errInvalidgrbit being returned.</p> | 
| <p>JET_bitBackupIncremental</p> | <p>Creates an incremental backup as opposed to a full backup. This means that only the log files since the last full or incremental backup will be backed up.</p> | 
| <p>JET_bitBackupSnapshot</p> | <p>Reserved for future use. Defined for Windows XP.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBackupInProgress</p> | <p>If an external backup or snapshot backup is already in process, this error will be returned, until <strong>JetBeginExternalBackup</strong> (or one of the variants of it) is called. ESE allows only one online backup at a time.</p> | 
| <p>JET_errBackupNotAllowedYet</p> | <p>The instance or database engine is either in recovery or in a shutdown or termination phase.</p> | 
| <p>JET_errCheckpointCorrupt</p> | <p>On a full backup, the checkpoint file could not be read, or the file could not be verified.</p> | 
| <p>JET_errCheckpointFileNotFound</p> | <p>On a full backup, the checkpoint file could not be found.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>The operation cannot complete because the instance that is associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p><strong>Windows XP:  </strong>This return value is introduced in Windows XP.</p> | 
| <p>JET_errInvalidBackup</p> | <p>Circular logging is enabled and the backup type specified is JET_bitBackupIncremental. See <a href="gg269235(v=exchg.10).md">JET_paramCircularLog</a> in the <strong>Transaction Log Errors</strong> for information about how to control circular or non-circular logging.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>One or more of the <em>grbit</em> members was invalid.</p> | 
| <p>JET_errLoggingDisabled</p> | <p>Recovery or logging is disabled. You cannot do an online backup if logging is disabled. For more information about logging and recovery, see <a href="gg269235(v=exchg.10).md">JET_paramRecovery</a>.</p> | 
| <p>JET_errLogWriteFail</p> | <p>The engine has stopped writing to the log drive, due to log being full or disk IO errors.</p> | 
| <p>JET_errMissingFullBackup</p> | <p>The incremental backup was specified (with JET_bitBackupIncremental), and never was a full backup taken for one of the attached databases for the logging set.</p> | 
| <p>JET_errNotInitialized</p> | <p>The operation cannot complete because the instance that is associated with the session has not yet been initialized.</p> | 
| <p>JET_errOutOfMemory</p> | <p>The operation failed because not enough memory could be allocated to complete it.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>The operation cannot complete because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errRunningInMultiInstanceMode</p> | <p>The operation failed because an attempt was made to use the engine in legacy mode (Windows 2000 compatibility mode) where only one instance is supported when in fact multiple instances already exist.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance that is associated with the session is being shut down.</p> | 



If the function succeeds, an external backup is initiated and the backup state engine is initialized. Subsequent APIs can now be called to complete the external backup sequence and stream or read off the database file, the database patch file (if supported), and the log file. An event can be logged that an external backup has begun.

If the function fails, the backup session will not be initiated. If another backup session is in progress, it will not be cancelled.

#### Remarks

The external backup process (as started by **JetBeginExternalBackup**) is designed to allow a fuzzy transaction online backup of the entire instance to a target device as a stream. The backup will contain all the database files that are attached to the instance using [JetAttachDatabase](./jetattachdatabase-function.md) (for a full backup), followed by their associated database patch files (if supported), and finally by the transaction log files that were generated during the backup process. The end result will be a set of files that can be restored from the stream, possibly combined with existing database and log files, and finally recovered to a consistent state.

The general order of operations for a full backup consists of the following calls. First, **JetBeginExternalBackup** is called to start the backup process. Then, [JetGetAttachInfo](./jetgetattachinfo-function.md) is called to get the list of databases that are attached to the instance that needs to be backed up. For each of these databases, [JetOpenFile](./jetopenfile-function.md) is called, followed by a number of [JetReadFile](./jetreadfile-function.md) calls, and then by a call to [JetCloseFile](./jetclosefile-function.md). Then, [JetGetLogInfo](./jetgetloginfo-function.md) is called to get a list of database patch and log files to be backed up. For each of these files, another sequence of [JetOpenFile](./jetopenfile-function.md), [JetReadFile](./jetreadfile-function.md), and [JetCloseFile](./jetclosefile-function.md) calls are made. Then, any undesired transaction log files are deleted using [JetTruncateLog](./jettruncatelog-function.md). Finally, the backup is ended by a call to [JetEndExternalBackup](./jetendexternalbackup-function.md).

It is also possible to modify this set of steps to perform an incremental backup of the instance. An incremental backup enumerates and backs up log files. Incremental backups are only possible if circular logging is not enabled.

It is also possible to modify this set of steps to allow subsequent differential backups of the instance to be performed. To perform a differential backup, do not call [JetTruncateLog](./jettruncatelog-function.md) in the previous full or incremental backup. By not calling [JetTruncateLog](./jettruncatelog-function.md), you enable subsequent backups to be differential with respect to the last full or incremental backup. Differential backups are only possible if circular logging is not enabled.

The database patch file is a special auxiliary file that is used to store database page images under certain circumstances during the backup. This file must be present in the same location as its associated database during a restore operation. This file is only used in Windows 2000. As a result, any application that is written to work against Windows 2000 and other releases must support database patch files, if they are present, but also must not fail if they are not present.

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
[JET_INSTANCE](./jet-instance.md)  
[JetAttachDatabase](./jetattachdatabase-function.md)  
[JetBeginExternalBackupInstance](./jetbeginexternalbackupinstance-function.md)  
[JetCloseFile](./jetclosefile-function.md)  
[JetEndExternalBackup](./jetendexternalbackup-function.md)  
[JetEndExternalBackupInstance2](./jetendexternalbackupinstance2-function.md)  
[JetGetAttachInfo](./jetgetattachinfo-function.md)  
[JetGetLogInfo](./jetgetloginfo-function.md)  
[JetOpenFile](./jetopenfile-function.md)  
[JetReadFile](./jetreadfile-function.md)  
[JetStopBackup](./jetstopbackup-function.md)  
[JetTruncateLog](./jettruncatelog-function.md)
