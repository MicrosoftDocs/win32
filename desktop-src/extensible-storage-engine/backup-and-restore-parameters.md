---
description: "Learn more about: Backup and Restore Parameters"
title: Backup and Restore Parameters
TOCTitle: Backup and Restore Parameters
ms:assetid: 432aff79-8766-428a-9a14-530f575308d0
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269236(v=EXCHG.10)
ms:contentKeyID: 32765538
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# Backup and Restore Parameters


_**Applies to:** Windows | Windows Server_

## Backup and Restore Parameters

This topic contains parameters that are used for backup and restore.

*JET_paramAlternateDatabaseRecoveryPath*  
113  

The full path to each database is persisted in the transaction logs at run time. Ordinarily, these databases must remain at the original location for transaction replay to function correctly. This parameter can be used to force crash recovery or a restore operation to look for the databases referenced in the transaction log in the specified folder.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>""</p> | 
| <p>Type:</p> | <p>Folder Path (string)</p> | 
| <p>Valid Range:</p> | <p>0 – 246 characters</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramCleanupMismatchedLogFiles*  
77  

This parameter controls the outcome of [JetInit](./jetinit-function.md) when the database engine is configured to start using transaction log files on disk that are of a different size than what is configured. Normally, [JetInit](./jetinit-function.md) will successfully recover the databases but will fail with JET_errLogFileSizeMismatchDatabasesConsistent to indicate that the log file size is misconfigured. However, when this parameter is set to true then the database engine will silently delete all the old log files, start a new set of transaction log files using the configured log file size, and return JET_errSuccess.

This parameter is useful when the application wishes to transparently change its transaction log file size yet still work transparently in upgrade and restore scenarios.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>False</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>Yes</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramDeleteOutOfRangeLogs*  
52  

When this parameter is true, then any transaction log files found on disk that are not part of the current sequence of log files will be deleted by [JetInit](./jetinit-function.md). This may be used to automatically clean up extraneous log files after a restore operation.

**Windows XP:**  Introduced in Windows XP.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>False</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>Yes</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramOSSnapshotTimeout*  
82  

This parameter configures the amount of time allowed between a call to [JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md) and [JetOSSnapshotThaw](./jetossnapshotthaw-function.md) before a timeout occurs. Please see [JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md) and [JetOSSnapshotThaw](./jetossnapshotthaw-function.md) for more information. The timeout is in milliseconds.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>20000 (Windows XP and Windows Server 2003);</p><p>70000 (Windows Server 2003 SP1)</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 2147483647</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramZeroDatabaseDuringBackup*  
71  

When this parameter is true then every page in a database that is undergoing a streaming backup will be scrubbed of deleted data. It is important to note that the database pages that are being scrubbed are on disk. The full data set is backed up prior to the scrub process.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>False</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)  
[JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)  
[JetOSSnapshotThaw](./jetossnapshotthaw-function.md)
