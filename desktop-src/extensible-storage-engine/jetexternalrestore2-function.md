---
description: "Learn more about: JetExternalRestore2 Function"
title: JetExternalRestore2 Function
TOCTitle: JetExternalRestore2 Function
ms:assetid: 66331be0-7abc-43a0-8b8b-dbdd227c918e
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269272(v=EXCHG.10)
ms:contentKeyID: 32765574
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetExternalRestore2W
- JetExternalRestore2A
- JetExternalRestore2
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

# JetExternalRestore2 Function


_**Applies to:** Windows | Windows Server_

## JetExternalRestore2 Function

The **JetExternalRestore2** function restores an external backup that was taken with the external backup APIs and provides checkpoints to use for circular logging operations. This is known as hard recovery, which is similar but different than soft recovery as performed by the [JetInit](./jetinit-function.md) function.

**Windows XP:  JetExternalRestore2** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetExternalRestore2(
      __in          JET_PSTR szCheckpointFilePath,
      __in          JET_PSTR szLogPath,
      __in_opt      JET_RSTMAP* rgrstmap,
      __in          long crstfilemap,
      __in          JET_PSTR szBackupLogPath,
      __in_out      JET_LOGINFO* pLogInfo,
      __in_opt      JET_PSTR szTargetInstanceName,
      __in_opt      JET_PSTR szTargetInstanceLogPath,
      __in_opt      JET_PSTR szTargetInstanceCheckpointPath,
      __in          JET_PFNSTATUS pfn
    );
```

### Parameters

*szCheckpointFilePath*

The path for the checkpoint file to use during recovery if *szTargetInstanceCheckpointPath* is not specified or that path has an active or running instance.

*szLogPath*

The path or directory for the logs for the final phase (undo) of the recovery and possibly for the roll forward logs. This path may be the same as the *szBackupLogPath*.

*rgrstmap*

This is an array of [JET_RSTMAP](./jet-rstmap-structure.md) structures. This is a map of old and new database paths or filenames. This is used because the databases may need to be recovered to a location other than the location they were backed up from. In the case where multiple databases are attached to a single logging set, the restore map can specify a subset of the databases to restore.

*crstfilemap*

The number of entries in the *rgrstmap* array parameter.

*szBackupLogPath*

The path to the directory where the log files are restored. These are the logs that were read off during the external backup sequence. This path may be the same as the *szLogPath*.

*pLogInfo*

The *pLogInfo* describes several aspects of the backup logs to recovery, this parameter allows **JetExternalRestore2** to take the explicit *genLow* and *genHigh* parameters that **JetExternalRestore2** has, as well as the base log name, instead of a presumed log base name of "edb".

*szTargetInstanceName*

This parameter is deprecated and cannot be used in your application.

*szTargetInstanceLogPath*

The path for the roll forward logs if the location of the logs you would like to roll forward are in an active logging set or instance. This should not be specified if the target instance is using circular logging.

*szTargetInstanceCheckpointPath*

The path for the checkpoint during recovery if there is no active instance running at this target. This should not be specified if the target instance is using circular logging.

*pfn*

The status callback, which reports the progress of the recovery.

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
<td><p>JET_errBadRestoreTargetInstance</p></td>
<td><p>The <em>szTargetInstanceLogPath</em> specified does not belong to an initialized instance. This error will only be returned in Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errDatabaseCorrupted</p></td>
<td><p>This indicates the database was corrupted, or an unrecognized file.</p></td>
</tr>
<tr class="even">
<td><p>JET_errEndingRestoreLogTooLow</p></td>
<td><p>This error is returned if one for the log files in the <em>szBackupLogPath</em>, has a log generation above that specified in <em>genHigh</em> or <em>pLogInfo.ulGenHigh</em>.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errFileNotFound</p></td>
<td><p>The operation failed because it could not open the requested file because it could not be found at the specified path.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen for <a href="gg294088(v=exchg.10).md">JetExternalRestore</a>, and so on when the <em>szTargetCheckpointPath</em> and the <em>szTargetInstanceLogPath</em> are either not both specified or not both unspecified. That is, they must match, and be both specified or both unspecified.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidPath</p></td>
<td><p>The operation failed because the specified path could not be found.</p></td>
</tr>
<tr class="even">
<td><p>JET_errOutOfMemory</p></td>
<td><p>The operation failed because not enough memory could be allocated to complete it.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errRestoreOfNonBackupDatabase</p></td>
<td><p>This error is returned if the database file specified during restore is not a database that was backed up with external backup.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRunningInOneInstanceMode</p></td>
<td><p>The database engine cannot run external restore or hard recovery in single instance mode. This error will only be returned in Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errStartingRestoreLogTooHigh</p></td>
<td><p>This error is returned if one of the log files in the <em>szBackupLogPath</em>, has a log generation below that specified by the <em>genLow</em> or <em>pLogInfo.ulGenLow</em>.</p></td>
</tr>
</tbody>
</table>


On success, all databases from the *rgrstmap* are completely recovered and in a clean or consistent state. At this point the database can be remounted to an existing instance.

On failure, the engine could not recover the database. The database is in an invalid state, and in order to retry hard recovery the entire database must be restored again. Typically, the source of such a situation is disk or log corruption, or some other form of log mismanagement, or a non-continuous log set.

#### Remarks

See [JetExternalRestore](./jetexternalrestore-function.md).

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
<td><p>Implemented as <strong>JetExternalRestore2W</strong> (Unicode) and <strong>JetExternalRestore2A</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](./jet-err.md)  
[JET_LOGINFO](./jet-loginfo-structure.md)  
[JET_PFNSTATUS](./jet-pfnstatus-callback-function.md)  
[JET_RSTMAP](./jet-rstmap-structure.md)  
[JetBeginExternalBackup](./jetbeginexternalbackup-function.md)  
[JetExternalRestore](./jetexternalrestore-function.md)  
[JetInit](./jetinit-function.md)
