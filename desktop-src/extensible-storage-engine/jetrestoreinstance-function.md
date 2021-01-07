---
description: "Learn more about: JetRestoreInstance Function"
title: JetRestoreInstance Function
TOCTitle: JetRestoreInstance Function
ms:assetid: 7ba2b6ee-96f5-44c5-9842-5e58580f60f1
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269306(v=EXCHG.10)
ms:contentKeyID: 32765597
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetRestoreInstanceW
- JetRestoreInstance
- JetRestoreInstanceA
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

# JetRestoreInstance Function


_**Applies to:** Windows | Windows Server_

## JetRestoreInstance Function

The **JetRestoreInstance** function restores and recovers a streaming backup of an instance including all the attached databases. It is designed to work with a backup created with the [JetBackupInstance](./jetbackupinstance-function.md) function. This is the simplest and most encapsulated one restore function.

**Windows XP:**  **JetRestoreInstance** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetRestoreInstance(
      __in          JET_INSTANCE instance,
      __in          JET_PCSTR sz,
      __in_opt      JET_PCSTR szDest,
      __in          JET_PFNSTATUS pfn
    );
```

### Parameters

*instance*

Specifies the instance to use for this call.

For Windows XP and later releases, the use of this parameter depends on the operating mode of the engine. If the engine is operating in legacy mode (Windows 2000 compatibility mode) where only one instance is supported then this parameter may either be NULL or it may be set to a valid output buffer containing NULL or JET_instanceNil that will return the global instance handle created as a side effect of the initialization. This instance handle can then be passed to any other API that takes an instance. If the engine is operating in multi-instance mode then this parameter must be set to a valid input buffer that contains the instance handle returned by [JetCreateInstance](./jetcreateinstance-function.md) that is being initialized.

*sz*

The folder where the backup is located. The backup should have been generated using the [JetBackup](./jetbackup-function.md) APIs.

*szDest*

Name of the folder where the database files from the backup set will be copied and recovered. If this is set to NULL (which is the case for the legacy [JetRestore](./jetrestore-function.md)), the database files will be copied and recovered to their original location.

*pfn*

The optional pointer to the function which will be called as notification information about the progress of the restore operation.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return code</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errSuccess</p></td>
<td><p>The operation completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>JET_errAlreadyInitialized</p></td>
<td><p>The operation failed because the engine is already initialized for this instance.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidLogSequence</p></td>
<td><p>The set of log files from the backup set and from the current log path do not match.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This error will be returned by <strong>JetRestoreInstance</strong> when the engine is in multi-instance mode and pinstance refers to an invalid instance Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidPath</p></td>
<td><p>The operation failed because some of paths provided are invalid (the backup path, the destination path, the log or system path for the instance).</p></td>
</tr>
<tr class="even">
<td><p>JET_errPageSizeMismatch</p></td>
<td><p>The operation failed because the engine is configured to use a database page size (using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> for <a href="gg269337(v=exchg.10).md">JET_paramDatabasePageSize</a>) that does not match the database page size used to create the transaction log files or the databases associated with the transaction log files.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errRunningInMultiInstanceMode</p></td>
<td><p>The operation failed because the parameters implied single instance mode (Windows 2000 compatibility mode) and the engine is already in multi-instance mode.</p></td>
</tr>
</tbody>
</table>


On success, database files from the backup set will be restored over to their location and recovery will be run such that the databases will be in a clean transactional consistency state. Recovery will replay the log files from the backup set and the log files from the log path if such files do exists. This recovery will result in changes to the checkpoint file, the transaction log files, and any databases referenced by those transaction log files.

On failure, the instance remains in an uninitialized state. The state of the transaction log files and any databases referenced by those transaction log files will likely have been changed in the attempt to initialize the restore and recover the databases.

#### Remarks

The recovery process will reconstruct the databases attached to the instance during the backup and save the changes back to the database files. The result will be databases that are transaction consistent. If possible, it will also save to the database the changes done since the backup was taken until the most recent change found in the transaction logs. This would be possible if the transaction logs generated since the backup was taken are still present in the transaction log directory. Note that if circular logging was enabled for the instance, the transaction logs generated are reused such that the recovery will be able to save the changes which took place up to the backup moment. In any case, it is possible for this process to take quite some time if the number of transaction log files to replay against the databases is large.

**JetRestoreInstance** must be called on an instance which was already created using [JetCreateInstance](./jetcreateinstance-function.md).

Because during recovery a significant number of database pages and transaction logs will be used, there is an entire series of error which might be returned by these functions. Such errors can be from temporary resource allocation failures like Jet_errOutOfMemory to errors representing physical corruptions like JET_errReadVerifyFailure, JET_errLogFileCorrupt or JET_errBadPageLink. These errors are almost always caused by hardware problems and thus cannot be avoided. File mismanagement will manifest itself most often as JET_errMissingLogFile or JET_errAttachedDatabaseMismatch or JET_errDatabaseSharingViolation or JET_errInvalidLogSequence. These errors are preventable by the application. The application must be careful to protect the repository of these files from manipulation by outside forces such as the user or other applications. If the application desires to destroy an instance entirely then all the files associated with the instance must be deleted. These include the checkpoint file, the transaction log files, and any database files attached to the instance.

The different steps of the recovery will have Event Log entries generated including the transaction log replay progress and the final result of the restore.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista or Windows XP.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008 or Windows Server 2003.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
<tr class="even">
<td><p><strong>Library</strong></p></td>
<td><p>Use ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DLL</strong></p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
<tr class="even">
<td><p><strong>Unicode</strong></p></td>
<td><p>Implemented as <strong>JetRestoreInstanceW</strong> (Unicode) and <strong>JetRestoreInstanceA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetBackup](./jetbackup-function.md)  
[JetBackupInstance](./jetbackupinstance-function.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
